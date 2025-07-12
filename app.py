import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')

def main():
    print("=== KALKULATOR TURUNAN & INTEGRAL ===")
    func_input = input("Masukkan fungsi aljabar (dalam x): ")
    func = sp.sympify(func_input)

    print("\nPilih Operasi:")
    print("1. Turunan")
    print("2. Integral")
    choice = input("Pilihan Anda (1/2): ")

    if choice == "1":
        derivative = sp.diff(func, x)
        print(f"\nHasil turunan simbolik: {derivative}")
        turunan_num = sp.lambdify(x, derivative, "numpy")
        plot_function(func, turunan_num, "Turunan")
    elif choice == "2":
        integral = sp.integrate(func, x)
        print(f"\nHasil integral simbolik: {integral}")
        integral_num = sp.lambdify(x, integral, "numpy")
        plot_function(func, integral_num, "Integral")
    else:
        print("Pilihan tidak valid.")

def plot_function(original_func, transformed_func, label):
    f_original = sp.lambdify(x, original_func, "numpy")
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_original(x_vals)
    y_transformed = transformed_func(x_vals)

    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, label='Fungsi Asli', color='blue')
    plt.plot(x_vals, y_transformed, label=f'{label} Fungsi', color='red')
    plt.title(f"Grafik Fungsi dan {label}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
