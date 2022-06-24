#=============================file linked
from get_data import *

#=============================import libraries

#=============================data declarations

#=============================funcition declarations
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