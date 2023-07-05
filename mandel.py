import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

width = 600
height = 400
max_iter = 100

xmin, xmax = -2.0, 0.5
ymin, ymax = -1.25, 1.25

x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)

img = np.zeros((height, width))

for i in range(height):
    for j in range(width):
        img[i, j] = mandelbrot(x[j] + 1j * y[i], max_iter)

plt.imshow(img, extent=(xmin, xmax, ymin, ymax), cmap='hot')
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Re")
plt.ylabel("Im")
plt.savefig("mandelbrot.png")
plt.show()