import streamlit as st
import json
from scraper_api import raspar_url
from gpt_organizer import organizar_com_gpt
from utils import salvar_csv, salvar_excel

st.title("Organização com ChatGPT")

chave_api = st.text_input("Cole sua chave da OpenAI:", type="password")
url = st.text_input("URL para raspar e organizar")

if st.button("Executar com GPT"):
    if not chave_api or not url:
        st.warning("Preencha a chave da OpenAI e a URL.")
    else:
        dados = raspar_url(url)
        st.subheader("Dados brutos:")
        st.json(dados)

        organizados = organizar_com_gpt(dados, chave_api)

        st.subheader("Dados organizados:")
        st.dataframe(organizados)

        csv = salvar_csv(organizados, "gpt_organizado.csv")
        xlsx = salvar_excel(organizados, "gpt_organizado.xlsx")

        st.download_button("Baixar CSV", open(csv, "rb"), file_name="gpt_organizado.csv")
        st.download_button("Baixar Excel", open(xlsx, "rb"), file_name="gpt_organizado.xlsx")
