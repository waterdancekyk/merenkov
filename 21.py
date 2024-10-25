import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    mandelbrot_image = np.zeros((height, width))  # Изменено: (height, width)

    for i in range(width):
        for j in range(height):
            mandelbrot_image[j, i] = mandelbrot(r1[i] + 1j * r2[j], max_iter)  # Изменено: j, i

    return mandelbrot_image

# Настройки для построения фрактала
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 800, 800
max_iter = 256

# Генерация множества Мандельброта
image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

# Визуализация фрактала
plt.imshow(image.T, extent=[xmin, xmax, ymin, ymax], cmap='hot')
plt.colorbar()
plt.title("Mandelbrot Set")
plt.show()
