import streamlit as st
import google.generativeai as genai 

#Web app and layout
st.set_page_config(page_title='Text to SQL', page_icon=None)
col1, col2 = st.columns((0.8,1.2))
col1.image('cads_blue.png', width=200)
col2.markdown("# :blue[ SQL Generator]")
st.write("#### :blue[ Este generador SQL usa Gemini]")
query_input = st.text_area('Introduce tu prompt en inglés simple')
submit = st.button('Generate SQL')








