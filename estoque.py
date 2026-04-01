from Modelos.produtos import Produtos
from datetime import datetime
import json
import os



Histórico = []

#------------------FUNÇÕES:

def mostrar_menu(): #Mostra o menu de opções
        print(
        "Estoque\n"
        "1-Listar Produtos\n"
        "2-Cadastrar Produto\n"
        "3-Excluir Produto\n"
        "4-Entrada de estoque\n"
        "5-Saída de estoque\n"
        "6-Editar Produto\n"
        "7-Histórico de entrada/saída de estoque"
    )
        escolher_funcionalidade()

def limpar_terminal(): # Limpa o terminal.
    input("Pressione qualquer tecla para recomeçar")
    os.system("cls")

def escolher_funcionalidade(): # Permite o usuário escolher qual funcionalidade deseja acessar.
    try:
        finalidade = int(input("Qual função deseja executar?  "))
        match finalidade:
            case 1:
                listar_produtos()
                limpar_terminal()
            case 2:
                cadastrar_produto()
            case 3:
                excluir_produto()
            case 4:
                entrada_estoque()
            case 5:
                saida_estoque()
            case 6:
                editar_produto()
            case 7:
                mostrar_historico()
            case _:
                'x'
                limpar_terminal()
                return
    except ValueError:
        'x'
        limpar_terminal()
        return

def salvar_dados():
    if os.path.exists("dados.json"):
        with open("dados.json", "w", encoding= 'utf-8') as arquivo:
            json.dump([v.to_dict() for v in Estoque], arquivo, indent=4, ensure_ascii=False)

def definir_lista():
    if os.path.exists('dados.json'):
        with open("dados.json", "r", encoding= 'utf-8') as arquivo:
             return json.load(arquivo)

def adicionar_historico(registro_recebido):
    registro = datetime.now()
    registro_formatado = f'{registro_recebido} às {registro.strftime("%H:%M")} do dia {registro.strftime("%d/%m/%Y")}'
    Histórico.append(registro_formatado)

def mostrar_historico():
    if len(Histórico) > 0:
        for registro in Histórico:
            print(registro)
        limpar_terminal()
        return
    else:
        print("Ainda não há histórico de mudanças de estoque")
        limpar_terminal()
        return


def verificar_se_ha_produtos(): # Verifica se a lista não está vazia.
    return len(Estoque) > 0

def listar_produtos(): # Lista os produtos no estoque
    if verificar_se_ha_produtos():
        for produto in Estoque:
            print(produto)
            return
    else:
        print("Não há produtos cadastrados, cadastre e tente novamente!")
        limpar_terminal()
        return

def procurar_produto_nalista(produtoembusca):
    produto_existe = None
    for produto in Estoque:
        if produtoembusca.lower().strip() == produto.nome.lower():
            produto_existe = True
            produto_encontrado = produto
            break
        else:
            continue
    if produto_existe:
        return produto_encontrado
    else:
        return produto_existe
    
def cadastrar_produto(): # Permite que o usuário cadastre produtos
    nome_novo_produto = input("Qual nome do produto?  ")
    verificacao_se_existe = procurar_produto_nalista(nome_novo_produto)
    if verificacao_se_existe == None:
        try:
            quantidade_novo_produto = int(input("Quantos há desse produto em estoque?  "))
            preçodecompra_novo_produto = float(input("Por quanto você comprou essse produto?  "))
            preçodevenda_novo_produto = float(input("Por quanto você vai vender esse produto?  "))
            if quantidade_novo_produto <= 0 or preçodecompra_novo_produto <= 0 or preçodevenda_novo_produto <= 0:
                print("Só aceitamos valores maiores que 0, tente novamente!")
                limpar_terminal()
                return
            elif preçodecompra_novo_produto > preçodevenda_novo_produto:
                print("Você está no prejuízo, defina o preço de venda sendo maior que o de compra!")
                limpar_terminal()
                return
            else:
                Estoque.append(Produtos(nome_novo_produto.strip().title(), quantidade_novo_produto, preçodecompra_novo_produto, preçodevenda_novo_produto))
                print("Seu Produto foi cadastrado!")
                salvar_dados()
                limpar_terminal()
                return
        except ValueError:
            'x'
            return
    else:
        print("Esse produto já está cadastrado, tente novamente.")
        limpar_terminal()
        return
    
def excluir_produto(): # Permite que o usuário exclua um produto cadastrado
    if verificar_se_ha_produtos():
        listar_produtos()
        produto_futuramente_excluido = input("Qual o nome do produto?  ")
        produto_excluido = procurar_produto_nalista(produto_futuramente_excluido)
        if produto_excluido != None:
            Estoque.remove(produto_excluido)
            print("Seu produto foi excluído!")
            salvar_dados()
            limpar_terminal()
            return
        else:
            print("Esse produto não está cadastrado.")
            limpar_terminal()
            return
    else:
        print("Não há produtos cadastrados, cadastre e tente novamente!")
        limpar_terminal()
        return

def entrada_estoque():
    if verificar_se_ha_produtos():
        listar_produtos()
        produto_futuramente_adicao_estoque = input("Qual produto você quer adicionar quantidade?  ")
        produto_adicao_estoque = procurar_produto_nalista(produto_futuramente_adicao_estoque)
        if produto_adicao_estoque != None:
            try:
                quantidade_adicionada = int(input(f"Quanto foi comprado de {produto_adicao_estoque.nome}?  "))
                if quantidade_adicionada > 0:
                  produto_adicao_estoque.quantidade += quantidade_adicionada
                  print(f"A quantia foi adicionada, agora há {produto_adicao_estoque.quantidade} unidades de {produto_adicao_estoque.nome}!")
                  salvar_dados()
                  registro_entrada = f'+ {quantidade_adicionada} unidades de {produto_adicao_estoque.nome}'
                  adicionar_historico(registro_entrada)
                  limpar_terminal()
                  return
                else:
                    print("Só há como adicionar quantidades maiores que 0! Tente novamente.")
                    limpar_terminal()
                    return
            except ValueError:
               'x'
               limpar_terminal()
               return
        else:
            print("Esse produto não está cadastrado.")
            limpar_terminal()
            return
    else:
        print("Não há produtos cadastrados, cadastre e tente novamente!")
        limpar_terminal()
        return
    
def saida_estoque():
    if verificar_se_ha_produtos():
        listar_produtos()
        produto_futuramente_subtracao_estoque = input("Qual produto você quer retirar quantidade?  ")
        produto_subtracao_estoque = procurar_produto_nalista(produto_futuramente_subtracao_estoque)
        if produto_subtracao_estoque != None:
            try:
                quantidade_retirada = int(input(f"Quanto foi vendido de {produto_subtracao_estoque.nome}?  "))
                if quantidade_retirada > 0 and produto_subtracao_estoque.quantidade >= quantidade_retirada:
                  produto_subtracao_estoque.quantidade -= quantidade_retirada
                  print(f"A quantia foi retirada, agora há {produto_subtracao_estoque.quantidade} unidades de {produto_subtracao_estoque.nome}!")
                  salvar_dados()
                  registro_saida = f'- {quantidade_retirada} unidades de {produto_subtracao_estoque.nome}'
                  adicionar_historico(registro_saida)
                  limpar_terminal()
                  return
                else:
                    print("Só há como adicionar quantidades maiores que 0 e menores que a quantidade inicial! Tente novamente.")
                    limpar_terminal()
                    return
            except ValueError:
               'x'
               limpar_terminal()
               return
        else:
            print("Esse produto não está cadastrado.")
            limpar_terminal()
            return
    else:
        print("Não há produtos cadastrados, cadastre e tente novamente!")
        limpar_terminal()
        return

def editar_produto():
    if verificar_se_ha_produtos():
        listar_produtos()
        produto_futuramente_editado = input("Qual Produto deseja editar?  ")
        produto_editado = procurar_produto_nalista(produto_futuramente_editado)
        if produto_editado != None:
            novo_nome = input("Qual nome deseja colocar nesse produto?  ").title().strip()
            try:
                nova_quantidade = int(input("Qual a quantidade desse produto?  "))
                if nova_quantidade < 0:
                    print("Só há como por números maiores ou iguais a 0, tente novamente")
                    limpar_terminal()
                    return
                novo_preço_compra = float(input("Qual o preço de compra desse produto?  "))
                novo_preço_venda = float(input("Qual o preço de venda?  "))
                if novo_preço_compra <= 0 or novo_preço_venda <= 0:
                    print("Só há como por números maiores ou diferentes a 0, tente novamente")
                    limpar_terminal()
                    return
                elif novo_preço_compra >  novo_preço_venda:
                    print("Você está no prejuízo, defina o preço de venda sendo maior que o de compra!")
                    limpar_terminal()
                    return
                else:
                    produto_editado._nome = novo_nome
                    produto_editado.quantidade = nova_quantidade
                    produto_editado._preço_de_compra = novo_preço_compra
                    produto_editado._preço_de_venda = novo_preço_venda
                    salvar_dados()
                    print("Seu produto foi editado!")
                    limpar_terminal()
                    return
            except ValueError:
                'x'
                limpar_terminal()
                return
        else:
            print("Esse produto não está cadastrado.")
            limpar_terminal()
            return
    else:
        print("Não há produtos cadastrados, cadastre e tente novamente!")
        limpar_terminal()
        return



#------------------CÓDIGO DE FUNCIONAMENTO:

if __name__ == '__main__':
    while True:
        Estoque = [definir_lista()]
        mostrar_menu()




