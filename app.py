import numpy as np
import streamlit as st
from sklearn.preprocessing import StandardScaler
from streamlit_option_menu import option_menu
from stroke_page import get_stroke_page
from diabet_page import get_diabet_page


with st.sidebar: 
    selected = option_menu('Прогноз заболеваний',
                          ['Инсульт',
                           'Диабет'],
                          icons=['person','person'], menu_icon="book",
                          default_index=0)
    
if (selected=="Инсульт"):
    get_stroke_page()
elif (selected=="Диабет"):
    get_diabet_page()
    
