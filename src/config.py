import typing as tp
import numpy as np

# cidades a serem visitadas
CIDADES: tp.Final[int] = 100

# constantes do ACO
A: tp.Final[float] = 0.5
B: tp.Final[float] = 0.5
R: tp.Final[float] = 0.5
Q: tp.Final[float] = 1.0

cidades = np.arange(CIDADES)
inicio = np.copy(cidades)
tours = np.empty((CIDADES, CIDADES+1))
custos = np.zeros(CIDADES)
melhor_agente = -1
distancia_cidades = np.array((CIDADES, CIDADES))
feromonios = np.empty((CIDADES, CIDADES))
qtde_feromonio = np.zeros(CIDADES)