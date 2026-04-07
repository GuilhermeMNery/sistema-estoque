from Modelos.produtos import Produtos
from Servicos.arquivo_service import  salvar_dados


def verificar_se_ha_produtos(Estoque): # Verifica se a lista não está vazia.
    return len(Estoque) > 0

def procurar_produto_nalista(Estoque, produtoembusca):#Procura o produto que o usuário enviou na lista
    for produto in Estoque:
        if produtoembusca.lower().strip() == produto.nome.lower():
            return produto
    return None

def cadastrar_produto(Estoque, nome, quantidade, preço_compra, preço_venda): # Permite que o usuário cadastre produtos
    Estoque.append(Produtos(nome.strip().title(), quantidade, preço_compra, preço_venda))
    salvar_dados(Estoque)

def excluir_produto(Estoque, produto):
    Estoque.remove(produto)
    salvar_dados(Estoque)

def entrada_estoque(Estoque, produto, quantidade):
    produto.quantidade += quantidade
    salvar_dados(Estoque)

def saida_estoque(Estoque, produto, quantidade):
    produto.quantidade -= quantidade
    salvar_dados(Estoque)

def editar_produto(Estoque, produto, nome, quantidade, preço_compra, preço_venda):
    produto.nome = nome
    produto.quantidade = quantidade
    produto._preço_de_compra = preço_compra
    produto._preço_de_venda = preço_venda
    salvar_dados(Estoque)