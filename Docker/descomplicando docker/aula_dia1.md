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

3.
