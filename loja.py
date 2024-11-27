import streamlit as st

# Dados dos produtos
produtos = [
    {"nome": "Produto A", "preco": 50.00, "imagem": "https://cdn.pixabay.com/photo/2024/06/01/14/00/ai-8802304_1280.jpg"},
    {"nome": "Produto B", "preco": 30.00, "imagem": "https://via.placeholder.com/150?text=Produto+B"},
    {"nome": "Produto C", "preco": 70.00, "imagem": "https://via.placeholder.com/150?text=Produto+C"},
    {"nome": "Produto D", "preco": 40.00, "imagem": "https://via.placeholder.com/150?text=Produto+D"},
    {"nome": "Produto E", "preco": 90.00, "imagem": "https://via.placeholder.com/150?text=Produto+E"},
]

# Função para mostrar o carrinho de compras
def exibir_carrinho(carrinho):
    if len(carrinho) > 0:
        st.write("### Carrinho de Compras:")
        total = 0
        for produto_nome, dados in carrinho.items():
            st.write(f"{dados['produto']['nome']} - R$ {dados['produto']['preco']:.2f} x {dados['quantidade']}")
            total += dados['produto']['preco'] * dados['quantidade']
        st.write(f"**Total: R$ {total:.2f}**")
        return total
    else:
        st.write("O carrinho está vazio.")
        return 0

# Função para simular o pagamento
def pagar(total):
    if total > 0:
        st.success(f"Pagamento de R$ {total:.2f} realizado com sucesso!")
        return True
    else:
        st.warning("Adicione itens ao carrinho para finalizar a compra.")
        return False

# Função principal para exibir os produtos e carrinho
def loja():
    st.title("Mini Loja")
    
    # Inicialize o carrinho na primeira vez que a loja for carregada
    if "carrinho" not in st.session_state:
        st.session_state.carrinho = {}

    # Exibindo os produtos
    st.write("### Produtos Disponíveis:")
    
    for produto in produtos:
        col1, col2, col3 = st.columns([1, 3, 1])

        with col1:
            st.image(produto["imagem"], width=100)
        
        with col2:
            st.write(f"**{produto['nome']}**")
            st.write(f"Preço: R$ {produto['preco']:.2f}")
        
        with col3:
            # Botão para adicionar o produto ao carrinho
            if st.button(f"Adicionar {produto['nome']} ao carrinho", key=produto['nome']):
                if produto['nome'] in st.session_state.carrinho:
                    # Se o produto já estiver no carrinho, incrementa a quantidade
                    st.session_state.carrinho[produto['nome']]['quantidade'] += 1
                else:
                    # Caso o produto não esteja no carrinho, adiciona com quantidade 1
                    st.session_state.carrinho[produto['nome']] = {
                        'produto': produto,
                        'quantidade': 1
                    }
                st.success(f"{produto['nome']} adicionado ao carrinho!")

# Título da aplicação
st.title("Página Interativa com Botões")

# Criar 3 colunas para os botões
col1, col2, col3 = st.columns([1, 1, 4])

# Definir os botões
with col1:
    botao_iniciar = st.button("Iniciar")

with col2:
    botao_carrinho = st.button("Carrinho")

with col3:
    botao_contato = st.button("Contato")

# Exibir conteúdo baseado no botão pressionado
if botao_iniciar:
    # Quando o botão "Iniciar" for clicado, limpa o carrinho e exibe a loja
    if "carrinho" in st.session_state:
        st.session_state.carrinho.clear()  # Limpar carrinho
    loja()

elif botao_carrinho:
    # Garantir que o carrinho esteja inicializado
    if "carrinho" not in st.session_state:
        st.session_state.carrinho = {}
    
    # Exibindo o carrinho
    total = exibir_carrinho(st.session_state.carrinho)
    if total > 0:
        # Exibir botão de pagamento
        botaopagamento = st.button("Efetuar pagamento")
        if botaopagamento:
            if pagar(total):
                # Após o pagamento, não limpa o carrinho até que o usuário clique em "Iniciar"
                st.session_state.pago = True  # Marca que o pagamento foi realizado
    else:
        st.warning("Carrinho vazio! Adicione itens para comprar.")

elif botao_contato:
    st.write("Aqui estarão informações de contato.")

# Exibindo a mensagem de pagamento apenas se o pagamento foi realizado
if getattr(st.session_state, 'pago', False):
    st.success("Pagamento realizado com sucesso!")
    # Adicionando o botão "Iniciar" para permitir que o usuário volte à página principal
    st.write("Clique em 'Iniciar' para voltar à página inicial.")
