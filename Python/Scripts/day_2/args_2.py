#!/usr/bin/env python3

import argparse
import subprocess

def criar(args):
    global dir
    dir = args.nomedir
    subprocess.call(['mkdir', dir])
    for arq in range(1,40):
        subprocess.call(['touch',str(arq)+'.txt'], cwd=dir)
    return list_dir(dir)

def list_dir(args):
    list_dir = args.listar
    subprocess.call(['ls','-lht', list_dir])

parser = argparse.ArgumentParser(description='Comando que cria e lista diretorio..')

subparser = parser.add_subparsers()

criar_dir = subparser.add_parser('criar')
criar_dir.add_argument('--nomedir', required=True)
criar_dir.set_defaults(func=criar)


listar_dir = subparser.add_parser('list')
listar_dir.add_argument('--listar', required=True)
listar_dir.set_defaults(func=list_dir)

cmd = parser.parse_args()
cmd.func(cmd)
