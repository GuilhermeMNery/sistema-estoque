from Modelos.produtos import Produtos
from Serviços.arquivo_service import Estoque, salvar_dados

def verificar_se_ha_produtos(): # Verifica se a lista não está vazia.
    return len(Estoque) > 0

def procurar_produto_nalista(produtoembusca):#Procura o produto que o usuário enviou na lista
    for produto in Estoque:
        if produtoembusca.lower().strip() == produto.nome.lower():
            return produto
    return None

def cadastrar_produto(nome, quantidade, preço_compra, preço_venda): # Permite que o usuário cadastre produtos
    Estoque.append(Produtos(nome.strip().title(), quantidade, preço_compra, preço_venda))
    salvar_dados()

def excluir_produto(produto):
    Estoque.remove(produto)
    salvar_dados()

def entrada_estoque(produto, quantidade):
    produto.quantidade += quantidade
    salvar_dados()

def saida_estoque(produto, quantidade):
    produto.quantidade -= quantidade
    salvar_dados()

def editar_produto(produto, nome, quantidade, preço_compra, preço_venda):
    produto.nome = nome
    produto.quantidade = quantidade
    produto._preço_de_compra = preço_compra
    produto._preço_de_venda = preço_venda
    salvar_dados()