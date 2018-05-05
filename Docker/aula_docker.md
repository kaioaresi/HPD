# Instalando o docker
---
**Passo 1**

```bash
    curl -fSsl https://get.docker.com | sh
```

> systemctl start docker

**Passo 2**
```docker
  # para listar containers rodando
  docker container ls

  # hellor world do docker
  docker container run -ti hello-world

```

1. run = rodar um container
2. t = criar um terminal
3. i = te jogar pra dentro do container
4. d = para apenas executar o container como daemon

**Passo 3**

Saindo de um container

Esse modo você sai do container encerrando o container
```
  ctrl + d
#  ou
  exit
```
Saindo de um container sem encerrar o container.
```
  ctrl + p + q
```

Como voltar para dentro de um container

```docker
  dcoker container ls # capture o container ID
  docker attach <container ID>
```

Listar container que já morreram

```docker
  docker container ls -a
```

Subir container mortos

```docker
  docker container ls -a # capture o id do container
  docker container start <container ID>
```


Parando a execução de um container

```docker
  docker container ls # capture o id do container
  docker container stop <id container>
```

Apagando container

```docker
  docker container ls -a # capture o id do container
  docker container rm <container ID>
```

# Subindo um processo Nginx

```docker
  docker container run -d nginx

# d = para apenas executar o container como daemon
```

**Acessando um container do Nginx**

```docker
  docker container run -d nginx -p 80:80
```
**Verificando logs ngixn**

```docker
  docker container logs -f <container id>
```

**Definindo uma nome para o container**

```docker
  docker container run -d -p 8080:80 --name nginxteste nginx
```

```docker
  docker container run -d -p 8080:80 --name ngixn123 --hostname node-1 --dns 8.8.8.8 nginx
```

# Removendo containers não utilizados/parados

O prune remove tudo que está parado
```docker
  docker container prune
```

O prune no image remove tudo que está quebrado ou com problema
```docker
  docker image prune
```

#### Como acessar um bash em um processo

```docker
#  docker container exec -ti <container id> <comando>
  dcoker container exec -ti <container id> bash # para acessar o processo via bash
  docker container exec -ti <container id> ifconfig # para exibir a saida do ifconfig
  docker container exec -ti <container id> curl localhost # para exibir uma saida do localhost
```

# Trabalhando com imagens

```docker
  docker image ls # lista das imagens
```

**Fazendo apenas o download da imagem**

```docker
  docker pull debian
  docker pull centos:7 # vai realizar o donwload do centos 7
```

**Deletando imagem**

```docker
  docker image rm <image id>
```

# Criando volumes com docker


```docker
  docker volume create <nome do volume>
```

Para saber onde foi criado o volume

```docker
  docker volume inspect <nome do volume>
```

Agora vamos criar uma index.html dentro deste vomule para replica-lo dps dos containers

```docker
  docker container run -d --mount type=volume,src=volume-1,dst=/usr/share/nginx/html -p 8080:80 --name nginx-1 nginx
```

Agora vamos bindar um diretorio

```docker
  docker container run -d --mount type=bind,src=/root/bind_teste,dst=/usr/share/nginx/html -p 8082:80 --name nginx-2 nginx
```


# Criando uma imagem






























#
