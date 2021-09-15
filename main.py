import matplotlib.pyplot as plt, seaborn as sns, numpy as np, locale
from math import sin, pi as 𝜋, e

def main():
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    α = 0.0001
    αΔtΔx2 = 0.2
    ny = 500
    nx = 11
    t = 0.5
    sol_an = []
    
    #p = np.arange(0, t, t/ny)
    p = np.arange(0, t, t/nx)
    
    T = np.zeros(shape=(ny, nx))
    T[0][1:-1] = 20
    
    for l in range(0, ny-1, 1):
        for i in range(1, nx-1):
            T[l+1][i] = T[l][i] + (αΔtΔx2) * (T[l][i+1] - 2*T[l][i] + T[l][i-1])
            
    for x in T[-1]:
        na = 0
        for n in range(1, 5):
            na += (1/n * e**((-n**2 * 𝜋**2 * α * ny)/2500) * sin((n*𝜋*x)/50))
        na *= 80/𝜋
        sol_an.append(na)

    sns.set()
    sns.set_style("white")
    
    plt.plot(p, T[-1], label="Método das diferenças finitas")
    plt.plot(p, sol_an, label="Solução analítica")
    #plt.plot(p, T)
    plt.grid()
    #plt.autoscale(axis='y', tight=True)
    plt.legend()
    plt.ylabel("Temperatura (°C)")
    plt.xlabel("Posição (cm)")
    plt.show()
    
if __name__ == '__main__':
    main()