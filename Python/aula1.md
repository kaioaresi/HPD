# Python primeiros passos

### Operações aritimeticas

> Dentro do `python3`

```
	2 + 2 # soma
	2 * 2 # multiplicação
	2 / 2 # divisão
	2 - 2 # subtração
	2 (2 + 2) # ordem de execução
	2 % 2 # resto
	2.2 * 2 # operação entre float e int
```
No python existem apenas numeros `int` e `float`

### Print

```
	print('Linuxtips, VAI!!!!')
```

### Operadores de comparação
> Saída booleando

```
	2 > 5
	2 < 5
	2 >= 5
	2 <= 5
	2 == 5
	2 != 5
```

### variaveis

```
	nome = 'Kaio Cesar'
	print(nome)

# ou
	print('Seu nome é {}'.format(nome))

```

### Listas

```
	mario = ["Mario", "Luigi", "Princesa", "Copa", "Yoshi"]

# Mostra toda a lista tudo
	print(mario)

# Apenas um item na posição
	print(mario[0])

# A ultima possição
	print(mario[-1])

# Mostrando um intervalo o `ultimo não é mostrado`
	print(mario[1:3])

# Mostrando de um ponto até o final ou visa e versa
	print(mario[2:])
	print(mario[:-1])
	print(mario[:]) # full lista

# Clonando um lista direto
> Observação: isse tipo apenas referencia duas variaveis ao mesmo valor, ou seja se um valor de qualquer umas das lista for alterado ambas variaveis tera o valor alterado.
	supermario = mario

# Clonagem com referencia separada
	supermario = mario[:]

# Add itens a lista

	supermario.append("Wario")

# Index da lista

	print(supermario.index("Copa"))		
```

# Add em uma posição definida

```python3
	supermario.insert(1, "Peach")
```

# Removendo item

```python3
	supermario.remove("Mario")
	supermario.pop(1)
	del(supermario[0])
```

# Orgenando

```python3
	supermario.sort() # só ordena
	print(supermario) # print ordenado

# outra forma de ordenar

	sorted(supermario) # ordena e imprime
```

# Percorendo um lista

```
	for nome in supermario:
		print('O nome do personagem é {}'.format(nome))

#
	for nome in supermario:
		print("O nome é %s" % nome)
```

# Condicionais

```
	if 1 > 2:
		print('2 é maior')
	else:
		print('1 é menor')
```

# Tuplas

Tuplas são imutaveis

```
	mario = ("Mario", "Luigi", "Princesa", "Copa", "Yoshi")
```

# Dicionario

```
	cadastro = {"Nome":"Mario", "Idade":150, "Estado":"MG"}
	print(cadastro['Nome']
	print(cadastro.keys()) # todas as keys
	print(cadastro.values()) # todos valores

	for valor in cadastro.values():
		print(valor)

	for chaves in cadastro.keys():
		print(chaves)

# remover um valor
	del(cadastro["MG"])
	cadastro.popitem()

# Tamanho
	len(cadastro)

# in e not
	kaio in cadastro
	kaio not cadastro

# Add novos itens
	cadastro={"Cidade":"Uberlandia"}
	cadastro.update(cadastro) # mesclando dois dicionarios
```

---

# Criando funções


```
	def print_nomes ():
		nomes = ["Kaio", "Cesar", "Fernanda", "Balene"]
		for nome in nomes:
			print('O nome é {}'.format(nome))

# Exemplos
	def nome():
		nome = str(input('Digite um nome: '))
		# colocando todos nomes em upper case
		if set('aeio').intersection(nome.upper()):
			print('Seu nome é {}'.format(nome))
		else:
			print('Mensagem qualquer!')


```

---

# Criando scripts

Para execução dos mesmo via terminal sem passar a referencia do path do python fora.
```
	#!/usr/bin/env python3
	chmod +x <script>
```

---

# Import Subprocess

```
# Server para executar um comando no linux
import subprocess

# Mostra todas funções
dir(subprocess)

# execurado um comando

subprocess.call(['df', '-h']) # modo hardcore passando lista

subprocess.call('df -h', shell=True) # mode easy

```

# Exercicio

1. Criar uma função que cria um diretorio e dentro dele arquivos 1-39
2. Listar os arquivos dentro de um diretorio

```
#!/usr/bin/env python3

import subprocess

def cria_dir():
    global dir
    dir = input('Digite o nome do diretorio: ')
    subprocess.call(['mkdir', dir])
    for i in range(1,40):
        subprocess.call(['touch', str(i)], cwd=dir)

def list_dir():
    subprocess.call(['ls', dir])

cria_dir()
list_dir()
```

#### Entendimento

```
	subprocess.call('ls -lh', cwd=dir, shell=True)
```

Quando é executado o `subprocess` e o metodo `call` é executado você pode passar um comando, e depois um onde será `cwd` executado o comando e o `shell` para aceitar passar o comando sem `[]`


#



## Resulmo parte 1
'''
# Foi apresentado a sintaxe básica do python 3.x

- Declaração de variaveis;
- Saídas (%s)
- Tipos de dados (String, int, float)
- Operadores logicos e matematicos;
- Estruturas de repetição (while e for);
- Listas
	- criando
		- append
		- atribuição direta
		- insert
		-
	- exibindo
	- buscas
		- index
	- Deletando
		- remove
		- pop()
		- del()
	- Ordenar
		- sorted()
		- sort()
- Dicionarios
	- update
- Tuplas
- Criando funções

### Parei 1:38:31
'''
