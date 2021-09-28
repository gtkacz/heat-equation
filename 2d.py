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
    
    Tcentro = 100
    
    x = np.arange(0, L + Δx, Δx)
    
    linhas = colunas = len(x)
    n = int(t_f/Δt)
    F0 = 25
    
    l = np.zeros((n, linhas, colunas))
    l[0:n][0][1:colunas-1] = Tcentro
    
    for k in range(0, t_f-1, 1):
        for i in np.arange(1, L - 0.1, Δx):
            for j in np.arange(1, L - 0.1, Δx):
                l[k + 1, i, j] = (l[k][i+1][j] + l[k][i-1][j] + l[k][i][j+1] + l[k][i][j-1] - 4*l[k][i][j]) + l[k][i][j]
                
    sns.heatmap(l[-1])

if __name__ == '__main__':
    main()