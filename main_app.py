# Import the libraries
import streamlit as st
from joblib import load

# Set the form key
form = st.form(key='my-form')
# Load the machine learning model
model = load('models/model.pkl')

# For input forms
clump_thickness = form.text_input('Masukkan nilai clump_thickness : ')
uniformity_cell_size = form.text_input('Masukkan nilai uniformity_cell_size : ')
uniformity_cell_shape = form.text_input('Masukkan nilai uniformity_cell_shape : ')
marginal_adhesion = form.text_input('Masukkan nilai marginal_adhesion : ')
single_epithelial_cell_size = form.text_input('Masukkan nilai single_epithelial_cell_size : ')
bare_nuclei = form.text_input('Masukkan nilai bare_nuclei : ')
bland_chromatin = form.text_input('Masukkan nilai bland_chromatin : ')
normal_nucleoli = form.text_input('Masukkan nilai normal_nucleoli : ')
mitoses = form.text_input('Masukkan nilai mitoses : ')

# Submit button
submit = form.form_submit_button("Classify!")

# If the user press the button
if submit:
    # Predict the input
    hasiil_prediksi = model.predict([[
            float(clump_thickness),
            float(uniformity_cell_size),
            float(uniformity_cell_shape),
            float(marginal_adhesion),
            float(single_epithelial_cell_size),
            float(bare_nuclei),
            float(bland_chromatin),
            float(normal_nucleoli),
            float(mitoses)]])[0]
    
    # Put the prediction to the proper format
    hasiil_prediksi = "tidak kena kanker payudara" if hasiil_prediksi == 2 else "ada kanker payudara"

    # Show the result
    st.write("Hasil perhitungan")
    st.write("Pasien " + hasiil_prediksi)