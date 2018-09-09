#!/usr/bin/env python3

def pause():
    input('\n\nPressione enter para continuar...\n\n')

def mensagemFim():
    print('Valeu por usar esse programa!')

def imprimaTresLinhas():
    for i in range(1,4):
        print('Esta é a linha {}.'.format(i))

def imprimaNovelLinhas():
    for i in range(1,4,):
        imprimaTresLinhas()

def mensagemInicio():
    print('Este programa é somente para mostrar como funciona o uso de funcstions.')
    pause()

def linhaBranco():
    print()

def limpaTela():
    for i in range(1,26):
        linhaBranco()

mensagemInicio()
limpaTela()
