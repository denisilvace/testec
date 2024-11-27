import streamlit as st

# Inicializar o estado da página se não estiver no session_state
if 'page' not in st.session_state:
    st.session_state.page = 'iniciar'  # Página inicial

# Função para exibir o conteúdo da "Página Iniciar"
def iniciar_page():
    st.title("Página Inicial")
    st.write("Bem-vindo à página inicial!")
    st.write("Clique acima para saber mais sobre nós.")

# Função para exibir o conteúdo da "Página Sobre Nós"
def sobre_nos_page():
    st.title("Sobre Nós")
    st.write("Aqui está um pouco sobre nossa empresa...")
    st.write("Clique acima para voltar à página inicial.")

# Layout do menu superior (usando colunas para centralizar)
col1, col2, col3 = st.columns([1, 4, 1])

with col2:  # O menu será exibido aqui no centro
    menu_option = st.radio("Navegação", ["Iniciar", "Sobre Nós"], horizontal=True)

# Controle de navegação baseado na opção do menu
if menu_option == "Iniciar":
    st.session_state.page = "iniciar"
elif menu_option == "Sobre Nós":
    st.session_state.page = "sobre_nos"

# Exibindo o conteúdo com base na página escolhida
if st.session_state.page == "iniciar":
    iniciar_page()
elif st.session_state.page == "sobre_nos":
    sobre_nos_page()
