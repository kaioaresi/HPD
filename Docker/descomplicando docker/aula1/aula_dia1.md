#1º - Fazer a descrição da historia do docker e arquitetura.

#2º - Fazendo a instalação

```bash
  curl -fsSl https://get.docker.com | bash
```
# 3º - Primeiros comandos pós-instalação.

**Fazendo um hello-world no docker**
```docker
  docker container run hello-world
```
Alguns comandos básicos

1. Como subir um container

Aqui estamos ordenando ao docker que execute um container do debian 9 e quando ele terminar de baixar o debian e subir o `-ti` é para abrir um terminal dentro do container.

```docker
  docker container run -ti debian:9
```
Outra forma de subir um container porém não acessar o mesmo é atravez do `-d`.
> Dica: Para containers de serviço é o indicado, pois o processo principal é o daemon do serviço e não o bash.

```docker
  docker container run -d nginx
```

2. Como sair de um container e manter o mesmo rodando

```bash
  ctrl + p + q
```

3. Para lista os containers em execução
```docker
  docker container ls
```

4. Como voltar para dentro de um container

Para containers que possuem um bash
```docker
  docker container attach <id do container> # o container id vc consegue capturar com `container ls`
```
Para acessar container que estão rodando serviço que não possuem um bash rodando.

```docker
  docker container exec -ti <container id> bash  
```

5. Para listar todos containers que já foram executados.

```docker
  docker container ls -a
```

6. Parando/startando/resinstartando/pausando/unpause um container

```docker
  docker container stop <container id>
  docker container start <container id>
  docker container restart <container id>
  docker container pause <container id>
  docker container unpause <container id>
```

7. Visualizando status de um container

```docker
  docker container stats <container id>
```
8. Visualizando processo sendo executados dentro de um container

```docker
  docker container top <container id>
```

9. Visualizando logs

```docker
  docker container logs -f <container id>
```

10. Bindando a porta de container

No exemplo se você acessar o ip do host pelo navegador pela porta 8080, será direcionado para a porta 80 do container.

```docker
  docker container run -d -p <uma porta do seu host>:<porta do container> <serviço>

  docker container run -d -p 8080:80 nginx  
```

11. Removendo TODOS containers/imagens

```docker
  docker container prune # remove containers parados
  docker image prune # remove todas imagens com defeito
```

12. Criando um container

```docker
  docker container create <image>
  docker container create archlinux # o container é criado mas não é executado.
  docker container ls -a # para visualizar o container Criando
  docker container run -ti <nome container> # para subir o container  
```

13. Obtendo  mais informações de um container

```docker
  docker container inspect <container id>
```

14. Limitando recursos em um container

**Memory**
```docker
  docker container run -d -m/--memory 100M nginx  
```

**CPU**
```docker
  docker container run -ti --cpus 0.2 ubuntu
```


**Verificando as imagens no docker**
Agora vamos verificar as imagens

1. Para listar as imagens
```docker
  docker image ls
```
2. Para listar todas as imagens
```docker
  docker container ls -a
```

# Criando o Dockerfile

Um Dockerfile é apenas uma receita para criar uma image de containr

1. Todos Dockerfile deve ter seu nome do arquivo escrito EXTAMENTE desta maneira `Dockerfile`


2. Sintaxe de um Dockerfile

Dentro do arquivo Dockerfile

```docker
FROM centos:7
RUN yum install -y epel-release && yum install vim -y # executa um comando no momento do build da image
CMD echo "Hello, world" # permite executar um comando, porém ele será executado depois que a image subir como container
```

3. Como fazer um build de uma image

```docker
  docker build -t kaioaresi/ubunto_vim:1.0 .
```
















#
