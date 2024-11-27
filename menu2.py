import streamlit as st

# Título da aplicação
st.title("Página Interativa com Botões")

# Criar 3 colunas para os botões
col1, col2, col3 = st.columns([1, 1, 4])

# Definir os botões
with col1:
    botao_iniciar = st.button("Iniciar")

with col2:
    botao_sobre_nos = st.button("Sobre Nós")

with col3:
    botao_contato = st.button("Contato")

# Exibir conteúdo baseado no botão pressionado
if botao_iniciar:
    st.subheader("Bem-vindo ao nosso site!")
    st.write("Aqui está o início da nossa aplicação.")
    st.write("Você pode navegar para outras páginas usando os botões acima.")
    
elif botao_sobre_nos:
    st.subheader("Sobre Nós")
    st.write("Somos uma empresa inovadora, dedicada a oferecer as melhores soluções tecnológicas.")
    st.write("Nossa missão é transformar o futuro através da tecnologia e criatividade.")
    
elif botao_contato:
    st.subheader("Entre em Contato")
    st.write("Se você deseja falar conosco, use os seguintes meios de contato:")
    st.write("📧 Email: contato@empresa.com")
    st.write("📞 Telefone: +55 11 1234-5678")
    
else:
    st.write("Clique em um dos botões acima para navegar pelas páginas.")
