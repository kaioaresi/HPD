#!/usr/bin/env python3.5

import docker
import argparse
from datetime import datetime
import requests


'''
Exercicio final
cliente.containers.run('nginx',name='kaio', detach=True)
'''

# globais
parser = argparse.ArgumentParser(description='Docker-cli HPD.')
client = docker.from_env()


def logs(mensage, e, logfile='docker-cli.log'):
    data_agora = datetime.now().strftime('%d/%m/%Y %H:%M')
    with open('docker-cli.log', 'a') as log:
        texto = "%s \t %s \t %s \n" % (data_agora, mensage, str(e))
        log.write(texto)


def list_container():
    containers = client.containers.list(all)

    for container in containers:
            container_name = container.attrs['Name']
            container_img = container.attrs['Config']['Image']
            container_cmd = container.attrs['Config']['Cmd']

            print('O nome do container é "{}" está usando a image "{}" e o entrypoint é "{}"'.format(container_name, container_img, container_cmd))


def run_container(args):
    try:
        executando = client.containers.run(args.image, args.comando)
        print(executando)
    except docker.errors.ImageNotFound as e:
        print('Essa image não existe ou não está publica!')
        logs("Essa image não existe!", e)
    except docker.errors.APIError as e:
        print('Comando não encontrado!')
        logs("Comando não existe!", e)

def procura(image):
    list_contianers = client.containers.list(all)
    for container in list_contianers:
        image_container = container.attrs['Config']['Image']

        if image_container.lower() == image.lower():
            container_id = container.short_id
            print('Achei o container "{}" rodando com a image "{}"'.format(container_id, image_container))

def remove():
    # remove todos container com portas baixa
    list_contianers = client.containers.list(all)
    for container in list_contianers:
        container_port = container.attrs['HostConfig']['PortBindings']['80/tcp'][0]['HostPort']
        container_id = container.short_id
        print(container_port)
        if int(container_port) < 1024:
            print('O container "{}" está usnado uma porta baixa {} e será removido'.format(container_id, container_port))
            remove = container.remove(force=True)

'''
        if isinstance(container_port, dict):
            for port_container, port_host in container_port.items():
                port_host = str(port_host)
                port_host2 = ''.join(filter(str.isdigit, port_host))
                if int(port_host2) <= 1024:
                    print('Removendo container {}'.format(container.short_id))
                    remove = container.remove(force=True)
                else:
                    print('Demais contianer estão usando portas altas.')
'''


def nome_astronautas():

    lista_nomes = []
    url = "http://api.open-notify.org/astros.json"
    resposta = requests.get(url)
    saida_completa = resposta.json()

    # Pegando o numero de astronautas
    n_pessoas = saida_completa['number']

    # Capturando dados astronautas
    dados_people = saida_completa['people']

    # Criando uma lista com os nomes dos astronautas
    for i in range(0, n_pessoas):

        nome = dados_people[i]['name']
        lista_nomes.append(nome)
        i += 1

    return lista_nomes


def run_container_name(args):
    lista_nomes = nome_astronautas()

    for nome in lista_nomes:
        try:
            padronizando_nome = nome.lower().replace(" ", "_")
            print("Criando container com nome: ", padronizando_nome)
            client.containers.run(str(args.img), name=padronizando_nome, detach=True)
        except docker.errors.ImageNotFound as e:
            print('Essa image não existe ou não está publica!')
            logs("Essa image não existe!", e)


# Executando

#run_container_name("nginx")


subparser = parser.add_subparsers()

# Containers: Run container
cria_container = subparser.add_parser('containers')
cria_container.add_argument('--image', required=True, help='Informe o nome da image!')
#cria_container.add_argument('--comando', required=True, help='Informe qual comando será executa detro no container.')
cria_container.set_defaults(func=run_container_name)

# Realiza o tratamento dos arqumentos
cmd = parser.parse_args()
cmd.func(cmd)
