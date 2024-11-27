import streamlit as st

# Dados dos produtos
produtos = [
    {"nome": "Produto A", "preco": 50.00, "imagem": "https://via.placeholder.com/150?text=Produto+A"},
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
        if st.button("Efetuar pagamento"):
            st.success(f"Pagamento de R$ {total:.2f} realizado com sucesso!")
            return True
    else:
        st.warning("Adicione itens ao carrinho para finalizar a compra.")

# Função principal para exibir os produtos e carrinho
def loja():
    st.title("Mini Loja")
    
    # Usando o session_state para armazenar o carrinho de compras
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

    # Exibindo o carrinho
    total = exibir_carrinho(st.session_state.carrinho)

    # Simulando o pagamento
    pagar(total)

# Executando a loja
if __name__ == "__main__":
    loja()

