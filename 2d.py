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
    
    # Initialize solution: the grid of l(k, i, j)
    l = np.empty((n, linhas, colunas))

    # Initial condition everywhere inside the grid
    u_initial = 0

    # Boundary conditions
    u_top = 100.0
    u_left = 75.0
    u_bottom = 0.0
    u_right = 50.0

    # Set the initial condition
    l.fill(u_initial)

    # Set the boundary conditions
    l[:, (linhas-1):, :] = u_top
    l[:, :, :1] = u_left
    l[:, :1, 1:] = u_bottom
    l[:, :, (colunas-1):] = u_right
    
    for k in range(1, n):
        for i in range(1, linhas-1):
            for j in range(1, colunas-1):
                l[k, i, j] = l[k-1, i, j] + λ*(l[k-1, i+1, j] + l[k-1, i-1, j] + l[k-1, i, j+1] + l[k-1, i, j-1] + -4*l[k-1, i, j])
    
    sns.heatmap(l[-1])
    plt.show()

if __name__ == '__main__':
    main()