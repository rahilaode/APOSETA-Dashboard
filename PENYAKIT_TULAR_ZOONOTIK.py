from matplotlib.pyplot import plot
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
from get_data import *
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def dbd():
    
    # Dataset
    dbd_2020 = get_data("vektor_zoonotik_2020")
    dbd_2021 = get_data("vektor_zoonotik_2021")

    # Logo
    st.sidebar.image('./images/logo1.png')
    
    # Filter
    st.sidebar.header("Masukan filter disini:")
    kec = st.sidebar.multiselect(
    "Pilih kecamatan:",
    options=dbd_2020["kecamatan"].unique(),
    default=dbd_2020["kecamatan"].unique()
    )
    pus = st.sidebar.multiselect(
    "Pilih puskesmas:",
    options=dbd_2020["puskesmas"].unique(),
    default=dbd_2020["puskesmas"].unique()
    )
    dbd_2020_selection  = dbd_2020.query(
    "kecamatan == @kec & puskesmas == @pus"
    ) 
    dbd_2021_selection  = dbd_2021.query(
    "kecamatan == @kec & puskesmas == @pus"
    )
    
    #Visualisasi
    #kasus = dbd_2021.groupby('kecamatan')["jumlah_kasus_dbd_lp"].sum()
    #kasus = kasus.reset_index()
    fig_tree21 = px.treemap(dbd_2021_selection, path=['kecamatan'],values='jumlah_kasus_dbd_lp', width=800, height=400)
    fig_tree21.update_layout(
        title = "Persebaran kasus DBD 2021",
    #treemapcolor = ["green"], #defines the colors in the treemap
        margin = dict(t=50, l=25, r=25, b=25)
    )
    #kasus_20 = dbd_2020.groupby('kecamatan')["jumlah_kasus_dbd_lp"].sum()
    #kasus_20 = kasus_20.reset_index()
    fig_tree20 = px.treemap(dbd_2020_selection, path=['kecamatan'],values='jumlah_kasus_dbd_lp', width=800, height=400)
    fig_tree20.update_layout(
         title = "Persebaran kasus DBD 2020",
    #treemapcolor = ["green"], #defines the colors in the treemap
        margin = dict(t=50, l=25, r=25, b=25)
    )    
    
    left, right = st.columns(2)
    left.plotly_chart(fig_tree20, use_container_width=True)
    right.plotly_chart(fig_tree21, use_container_width=True)
    
def malaria():
    # Dataset
    malaria_2020 = get_data("malaria_2020")
    malaria_2021 = get_data("malaria_2021")

    
    # Logo
    st.sidebar.image('./images/logo1.png')
    
    # Filter
    st.sidebar.header("Masukan filter disini:")
    kec = st.sidebar.multiselect(
    "Pilih kecamatan:",
    options=malaria_2020["kecamatan"].unique(),
    default=malaria_2020["kecamatan"].unique()
)
    pus = st.sidebar.multiselect(
    "Pilih puskesmas:",
    options=malaria_2021["puskesmas"].unique(),
    default=malaria_2021["puskesmas"].unique()
)
    malaria_2020_selection  = malaria_2020.query(
    "kecamatan == @kec & puskesmas == @pus"
    ) 
    malaria_2021_selection  = malaria_2021.query(
    "kecamatan == @kec & puskesmas == @pus"
)
    
    #Visualisasi    
