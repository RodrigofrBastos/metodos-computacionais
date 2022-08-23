import numpy as np

#gerar numeros randomicos

#gera randomicos inteiros
np.random.randint(30)
np.random.randint(10,50)

#gera uma amostra aleatoria a partir de um array 1D
np.random.choice([1,2,3,4,5])

# gera 3 amostras aleatorias a partir de um array 1D
np.random.choice([1,2,3,4,5], 3)


# gera um array aleatorio 2x4 com elementos aleatorios
a = np.random.choice(np.linspace(1,21,11), (2,4))
print(a)


# EXERCICIOS


