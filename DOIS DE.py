import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

plate_length = 50
max_iter_time = 750

alpha = 2
delta_x = 1

delta_t = (delta_x ** 2)/(4 * alpha)
F0 = (alpha * delta_t) / (delta_x ** 2)

u = np.empty((max_iter_time, plate_length, plate_length))
Er = np.empty((max_iter_time, plate_length, plate_length))

u_initial = 0

u_top = 100.0
u_left = 0.0
u_bottom = 0.0
u_right = 0.0

u.fill(u_initial)
Er.fill(0)

u[:, (plate_length-1):, :] = u_top
u[:, :, :1] = u_left
u[:, :1, 1:] = u_bottom
u[:, :, (plate_length-1):] = u_right

def calculate(u):
    for k in tqdm(range(0, max_iter_time-1, 1)):
        for i in range(1, plate_length-1, delta_x):
            for j in range(1, plate_length-1, delta_x):
                u[k + 1, i, j] = F0 * (u[k][i+1][j] + u[k][i-1][j] + u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j]) + u[k][i][j]
        Er[k + 1, i, j] = abs((u[k + 1, i, j] - u[k, i, j])/u[k + 1, i, j])

    return u

def plotheatmap(u_k, k):
    plt.clf()

    plt.title(f"Temperatura em t = {k*delta_t:.3f}")
    plt.xlabel("x")
    plt.ylabel("y")

    # This is to plot u_k (u at time-step k)
    plt.pcolormesh(u_k, cmap=plt.cm.jet, vmin=0, vmax=100)
    plt.colorbar()

    return plt

u = calculate(u)
k = max_iter_time - 1
plotheatmap(u[k], k)
print(Er)
plt.show()