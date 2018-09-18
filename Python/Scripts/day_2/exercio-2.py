#!/usr/bin/env python3
import subprocess
import argparse

def nomedir(args):
    diretorio = args.nomedir
    subprocess.call(['mkdir', args.nomedir])
    for i in range(1,40):
        subprocess.call(['touch', str(i)+".txt"], cwd=args.nomedir)
    return diretorio

def list_dir():
    subprocess.call('ls -lh', cwd=dir, shell=True)

parser = argparse.ArgumentParser(description="Comando para criar e listar diretorios.")

# criando várias opção e passando arqumentos
subparsers = parser.add_subparsers()

# Exemplo part 1: <scripts>.py diretorios <comando>
criar_dir = subparsers.add_parser('diretorios')

# Exemplo part 2: <scripts>.py diretorios --criar <nome dir>
criar_dir.add_argument("--criar", required=True, help='Cria um novo diretorio')

# Função que será executando quando a opção criar for executada
criar_dir.set_defaults(func=nomedir)

cmd = parser.parse_args()

cmd.func(cmd)
