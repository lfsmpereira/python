# Variável global
global_var = "Eu sou uma variável global"

def demonstrate_local_variable():
    # Variável local
    local_var = "Eu sou uma variável local"
    print(local_var)

def demonstrate_global_variable():
    global global_var
    print(global_var)

def function_with_arguments(arg1, arg2):
    # Usando argumentos da função
    result = arg1 + arg2
    return result

def function_with_static_variable():
    if not hasattr(function_with_static_variable, "counter"):
        # Variável estática inicializada apenas uma vez
        function_with_static_variable.counter = 0
    function_with_static_variable.counter += 1
    return function_with_static_variable.counter

# Função principal para demonstrar o uso das variáveis
def main():
    print("### Demonstração de Variáveis Locais ###")
    demonstrate_local_variable()
    
    print("\n### Demonstração de Variáveis Globais ###")
    demonstrate_global_variable()
    
    print("\n### Função com Argumentos ###")
    resultado = function_with_arguments(5, 7)
    print(f"Resultado da soma: {resultado}")
    
    print("\n### Função com Variável Estática ###")
    print(f"Chamada 1: Contador = {function_with_static_variable()}")
    print(f"Chamada 2: Contador = {function_with_static_variable()}")
    print(f"Chamada 3: Contador = {function_with_static_variable()}")

if __name__ == "__main__":
    main()
