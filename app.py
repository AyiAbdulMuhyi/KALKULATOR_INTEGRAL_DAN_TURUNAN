import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(
    page_title="KalkulusX - Kalkulator Integral & Turunan",
    layout="centered"
)

# CSS Styling untuk mempercantik tampilan
st.markdown("""
    <style>
        .main {
            background-color: #f0f6ff;
        }
        h1, h4 {
            text-align: center;
        }
        .stTextInput>div>div>input {
            background-color: #ffffff;
            padding: 10px;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #0A74DA;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Judul Aplikasi
st.markdown("<h1 style='color:#0A74DA;'>🧮 KalkulusX</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='color:#555;'>Kalkulator Integral dan Turunan Fungsi Aljabar</h4>", unsafe_allow_html=True)
st.markdown("---")

# Input Fungsi
st.subheader("✏️ Masukkan Fungsi f(x)")
fungsi_input = st.text_input("Contoh: x**2 + 3*x", value="x**2 + 3*x")

# Validasi fungsi
try:
    x = sp.Symbol('x')
    fungsi = sp.sympify(fungsi_input)
except (sp.SympifyError, TypeError):
    st.error("❌ Format fungsi tidak valid. Contoh yang benar: x**2 + 3*x")
    st.stop()

# Pilihan Operasi
st.subheader("⚙️ Pilih Operasi")
operasi = st.radio("Operasi yang ingin dilakukan:", ["Turunan", "Integral"], horizontal=True)

# Operasi Simbolik
st.subheader("🧠 Hasil Simbolik")
if operasi == "Turunan":
    hasil = sp.diff(fungsi, x)
    st.latex(f"f'(x) = {sp.latex(hasil)}")
else:
    hasil = sp.integrate(fungsi, x)
    st.latex(f"\\int f(x)\\,dx = {sp.latex(hasil)} + C")

# Evaluasi Numerik
st.subheader("📍 Evaluasi Numerik pada x")
titik = st.number_input("Masukkan nilai x:", value=1.0)
evaluasi = hasil.subs(x, titik)
st.success(f"Hasil evaluasi pada x = {titik} adalah **{evaluasi}**")

# Grafik Fungsi
st.subheader("📈 Grafik Fungsi dan Hasil Operasi")
x_vals = np.linspace(-10, 10, 400)

# Konversi fungsi simbolik ke bentuk numerik
f_lambd = sp.lambdify(x, fungsi, modules=["numpy"])
h_lambd = sp.lambdify(x, hasil, modules=["numpy"])

try:
    y_f = f_lambd(x_vals)
    y_h = h_lambd(x_vals)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x_vals, y_f, label="f(x)", color="blue")
    ax.plot(x_vals, y_h, label="Hasil Operasi", color="red")
    ax.set_title("Grafik f(x) dan " + ("f'(x)" if operasi == "Turunan" else "∫f(x) dx"))
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
except Exception as e:
    st.error("❌ Grafik tidak dapat ditampilkan untuk fungsi ini.")

st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>© 2025 • Dibuat dengan ❤️ oleh Mahasiswa Kalkulus</p>", unsafe_allow_html=True)
