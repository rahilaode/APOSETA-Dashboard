from matplotlib.pyplot import plot
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
from db import get_data
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def td():
    
    # Dataset
    fasilitas_kesehatan_ibu_2020 = get_data("fasilitas_kesehatan_ibu_2020")
    fasilitas_kesehatan_ibu_2021 = get_data("fasilitas_kesehatan_ibu_2021")

    # Logo
    st.sidebar.image('./images/logo1.png')
    
    # Filter
    st.sidebar.header("Masukan filter disini:")
    kec = st.sidebar.multiselect(
    "Pilih kecamatan:",
    options=fasilitas_kesehatan_ibu_2020["kecamatan"].unique(),
    default=fasilitas_kesehatan_ibu_2020["kecamatan"].unique()
)
    pus = st.sidebar.multiselect(
    "Pilih puskesmas:",
    options=fasilitas_kesehatan_ibu_2021["puskesmas"].unique(),
    default=fasilitas_kesehatan_ibu_2021["puskesmas"].unique()
)
    kesehatan_2020_selection  = fasilitas_kesehatan_ibu_2020.query(
    "kecamatan == @kec & puskesmas == @pus"
    ) 
    kesehatan_2021_selection  = fasilitas_kesehatan_ibu_2021.query(
    "kecamatan == @kec & puskesmas == @pus"
)
    
    #Visualisasi
    
    
