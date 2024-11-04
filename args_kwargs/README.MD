## O que são *args e **kwargs em Python?

Você provavelmente já viu *args e **kwargs em algum código por aí, mas afinal, o que são eles? A primeira coisa a saber é que você não precisa usar exatamente esses nomes (*args e **kwargs); você poderia escrever *variavel e *variaveis, por exemplo. O que importa mesmo são os asteriscos ```*```.

Esses símbolos são usados na definição de funções para permitir que elas recebam uma quantidade variável de argumentos.

Vamos a um exemplo prático:

Imagine que você quer criar uma função de soma:

```python
def soma(a, b):
    return a + b

print(soma(1, 2))
# Out: 3
```

Agora, se precisar somar mais um número, você teria que mudar a função para:
```python
def soma(a, b, c):
    return a + b + c

print(soma(1, 2, 3))
# Out: 6
```

Mas e se você quiser somar apenas dois números de novo? Ou, em outro momento, somar mais de três? Teria que continuar ajustando a função cada vez? Não, é aí que entra o *args.

Com *args, você permite que a função aceite qualquer quantidade de números:

```python
def soma(*a):
    resultado = 0
    for i in args:
        resultado += i
    return resultado

print(soma(2, 4)) # Out: 6
print(soma(4, 2, 1, 3)) # Out: 10
```

Com essa versão, você pode passar quantos números quiser para a função. Repare escrevemos *a em vez de *args, mas mesmo assim o código funciona. Porém, é uma convenção escrever como *args, além de facilitar o seu entendimento.

Agora, vamos falar sobre **kwargs.

**kwargs permite passar argumentos nomeados, ou seja, pares de chave=valor (por exemplo, nome="Carlos", idade=40). Esses argumentos são passados para a função como um dicionário.

Veja um exemplo:
```python
def pessoa(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave} - {valor}")

pessoa(nome="Carlos", idade=40)
# Out: nome - Carlos
# Out: idade - 40
```

Aqui, **kwargs coleta os argumentos nomeados e permite que você os manipule dentro da função.

Também é possível desempacotar (unzip) dicionários diretamente na função com **kwargs:
```python
def pessoa(**kwargs):
    print(kwargs)

d = {'nome': 'Carlos', 'idade': 44}
pessoa(**d)
# Out: {'nome': 'Carlos', 'idade': 44}
```

Em vez de escrever:
```python
def pessoa(nome, idade):
    print(nome, idade)

pessoa("Carlos", 40)
# Out: Carlos, 40
```
Podemos simplesmente desempacotar o dicionário, como no exemplo acima, e obter o mesmo resultado.