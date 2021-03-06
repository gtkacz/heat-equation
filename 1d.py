import matplotlib.pyplot as plt, seaborn as sns, numpy as np, locale
from math import sin, pi as 𝜋, e
import sys

def main():
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    sns.set()
    sns.set_style("white")
    
    α = 0.0001
    αΔtΔx2 = 0.2
    Δt = 5
    Δx = 0.05
    ny = 100
    nx = 11
    le = 0.5
    sol_an = []
    
    p = np.arange(0, le+Δx, Δx)
    
    T = np.zeros(shape=(ny, nx))
    T[0][1:-1] = 20
    
    for l in range(1, ny):
        for i in range(1, nx-1):
            T[l][i] = T[l-1][i] + ((αΔtΔx2) * (T[l-1][i+1] - 2*T[l-1][i] + T[l-1][i-1]))
            
    α *= 100
    for x in p: #solução analítica
        na = 0
        for n in range(1, 6):
            na += (1/n * e**(-((n**2) * (𝜋**2) * α * (ny*Δt))/2500) * sin((n*𝜋*x)/50))
        na *= 80/𝜋
        sol_an.append(na)
    
    plt.scatter(p, T[-1])
    plt.plot(p, T[-1], label="Método das diferenças finitas")
    plt.scatter(p, sol_an)
    plt.plot(p, sol_an, label="Solução analítica")
    plt.grid()
    #plt.autoscale(axis='x', tight=True)
    plt.legend()
    plt.ylabel("Temperatura (°C)")
    plt.xlabel("Posição (m)")
    plt.show()
    #plt.savefig("teste")
    
if __name__ == '__main__':
    main()