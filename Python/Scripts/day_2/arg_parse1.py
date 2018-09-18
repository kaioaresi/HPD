#!/usr/bin/env python3

import argparse

#> https://docs.python.org/3/library/argparse.html

# instanciando objeto e abrindo bloco
parser = argparse.ArgumentParser()

# Não aceita passar valor
parser.add_argument("teste1", help="Teste de um argumento", type=int)

# Aceita passar valor
parser.add_argument("--teste2", help="Teste de um argumento")

# fechando o bloco
args = parser.parse_args()

print(args.teste1)
print(args.teste2)
