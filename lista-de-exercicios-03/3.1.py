# Crie um array  5x3 com elementos inteiros iguais a 1. E um array 3x5
# ? Quantos elementos possuem os dois arrays?

import numpy as np

a = np.ones((5,3), dtype=int)
print(a.size)

b = np.ones((3,5), dtype=int)
print(b.size)



