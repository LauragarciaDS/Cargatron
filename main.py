from importlib.resources import path
import streamlit as st
import pandas as pd
import numpy as np
import funtions as ft


#st.set_page_config(layout='wide')



st.set_page_config(layout='wide')

st.markdown('**Como te encuentras hoy?**')

pagina = st.sidebar.selectbox('Página', ('Home', 'Datos'))

if pagina == 'Home':
    ft.home()
elif pagina == 'Datos':  # tantas paginas como tengamos
    ft.datos()
    












# with st.expander("Descripcion"):  a mi me ha salido con esto
#     st.markdown("Esto será una descripción para encontrar elcargador más cercano a tu casa")
#     st.code("""with st.expander("Descripcion"):
#     st.markdown("Esto será una descripción para encontrar elcargador más cercano a tu casa")""")




