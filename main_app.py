import streamlit as st
from joblib import load

form = st.form(key='my-form')
model = load('models/model.pkl')

clump_thickness = form.text_input('Masukkan nilai clump_thickness : ')
uniformity_cell_size = form.text_input('Masukkan nilai uniformity_cell_size : ')
uniformity_cell_shape = form.text_input('Masukkan nilai uniformity_cell_shape : ')
marginal_adhesion = form.text_input('Masukkan nilai marginal_adhesion : ')
single_epithelial_cell_size = form.text_input('Masukkan nilai single_epithelial_cell_size : ')
bare_nuclei = form.text_input('Masukkan nilai bare_nuclei : ')
bland_chromatin = form.text_input('Masukkan nilai bland_chromatin : ')
normal_nucleoli = form.text_input('Masukkan nilai normal_nucleoli : ')
mitoses = form.text_input('Masukkan nilai mitoses : ')

submit = form.form_submit_button("Classify!")

if submit:
    st.write("Hasil perhitungan")
    st.write("Untuk variabel Protein",
        model.predict([[
            float(clump_thickness),
            float(uniformity_cell_size),
            float(uniformity_cell_shape),
            float(marginal_adhesion),
            float(single_epithelial_cell_size),
            float(bare_nuclei),
            float(bland_chromatin),
            float(normal_nucleoli),
            float(mitoses)]])[0])