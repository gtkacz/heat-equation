import numpy as np
import matplotlib.pyplot as plt

# Difusividade [m²/s]
alpha = 0.0001

# Intervalo espacial [m]
dx = 0.05

# Intervalo temporal [s]
dt = 5.

# Comprimento [m]
comp = 0.5

# Número de intervalos na malha espacial
nint = comp/dx+1
nint = int(nint)

# Número de intervalos na malha temporal
ntemp = 100

# Temperatura [C] na condição inicial
T = np.zeros((ntemp,nint))
T[0,1:10] = 20

# Armazenar os erros
erros = np.zeros((ntemp,1))

# Calcular todas as temperaturas em todos os instantes
for l in range(1,ntemp):
    # Calcular todas as temperaturas no instante 1
    for i in range(1,nint-1):
        T[l,i] = (alpha*dt/dx**2)*(T[l-1,i+1] + T[l-1,i-1]- 2*T[l-1,i]) + T[l-1,i]

    # Cálculo do erro
    erros[l,0] = max(abs((T[l,1:-1] - T[l-1,1:-1]) / T[l,1:-1]))
    
# Posições [m]
x = np.linspace(0,.5,nint)

# Gráfico
plt.plot(x,T[99,:])
plt.xlabel('Posição [m]')
plt.ylabel('Temperatura [C]')

# Imprimir o erro na iteração 5
print(erros[5,0])
