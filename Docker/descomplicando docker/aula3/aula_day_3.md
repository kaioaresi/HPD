# Dia 3
- Docker machine
- Docker swarm
  Trabalhando com cluster
    1. Iniciando cluster swarm
    ```
      docker swarm init
    ```
    Copie a saida e cole nos demais nodes para adiciona-los ao cluster
    2. Listando nodes
      ```
        docker node ls
      ```
    3. Recuperando tokens worker/manager
      ```
        docker swarm join-token worker/manager
      ```
    4. Saindo do cluster
      ```
        docker swarm leave # para worker
        docker swarm leave --force # para manager
      ```
      depois vá até o manager e remova o node/manager
      ```
        docker swarm node ls # pege o id
        docker swarm node rm <id>
      ```
    5. Promovendo worker para manager
      ```
        docker node promote <id>
      ```
    6. Trocando o token em todos nodes
      ```
        docker swarm ca --rotate
      ```
    7. Alterando tempo de resposta do heartbeat
      ```
        docker swarm update --dispatcher-heartbeat 2s
      ```
    8. Informações do docker e configurações
      ```
        docker info
      ```
    9. Eventos e logs cluster
      ```
        docker system events # para ver eventos correntes
        docker system events --since 20180606

      ```
    10. Armazenamento
      ```
        docker system df
      ```
    11. Limpeza docker
      ```
        docker system prune
      ```

- Services

> Service só funciona em swarm mode


1. Criando um servico com redundancia
```
  docker service create --name <nome do serviço> --replicas <numero de replicas> -p <porta do host>:<porta dos containers> <image>
  docker service create --name servidor_web --replicas 2 -p 8081:80 nginx
```
> global é garantido apenas um container por host
> replicas é criado uma quantidade de replicas por host

2. Listando services criados

```
  docker service ls
```
3. Verificando logs dos Services

```
  docker service lgos
```

4. Scalando servico

```
  docker service scale <nome do serviço>=<quantidade>
  docker service scale servidor_web=10 # para subir
  docker service scale servidor_web=2 # para descer
```

5. Verificando container rodando em um serviço

```
  docker service ps <nome do serviço>
  docker service ps servidor_web
```

6. Inspecionando serviço

```
  docker service inspect <nome do serviço>
```

7. Update de informações do serviço


O update é realizado porém o serviço continua up
```
  docker service update --publish-add 9091:80 <nome do serviço> # adiciona uma nova porta
  docker service update --publish-rm 9091:80 <nome do serviço> # remove uma porta
```

---

## Network
1. Criando um rede

```
  docker network create --driver overlay <nome da rede>
  docker network create --driver overlay aresi
```

1.1 Como usar a rede
```
  docker service create --name web -p 8080:80 --network aresi nginx
```





---

# Docker machine

## Instalando docker-machine

```
base=https://github.com/docker/machine/releases/download/v0.14.0 &&
  sudo curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine &&
  sudo install /tmp/docker-machine /usr/local/bin/docker-machine
```

1. Criando uma docker-machine

```
  docker-machine create --driver virtualbox <nome da machina>
  docker-machine create --driver virtualbox dockermachine01

```
> a logica de listagem, remoção é a mesma logica https://docs.docker.com/machine/reference/

2. Exportando váriaveis de ambiente para dentro do vm docker

```
  eval $(docker-machine env <nome da sua docker machine>)

```

3. Logando na docker machine

```
  docker-machine ssh <nome da machine>
```

4. Saindo da env docker machine

```
  unset eval
```


# Criando um arquivo Compose

1.



# Estudar aparte
  - servidor nfs sync de diretorios
