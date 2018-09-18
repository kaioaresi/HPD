#!/usr/bin/env python3.5

import docker
import argparse


parser = argparse.ArgumentParser(description='Docker-cli HPD.')

client = docker.from_env()

'''
def list_container():
    containers = client.containers.list(all)

    for container in containers:
            container_name = container.attrs['Name']
            container_img = container.attrs['Config']['Image']
            container_cmd = container.attrs['Config']['Cmd']
            print('O nome do container é "{}" está usando a image "{}" e o entrypoint é "{}"'.format(container_name, container_img, container_cmd))
'''

def list_container():
    containers = client.containers.list(all)

    for container in containers:
            container_name = container.attrs['Name']
            container_img = container.attrs['Config']['Image']
            container_cmd = container.attrs['Config']['Cmd']

            print('O nome do container é "{}" está usando a image "{}" e o entrypoint é "{}"'.format(container_name, container_img, container_cmd))
'''
#old
def run_container(image, comando):
    executando = client.containers.run(image, comando)
    print(executando)
'''

def run_container(args):
    try:
        executando = client.containers.run(args.image, args.comando)
        print(executando)
    except docker.errors.ImageNotFound as im:
        print('Essa image não existe não ou não é publica erro=> ', im)
    except docker.errors.APIError as co:
        print('Comando não encontrado =>', co)

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
        container_port = container.attrs['HostConfig']['PortBindings']
        if isinstance(container_port, dict):
            for port_container, port_host in container_port.items():
                port_host = str(port_host)
                port_host2 = ''.join(filter(str.isdigit, port_host))
                if int(port_host2) <= 1024:
                    print('Removendo container {}'.format(container.short_id))
                    remove = container.remove(force=True)
                else:
                    print('Demais contianer estão usando portas altas.')




subparser = parser.add_subparsers()

# Containers: Run container
cria_container = subparser.add_parser('containers')
cria_container.add_argument('--image', required=True, help='Informe o nome da image!')
cria_container.add_argument('--comando', required=True, help='Informe qual comando será executa detro no container.')
cria_container.set_defaults(func=run_container)

'''
# List: lista containers
lista = subparser.add_parser('list')
lista.add_argument('--list', help='Lista todos containers')
lista.set_defaults(func=list_container)
'''


# Realiza o tratamento dos arqumentos
cmd = parser.parse_args()
cmd.func(cmd)





'''
print('Run container\n')
run_container('nginx', 'ls -lha')
print('==='*10)
print()
print('Lista container\n')
list_container()
print('==='*10)
print('\nProcura image container\n')
procura('Ubuntu')
print('==='*10)
remove()
'''
