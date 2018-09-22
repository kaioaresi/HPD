# Trabalhando arquivos

```
  # informando o path do arquivo
  arq = '/home/kaio/HPD_exec/HPD/Python/Scripts/day_3/frutas.txt'

  # Lendo o arquivo
  list_frutas = open(arq,'r')
  list_frutas.read()
  list_frutas.readline() # mostra linha por linha
  list_frutas.readlines() # mostra em forma de lista

  # Criando um novo arquivo
  novo = '/home/kaio/HPD_exec/HPD/Python/Scripts/day_3/novo_file_python.txt'
  nova_list = open(novo, 'w')
  mensagem = "Uma mensagem qualquer"
  nova_list.write(mensagem)


  # Editando o arquivo
  list_frutas = open(arq,'w')

  # Escrever e ler o arquivo
  list_frutas = open(arq,'rw')

  # Fechando o arquivo, se abrir o arquivo tem que fechar
  list_frutas.close()
```

# Level 2

```
  # Abrindo um arquivo e não se preocupar em fechar
  arq = '/home/kaio/HPD_exec/HPD/Python/Scripts/day_3/frutas.txt'
  with open(arq, 'r') as lista_frutas:
    lista2 = lista_frutas.read()

  # check se o arquivo foi Fechando
  lista_frutas.closed  
```

# Escrevendo logs

```
from datetime import datetime

def logando(mensage, e, logfile="docker_cli.log"):
  data_atual = datetime.now().strftime('%d/%m/%Y %H:%M')
  # append do arquivo
  with open(docker_cli.log,'a') as log:
    texto = "%s \t %s \t %s \n" % (data_atual, mensagem, str(e))
    log.write(texto)
```

---


# Trabalhando com reguests - topizera
> http://docs.python-requests.org/en/master/

```
  pip install requests
```

```
import requests

# Informando parametros
parametros = {"lat": -18.9146, "lon": -48.2754}

# pegando um informação
response = requests.get('http://api.open-notify.org/iss-pass.json', params=parametros)

response.status_code
response.text
response.json()

```

## Exemplo 2 - GET

```
import requests

url = "http://maps.googleapis.com/maps/api/geocode/json"
local = "Uberlandia"
parametros = {'address':local}

consulta = requests.get(url, params=parametros)
udi = consulta.json()
```

# Exemplo 3 - Post

> https://pastebin.com/api

```
import requests


api_endpoint = "https://pastebin.com/api/api_post.php"
api_key = "70b3e4a56605a5374abd6f3421457d7c"

source_code = "Teste mensagem"

dados = {"api_dev_key": api_key, 'api_option':'paste','api_paste_code':source_code, 'api_paste_format':'python'}

request = requests.post(url=api_endpoint, data=dados)

```



# Convertendo timestamp

```
import time

time.strftime('%H:%M:%S %d:%m:%Y', time.localtime(1537645041))
```


## Exercicio 1

Saida: Neste momento temos x pessoas no espaço são eles : X,y,z,w


```
import requests

url = "http://api.open-notify.org/astros.json"

lista_nomes = []

resposta = requests.get(url)

saida_completa = resposta.json()

# Armazenou a saída completa
saida_completa

# Número de pessoas
n_pessoas = saida_completa['number']

# Nomes das pessoas
lista_pessoas = saida_completa['people']

```

























#
