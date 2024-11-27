import streamlit as st
st.markdown("# Título Principal")
st.markdown("## subtítulo")
st.markdown("texto em **negrido** e *itálico*")
st.markdown("- Item 1\n- Item2\n- Item 3")

st.markdown("[visite meu site](https://www.entra.com.br)")

st.markdown("""
# Exemplo de Markdown
Texto **negrito**, texto *itálico* e texto ~~riscado~~.

## Lista não ordenada
- Item A
- Item B
- Item C

## Lista ordenada
1. Primeiro
2. Segundo
3. Terceiro

[Visite o site do Streamlit](https://streamlit.io)

```python
# Bloco de código
print("Olá, Markdown!")
nome=int(input("Digite seu nome: ))
""")

st.markdown('<h1 style="color:blue;">Título Azul</h1>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Coluna 1")
    st.markdown("- Item A\n- Item B")

with col2:
    st.markdown("### Coluna 2")
    st.markdown("- Item C\n- Item D")

st.title('Tutorial de Análise de Dados')
st.markdown("""
## Passo 1: Carregando os Dados
Primeiro, carregue seu arquivo CSV usando o widget de upload.

## Passo 2: Analisando as Colunas
Use as funções de filtragem para explorar os dados. Você pode selecionar as colunas para exibição usando os controles ao lado.
""")

pip install cryptography

from cryptography.fernet import Fernet

# Gera uma chave para criptografia
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)
    return chave

# Carregar a chave do arquivo
def carregar_chave():
    return open("chave.key", "rb").read()

# Função para criptografar a mensagem
def criptografar_mensagem(mensagem, chave):
    fernet = Fernet(chave)
    mensagem_criptografada = fernet.encrypt(mensagem.encode())
    return mensagem_criptografada

# Função para descriptografar a mensagem
def descriptografar_mensagem(mensagem_criptografada, chave):
    fernet = Fernet(chave)
    mensagem_descriptografada = fernet.decrypt(mensagem_criptografada).decode()
    return mensagem_descriptografada

# Exemplo de uso
if __name__ == "__main__":
    # Gerar uma chave e salvar
    chave = gerar_chave()

    # Ou, se a chave já foi gerada, carregue-a
    # chave = carregar_chave()

    # Mensagem a ser criptografada
    mensagem = "Esta é uma mensagem secreta."

    # Criptografando
    mensagem_criptografada = criptografar_mensagem(mensagem, chave)
    print(f"Mensagem criptografada: {mensagem_criptografada}")

    # Descriptografando
    mensagem_original = descriptografar_mensagem(mensagem_criptografada, chave)
    print(f"Mensagem descriptografada: {mensagem_original}")
