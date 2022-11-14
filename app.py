import streamlit as st

st.title("Applikasi Web Datamining")
st.write("""
# Web Apps - Klasifikasi HousePrice Dataset
Applikasi Berbasis Web untuk Mengklasifikasi Jenis **HousePrice**
""")

algoritma = st.sidebar.selectbox(
    "Pilih Algoritma",
    ("KNN", "Naive Bayes", "Random Forest")
)
st.subheader("Parameter Inputan")

Addres = st.text_input("Masuukan Addres :")
Zip = st.text_input("Masuukan Zip :")
price = st.number_input("Masukkan Price :")
area = st.number_input("Masukkan Area :")
room = st.number_input("Masukkan Room :")
lon = st.number_input("Masukkan Lon :")
lat = st.number_input("Masukkan Lat :")
hasil = st.button("Cek Klasifikasi")

st.subheader("Prediksi (Hasil Klasifikasi)")
st.write(f"Class   = ")

st.subheader("Probabilitas Hasil Prediksi (Klasifikasi)")
st.write(f"Algoritma = {algoritma}")
st.write(f"Akurasi   = ")
