#!/usr/bin/env python3



def inss(salario):

    if salario <= 1693.72:
        desc_inss = salario * 0.08
    elif salario >= 1693.73 and salario <= 2822.90:
        desc_inss = salario * 0.09
    else:
        desc_inss = salario * 0.11
    return desc_inss


def dados():

    salario = float(input('Digite o valor bruto do seu salário: '))
    vt = input('Você utiliza vale-transporte ? (y/n) ')
    outros = input('Você possuem mais algun gasto extra ? (y/n) ')

    if vt == 'y':
        vt_total = salario * 0.06

    if outros == 'y':
        valor_outros = float(input('Qual é esse valor? '))

    desc_inss = inss(salario)
    if valor_outros is None:
        print('==='*10)
        print('Dados\nsalario: {}\ndesconto no inss {}\nvale transporte {}\n'.format(salario, desc_inss, vt_total))
        print('==='*10)
    else:
        print('==='*10)
        print('Dados\nsalario: {}\ndesconto no inss {}\nvale transporte {}\noutros {}\n'.format(salario, desc_inss, vt_total, valor_outros))
        print('==='*10)



dados()
