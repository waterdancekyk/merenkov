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
    mandelbrot_image = np.zeros((height, width))

    for i in range(width):
        for j in range(height):
            mandelbrot_image[j, i] = mandelbrot(r1[i] + 1j * r2[j], max_iter)

    return mandelbrot_image

def julia(c, max_iter):
    def f(z):
        return z**2 + c

    return f

def julia_set(xmin, xmax, ymin, ymax, width, height, c, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    julia_image = np.zeros((height, width))

    for i in range(width):
        for j in range(height):
            z = r1[i] + 1j * r2[j]
            n = 0
            while abs(z) <= 2 and n < max_iter:
                z = z**2 + c
                n += 1
            julia_image[j, i] = n

    return julia_image

def plot_fractal(fractal_image, title, xmin, xmax, ymin, ymax):
    plt.imshow(fractal_image.T, extent=[xmin, xmax, ymin, ymax], cmap='hot')
    plt.colorbar()
    plt.title(title)
    plt.show()

def main():
    try:
        # Настройки для построения множества Мандельброта
        xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
        width, height = 800, 800
        max_iter = 256

        # Генерация множества Мандельброта
        mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
        plot_fractal(mandelbrot_image, "Множество Мандельброта", xmin, xmax, ymin, ymax)

        # Настройки для построения множества Жулиа
        c = complex(-0.8, 0.156)  # Комплексное число для множества Жулиа
        julia_image = julia_set(xmin, xmax, ymin, ymax, width, height, c, max_iter)
        plot_fractal(julia_image, "Множество Жулиа", xmin, xmax, ymin, ymax)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Программа завершена.")

# Запускаем программу
if __name__ == "__main__":
    main()
