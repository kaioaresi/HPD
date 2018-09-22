#!/usr/bin/env python3
import requests

'''
Realizar um get em uma api para capturar a quantidade de pessoas no espaço e o nome dos astronautas
Saida: Neste momento temos x pessoas no espaço são eles : X,y,z,w
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

    print('Neste momento temos {} pessoas no espaço são eles : {}'.format(n_pessoas,lista_nomes))


nome_astronautas()
