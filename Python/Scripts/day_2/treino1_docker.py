#!/usr/bin/env python3

import docker

client = docker.from_env()

ids_containers = client.containers.list(all)

for containers in ids_containers:
  container_nomes = containers.attrs['Name']
  print('O nome deste container é {}'.format(container_nomes))
