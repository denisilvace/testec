import googlemaps
import streamlit as st

# Configure a chave da API do Google Maps
gmaps = googlemaps.Client(key='SUA_CHAVE_DE_API')

# Exemplo de geocodificação (converter endereço em coordenadas)
endereco = st.text_input('Digite um endereço para geolocalizar:')
if endereco:
    resultado = gmaps.geocode(endereco)
    if resultado:
        lat, lng = resultado[0]['geometry']['location'].values()
        st.write(f'Coordenadas: {lat}, {lng}')
    else:
        st.write('Endereço não encontrado.')