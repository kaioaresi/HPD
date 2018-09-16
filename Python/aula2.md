# Arg. parser

Possibilita a criação de helps, para o nossos scripts em python.

```
#!/usr/bin/env python3

import argparse

# instanciando o objeto
parser = argparse.ArgumentParser()

parser.parse_args()
```

```
#!/usr/bin/env python3

import argparse

#> https://docs.python.org/3/library/argparse.html
#> https://docker-py.readthedocs.io/en/stable/
#> https://docs.python.org/3/library/argparse.html

# instanciando objeto e abrindo bloco
parser = argparse.ArgumentParser()

# Não aceita passar valor
parser.add_argument("teste1", help="Teste de um argumento", type=int)

# fechando o bloco
args = parser.parse_args()

print(args.teste1)

```

# Unindo dois mundos Docker e Python
Pré-requisito

```
  pip3 install docker
```

Executando alguns comandos

```
import docker

# forma de conectar no socket do docker
client = docker.from_env()

client.contianer.run("hello-world")
client.contianer.run("ubuntu", "uname -a")

client.container.list(all)


container1 = client.containers.get(<id container>)


container.attrs
container.attrs['Config']['Cmd']
container1.attrs['NetworkSettings']['IPAddress']


client.containers.run('nginx', detach=True)

```


# Teste 1

```
import docker

client = docker.from_env()

ids_containers = client.containers.list(all)

for containers in ids_containers:
  container_nomes = containers.attrs['Name']
  print('O nome deste container é {}'.format(container_nomes))


```
