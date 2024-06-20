import streamlit as st
import google.generativeai as genai 
import os

#Web app and layout
st.set_page_config(page_title='Text to SQL', page_icon=None)
col1, col2 = st.columns((0.8,1.2))
col1.image('cads_blue.png', width=200)
col2.markdown("# :blue[ SQL Generator]")
st.write("#### :blue[ Este generador SQL usa Gemini]")
query_input = st.text_area('Introduce tu prompt en inglés simple')
submit = st.button('Generate SQL')

#Gemini API
genai.configure(api_key="API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')

supportive_info1 = ["""Based on the  prompt text, create a SQL query, and make sure to exclude ''' in the beginning and end."""]


#Submit
if submit:
    with st.spinner("Generating.."):
        st.write("##### 1. The Generated SQL Query Code :")
        response=model.generate_content([supportive_info1[0], query_input])
        st.code(response.text)




