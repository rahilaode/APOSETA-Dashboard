from matplotlib.pyplot import plot
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
from get_data import *
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def diare():

    # Dataset
    diare_2020 = get_data("diare_2020")
    diare_2021 = get_data("diare_2021")

    # Logo
    st.sidebar.image('./images/logo1.png')

    # Filter
    st.sidebar.header("Masukan filter disini:")
    kec = st.sidebar.multiselect(
    "Pilih kecamatan:",
    options=diare_2020["kecamatan"].unique(),
    default=diare_2020["kecamatan"].unique()
)
    pus = st.sidebar.multiselect(
    "Pilih puskesmas:",
    options=diare_2021["puskesmas"].unique(),
    default=diare_2021["puskesmas"].unique()
)
    diare_2020_selection  = diare_2020.query(
    "kecamatan == @kec & puskesmas == @pus"
    ) 
    diare_2021_selection  = diare_2021.query(
    "kecamatan == @kec & puskesmas == @pus"
)

    #Visualisasi


def hipertensi():
    # Dataset
    hipertensi_2020 = get_data("hipertensi_2020")
    hipertensi_2021 = get_data("hipertensi_2021")

    # Logo
    st.sidebar.image('./images/logo1.png')

    # Filter
    st.sidebar.header("Masukan filter disini:")
    kec = st.sidebar.multiselect(
    "Pilih kecamatan:",
    options=hipertensi_2020["kecamatan"].unique(),
    default=hipertensi_2020["kecamatan"].unique()
)
    pus = st.sidebar.multiselect(
    "Pilih puskesmas:",
    options=hipertensi_2021["puskesmas"].unique(),
    default=hipertensi_2021["puskesmas"].unique()
)
    hipertensi_2020_selection  = hipertensi_2020.query(
    "kecamatan == @kec & puskesmas == @pus"
    ) 
    hipertensi_2021_selection  = hipertensi_2021.query(
    "kecamatan == @kec & puskesmas == @pus"
)

    #Visualisasi



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
