def soma(a, b):
    return a + b

print(f"Exemplo 1: {soma(1, 2)}")

def soma(a, b, c):
    return a + b + c

print(f"Exemplo 2: {soma(1, 2, 3)}")

def soma(*a):
    resultado = 0
    for i in a:
        resultado += i
    return resultado

print(f"Exemplo 3: {soma(2, 4)}")
print(f"Exemplo 3: {soma(4, 2, 1, 3)}")

def pessoa(**kwargs):
    for chave, valor in kwargs.items():
        print(f"Exemplo 4: {chave} - {valor}")

pessoa(nome="Carlos", idade=40)

def pessoa(**kwargs):
    print(f"Exemplo 5: {kwargs}")

d = {'nome': 'Carlos', 'idade': 44}
pessoa(**d)

def pessoa(nome, idade):
    print(f"Exemplo 6: {nome}, {idade}")

pessoa("Carlos", 40)