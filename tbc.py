#=============================file linked
from get_data import *

#=============================import libraries
import streamlit as st


#=============================funcition declarations
def tbc():
    # Dataset
    tbc_2020 = get_data("tbc_2020")
    tbc_2021 = get_data("tbc_2021")

    # Logo
    st.sidebar.image('./images/logo1.png')

    # Filter
    st.sidebar.header("Masukan filter disini:")
    kec = st.sidebar.multiselect(
    "Pilih kecamatan:",
    options=tbc_2020["kecamatan"].unique(),
    default=tbc_2020["kecamatan"].unique()
)
    pus = st.sidebar.multiselect(
    "Pilih puskesmas:",
    options=tbc_2021["puskesmas"].unique(),
    default=tbc_2021["puskesmas"].unique()
)
    tbc_2020_selection  = tbc_2020.query(
    "kecamatan == @kec & puskesmas == @pus"
    ) 
    tbc_2021_selection  = tbc_2021.query(
    "kecamatan == @kec & puskesmas == @pus"
)

    #Visualisasi