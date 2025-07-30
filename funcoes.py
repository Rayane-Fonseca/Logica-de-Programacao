# Função Posicional

def funcao_posicional(a, b, c):
    print(c, b, a)

funcao_posicional(1, 2, 3)

# Função Nomeada

def funcao_nomeada(a, b, c):
    print(a, b, c)

funcao_nomeada(b=10, c=20, a=5)

# Função Padrão

def funcao_padrao(a, b=100, c=200):
    print(a, b, c)

funcao_padrao(1)
funcao_padrao(1, 2)
funcao_padrao(1, 2, 3)