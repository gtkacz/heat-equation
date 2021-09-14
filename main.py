import matplotlib.pyplot as plt
import seaborn as sns, numpy as np, locale

def main():
    #α = 0.0001
    αΔtΔx2 = 0.2
    ny = 500
    nx = 11
    
    p = np.arange(0, 0.5, 0.5/nx)
    
    T = np.zeros(shape=(ny, nx))
    T[0][1:-1] = 20
    
    for l in range(0, ny-1, 5):
        for i in range(1, nx-1):
            T[l+1][i] = T[l][i] + (αΔtΔx2) * (T[l][i+1] - 2*T[l][i] + T[l][i-1])
            
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    sns.set()
    sns.set_style("white")
    
    plt.plot(T[-1], p)
    plt.grid()
    #plt.autoscale(axis='y', tight=True)
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Posição (cm)")
    plt.show()
    
if __name__ == '__main__':
    main()