#!/usr/bin/env python3

import subprocess


def nome_dir():
    global dir
    dir = input('Digite o nome do diretorio: ')

def mk_dir():
    nome_dir()
    subprocess.call(['mkdir', dir])
    for i in range(1,40):
        subprocess.call(['touch', str(i)], cwd=dir)

def list_dir():
    subprocess.call('ls -lh', cwd=dir, shell=True)

mk_dir()
list_dir()
