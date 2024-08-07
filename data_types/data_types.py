# Função para manipular números inteiros
def soma_inteiros(a: int, b: int) -> int:
    return a + b

# Função para manipular números de ponto flutuante
def calcular_media(valores: list[float]) -> float:
    return sum(valores) / len(valores)

# Função para manipular strings
def saudacao(nome: str) -> str:
    return f"Olá, {nome}! Bem-vindo!"

# Função para manipular listas
def adicionar_elemento(lista: list, elemento) -> list:
    lista.append(elemento)
    return lista

# Função para manipular dicionários
def adicionar_entrada(dicionario: dict, chave, valor) -> dict:
    dicionario[chave] = valor
    return dicionario

# Função para manipular tuplas
def acessar_elemento(tupla: tuple, indice: int):
    return tupla[indice]

# Função para manipular conjuntos (sets)
def unir_conjuntos(conjunto1: set, conjunto2: set) -> set:
    return conjunto1.union(conjunto2)

# Função para manipular valores booleanos
def verificar_paridade(numero: int) -> bool:
    return numero % 2 == 0

# Cria um range de 0 a 9
def basic_range_example():
    r = range(10)
    print("Basic range example (0-9):", list(r))

# Cria um range de 5 a 14
def range_with_start_and_end():
    r = range(5, 15)
    print("Range with start and end (5-14):", list(r))

# Cria um range de 0 a 20, pulando de 2 em 2
def range_with_step():
    r = range(0, 21, 2)
    print("Range with step (0-20, step 2):", list(r))

# Cria um range de 10 a 1, decrementando de 1 em 1
def range_with_negative_step():
    r = range(10, 0, -1)
    print("Range with negative step (10-1):", list(r))

# Soma todos os números de 0 a n-1
def sum_of_range(n):
    r = range(n)
    return sum(r)

# Filtra os números pares em um range
def even_numbers_in_range(start, end):
    r = range(start, end)
    evens = [num for num in r if num % 2 == 0]
    return evens

# Usa range para acessar índices de uma lista
def range_as_index():
    fruits = ["apple", "banana", "cherry", "date"]
    for i in range(len(fruits)):
        print(f"Fruit at index {i}: {fruits[i]}")

# Exemplos de uso das funções

# Inteiros
resultado_soma = soma_inteiros(10, 5)
print(f"Soma de inteiros: {resultado_soma}")

# Pontos flutuantes
valores = [10.5, 20.3, 30.7]
media = calcular_media(valores)
print(f"Média dos valores: {media}")

# Strings
mensagem = saudacao("Enzo")
print(mensagem)

# Listas
lista = [1, 2, 3]
nova_lista = adicionar_elemento(lista, 4)
print(f"Lista após adicionar elemento: {nova_lista}")

# Dicionários
dicionario = {"nome": "Alice", "idade": 30}
novo_dicionario = adicionar_entrada(dicionario, "cidade", "São Paulo")
print(f"Dicionário após adicionar entrada: {novo_dicionario}")

# Tuplas
tupla = (10, 20, 30)
elemento = acessar_elemento(tupla, 1)
print(f"Elemento da tupla no índice 1: {elemento}")

# Conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = unir_conjuntos(conjunto1, conjunto2)
print(f"União dos conjuntos: {uniao}")

# Booleanos
paridade = verificar_paridade(10)
print(f"O número 10 é par? {paridade}")

# Range
basic_range_example()
range_with_start_and_end()
range_with_step()
range_with_negative_step()

n = 10
print(f"Sum of range 0 to {n-1}:", sum_of_range(n))

start, end = 1, 20
print(f"Even numbers in range {start} to {end-1}:", even_numbers_in_range(start, end))

range_as_index()
