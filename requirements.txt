import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')

st.title("🧮 Kalkulator Integral & Turunan (KalkulusX)")
fungsi_input = st.text_input("Masukkan fungsi aljabar (misal: x*2 + 3*x):", "x*2 + 3*x")
fungsi = sp.sympify(fungsi_input)

operasi = st.radio("Pilih Operasi:", ["Turunan", "Integral"])

# Hasil simbolik
if operasi == "Turunan":
    hasil = sp.diff(fungsi, x)
    st.latex(f"f'(x) = {sp.latex(hasil)}")
else:
    hasil = sp.integrate(fungsi, x)
    st.latex(f"\\int f(x) dx = {sp.latex(hasil)} + C")

# Evaluasi numerik
titik = st.number_input("Evaluasi pada x =", value=1.0)
evaluasi = hasil.subs(x, titik)
st.write(f"Hasil evaluasi pada x = {titik} adalah {evaluasi}")

# Grafik
st.subheader("Grafik Fungsi dan Hasil")
x_vals = np.linspace(-10, 10, 400)
f_lambd = sp.lambdify(x, fungsi, modules=["numpy"])
h_lambd = sp.lambdify(x, hasil, modules=["numpy"])

plt.figure(figsize=(10,5))
plt.plot(x_vals, f_lambd(x_vals), label='Fungsi Asli f(x)', color='blue')
plt.plot(x_vals, h_lambd(x_vals), label='Hasil Operasi', color='red')
plt.legend()
plt.grid(True)
st.pyplot(plt)
