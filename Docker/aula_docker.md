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


**Criando um dockerfile**
```docker
  mkdir dockerfiles
  vim Dockerfile # o nome deve ser desta maneira

      FROM ubuntu # qual imagem será utilizada
      MAINTAINER KAIO ARESI # quem criou a imagem
      RUN apt-get update ; apt-get install -y ngin ; apt-get clean # quais comandos serão executados no momento da criação da imagem
      COPY index.html /var/www/html/ # irá copiar o index.html do diretorio local para dentro do container
      ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]
      EXPOSE 80 # para disponibilizar a porta
```

Agora vamos criar o index.html
```html
  <h1>Meu primeiro Dockerfile</h1>
```

Agora vamos criar a imagem
```docker
  docker build -t <tag> <diretorio do Dockerfile>
  docker build -t ubunto_nginx:1.0 .
```

**Treino Dockerfile**

```docker
    FROM centos:7
    MAINTAINER KAIO ARESI (kaioaresi@gmail.com)
    RUN yum install -y epel-release ; yum install -y nginx ; yum clean all
    COPY index2.html /var/www/html/
    ENTRYPOINT ['/usr/sbin/nginx', '-g', 'daemon off;']
    EXPOSE 80
```


**Docker login**

```docker
  docker login
```

Para subir uma image para o dockerhub, você deve primeiro colocar o nome da image no formato correto.

**1º passo**
Renomeando uma image para o padrão dockerhub
```docker
  docker tag <image id> <nome usuário>/<nome img>:<versão>
  docker tag 5a54b0b48c76 kaioaresi/ubuntu_nginx_k:1.0
```

**2º passo**
Subindo uma imagem para o dockerhub
```docker
  docker push kaioaresi/ubuntu_nginx_k:1.0
```

#### Criando um Dockerfile multi stage

**1º passo**


```docker

  FROM golang:alpine
  WORKDIR /app # quando o container subir qual diretorio ele irá trabalhar
  ADD ./app
  RUN go build -o opa
  ENTRYPOINT ./opa
```

Agora crie um arquivo em GO no mesmo diretorio
```go
  package main

  import "fmt"

  func main()  {
    fmt.Println("Teste app docker")
  }
```


#### Agora o multi

```docker
FROM golang:alpine AS buildando
ADD . /src
WORKDIR /src
RUN go build -o opa

FROM alpine
WORKDIR /app
COPY --from=buildando /src/opa /app
ENTRYPOINT ./opa

```
#### Historico das imagens

```docker
  docker image history <image id>
```



#### Limitando consumo de um container

Para limitar a quantidade máxima de recursos que um container pode consumir.

```docker
  docker container run -d -p 8080:80 --memory 128M kaioaresi/centos_nginx_k:1.0
```


```docker
  docker container run -d -p 8081:80 --cpus 0.2 kaioaresi/centos_nginx_k:1.0
```

Como verificar a utilização de recursos do containers

```docker
  docker container stats <container id>
```




















#
