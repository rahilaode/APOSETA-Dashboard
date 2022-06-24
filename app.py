#=============================file linked
from GAMBARAN_UMUM import *
from PENYAKIT_MENULAR_LANGSUNG import *
from zoonotik import *

#=============================import libraries
import streamlit as st
import hydralit_components as hc
# https://discuss.streamlit.io/t/hydralit-navbar-custom-streamlit-component-responsive-navbar/16587
# https://github.com/TangleSpace/hydralit_components
# https://github.com/TangleSpace/hydralit


#make it look nice from the start
st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)

# specify the primary menu definition
menu_data = [
    {'id':'gambaran_umum', #GAMBARAN UMUM
    'icon': "far fa-copy", 
    'label':"Gambaran Umum"},
    {'id':'pengendalian_penyakit', #PENGENDALIAN PENYAKIT
    'icon': "far fa-copy",
    'label':"Pengendalian Penyakit", 
    'submenu':[{'id':' subid11','icon': "fa fa-paperclip", 'label':"Penyakit Tular Zoonotik"}, #SUB_Tular Zoonotok
    {'id':'subid12','icon': "far fa-copy", 'label':"Penyakit Tidak Menular"}, #SUB_tidak Menular
    {'id':'subid13','icon': "far fa-copy", 'label':"Penyakit Menular Langsung"}]}, #SUB_Menular
    {'id':'kesehatan_ibu', #KESEHATAN IBU
    'icon': "far fa-copy", 
    'label':"Kesehatan Ibu"},
    {'id':' kesehatan_lingkungan', #KESEHATAN LINGKUNGAN
    'icon': "far fa-copy", 
    'label':"Kesehatan Lingkungan"},
    ]

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    #override_theme=over_theme,
    home_name='Home',
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)

if menu_id == "gambaran_umum":
    gambaran_umum() #NYOBAA

elif menu_id == "pengendalian_penyakit":
    gambaran_umum() #NYOBAA
    



#get the id of the menu item clicked
st.info(f"{menu_id}")