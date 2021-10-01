import matplotlib.pyplot as plt, seaborn as sns, numpy as np, locale
from math import sin, pi as 𝜋, e

def main():
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    sns.set()
    sns.set_style('dark')
    #plt.rcParams['font.family'] = 'Bahnschrift'
    
    α = 0.25
    Δx = 0.1
    Δy = 0.1
    Δt = 0.01
    L = 0.5
    t_f = 10
    
    x = np.arange(0, L + Δx, Δx)
    
    linhas = colunas = len(x)
    n = int(t_f/Δt)
    λ = 25
    
    # Initialize solution: the grid of T(l, i, j)
    T = np.empty((n, linhas, colunas))
    Er = np.empty((n, linhas, colunas))

    # Initial condition everywhere inside the grid
    u_initial = 0

    # Boundary conditions
    u_top = 100.0
    u_left = 75.0
    u_bottom = 0.0
    u_right = 50.0

    # Set the initial condition
    T.fill(u_initial)
    Er.fill(0)

    # Set the boundary conditions
    T[:, (linhas-1):, :] = u_top
    T[:, :, :1] = u_left
    T[:, :1, 1:] = u_bottom
    T[:, :, (colunas-1):] = u_right
    
    for l in range(1, n):
        for i in range(1, linhas-1):
            for j in range(1, colunas-1):
                T[l, i, j] = T[l-1, i, j] + λ*(T[l-1, i+1, j] + T[l-1, i-1, j] + T[l-1, i, j+1] + T[l-1, i, j-1] + -4*T[l-1, i, j])
        
        Er[l, i, j] = abs((T[l, i, j] - T[l - 1, i, j])/T[l, i, j])
    
    print(Er)
    sns.heatmap(T[-1])
    plt.show()

if __name__ == '__main__':
    main()