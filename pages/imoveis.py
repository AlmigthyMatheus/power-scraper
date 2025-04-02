import streamlit as st
from scraper_api import raspar_url
from utils import salvar_csv, salvar_excel

st.title("Raspagem de Imóveis")

url = st.text_input("URL do site de imóveis para raspar")

campos = {
    "title_tag": st.text_input("Tag do Título", value="h1"),
    "price_tag": st.text_input("Tag do Preço", value=".price"),
    "location_tag": st.text_input("Tag da Localização", value=".location"),
}

if st.button("Raspar Imóvel"):
    dados = raspar_url(url)
    st.json(dados)

    csv = salvar_csv(dados, "imoveis.csv")
    xlsx = salvar_excel(dados, "imoveis.xlsx")

    st.download_button("Baixar CSV", open(csv, "rb"), file_name="imoveis.csv")
    st.download_button("Baixar Excel", open(xlsx, "rb"), file_name="imoveis.xlsx")
