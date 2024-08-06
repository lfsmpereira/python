def add(a, b):
    """Soma dois números."""
    return a + b

def subtract(a, b):
    """Subtrai o segundo número do primeiro."""
    return a - b

def multiply(a, b):
    """Multiplica dois números."""
    return a * b

def divide(a, b):
    """Divide o primeiro número pelo segundo. Retorna None se o segundo número for zero."""
    if b == 0:
        return None
    return a / b

def modulus(a, b):
    """Calcula o resto da divisão do primeiro número pelo segundo."""
    if b == 0:
        return None
    return a % b

def exponentiate(a, b):
    """Calcula a exponenciação do primeiro número elevado ao segundo."""
    return a ** b

def integer_divide(a, b):
    """Divide o primeiro número pelo segundo e retorna o resultado inteiro da divisão."""
    if b == 0:
        return None
    return a // b

# Exemplos de uso das funções
if __name__ == "__main__":
    x = 10
    y = 3

    print(f"Addition: {x} + {y} = {add(x, y)}")
    print(f"Subtraction: {x} - {y} = {subtract(x, y)}")
    print(f"Multiplication: {x} * {y} = {multiply(x, y)}")
    print(f"Division: {x} / {y} = {divide(x, y)}")
    print(f"Modulus: {x} % {y} = {modulus(x, y)}")
    print(f"Exponentiation: {x} ** {y} = {exponentiate(x, y)}")
    print(f"Integer division: {x} // {y} = {integer_divide(x, y)}")
