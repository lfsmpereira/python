##Data Types
In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:

###Text Type: str
###Numeric Types: int, float, complex
###Sequence Types: list, tuple, range
###Mapping Type: dict
###Set Types: set, frozenset
###Boolean Type: bool
###Binary Types: bytes, bytearray, memoryview
###None Type: NoneType

###frozenset:

frozenset é uma coleção imutável de elementos únicos, semelhante ao set, mas que não pode ser alterada após a sua criação.
Exemplos de operações com frozenset: união (|) e interseção (&).

###bytes:

bytes é uma sequência imutável de números inteiros no intervalo de 0 a 255.
Você pode criar um objeto bytes a partir de uma lista de inteiros e também converter de volta para uma string usando decode.

###bytearray:

bytearray é semelhante a bytes, mas mutável.
Pode ser modificado após a criação, e pode ser convertido para string usando decode.

###memoryview:

memoryview permite o acesso a memória de um objeto sem fazer uma cópia.
Útil para trabalhar com grandes volumes de dados, permitindo a modificação direta da memória subjacente de objetos como bytearray.