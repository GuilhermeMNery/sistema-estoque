import os
import Serviços.arquivo_service
from Serviços.arquivo_service import Estoque, Histórico, adicionar_historico
from Serviços.estoque_service import procurar_produto_nalista, verificar_se_ha_produtos, cadastrar_produto, excluir_produto, entrada_estoque, saida_estoque, editar_produto

def mostrar_menu(): #Mostra o menu de opções
        print(
        "Estoque\n"
        "1-Listar Produtos\n"
        "2-Cadastrar Produto\n"
        "3-Excluir Produto\n"
        "4-Entrada de estoque\n"
        "5-Saída de estoque\n"
        "6-Editar Produto\n"
        "7-Histórico de entrada/saída de estoque\n"
        "8-Sair"
    )
        escolher_funcionalidade()

def limpar_terminal(): # Limpa o terminal.
    input("Pressione qualquer tecla para recomeçar")
    os.system("cls" if os.name == 'nt' else "clear")

def escolher_funcionalidade(): # Permite o usuário escolher qual funcionalidade deseja acessar.
    try:
        finalidade = int(input("Qual função deseja executar?  "))
        match finalidade:
            case 1:
                listar_produtos()
                limpar_terminal()
            case 2:
                valores = obter_produto_cadastrado()
                cadastrar_produto(valores[0], valores[1], valores[2], valores[3])
            case 3:
                listar_produtos()
                excluir_produto(obter_produto_excluido())
            case 4:
                listar_produtos()
                valores = obter_entrada_estoque()
                entrada_estoque(valores)
                registro_entrada = f'+ {valores[0]} unidades de {valores[1].nome}'
                adicionar_historico(registro_entrada)

            case 5:
                listar_produtos()
                valores = obter_saida_estoque()
                saida_estoque(valores)
                registro_saida = f'+ {valores[0]} unidades de {valores[1].nome}'
                adicionar_historico(registro_saida)

            case 6:
                editar_produto(obter_produto_editado)
            case 7:
                escolha_filtrohistorico()
            case 8:
                exit()
            case _:
                print('❌ Número inválido, tente novamente!')
                limpar_terminal()
                return
    except ValueError:
        print("❌ Só aceitamos números, tente novamente")
        limpar_terminal()
        return

def listar_produtos(): # Lista os produtos no estoque
    if verificar_se_ha_produtos():
        for produto in Estoque:
            print(produto)
        return
    else:
        print("Não há produtos cadastrados, cadastre e tente novamente!")
        limpar_terminal()
        return
    
def obter_produto_cadastrado():
    nome_novo_produto = input("Qual nome do produto?  ")
    verificacao_se_existe = procurar_produto_nalista(nome_novo_produto)
    if verificacao_se_existe is not  None:
        if nome_novo_produto is None:
            print('❌ O produto tem que ter um nome!')
            limpar_terminal()
            return
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
                print("Seu Produto foi cadastrado!")
                limpar_terminal()
                return nome_novo_produto, quantidade_novo_produto, preçodecompra_novo_produto, preçodevenda_novo_produto
        except ValueError:
            print("❌ Só aceitamos números, tente novamente")
            return
    else:
        print("❌ Esse produto já está cadastrado, tente novamente.")
        limpar_terminal()
        return

def obter_produto_excluido(): # Permite que o usuário exclua um produto cadastrado
        produto_futuramente_excluido = input("Qual o nome do produto?  ")
        produto_excluido = procurar_produto_nalista(produto_futuramente_excluido)
        if produto_excluido is not None:
            print("Seu produto foi excluído!")
            limpar_terminal()
            return produto_excluido
        else:
            print("❌ Esse produto não está cadastrado.")
            limpar_terminal()
            return
        
def obter_entrada_estoque():#Permite aumentar a quantidade de um produto
    produto_futuramente_adicao_estoque = input("Qual produto você quer adicionar quantidade?  ")
    produto_adicao_estoque = procurar_produto_nalista(produto_futuramente_adicao_estoque)
    if produto_adicao_estoque is not None:
        try:
            quantidade_adicionada = int(input(f"Quanto foi comprado de {produto_adicao_estoque.nome}?  "))
            if quantidade_adicionada > 0:
                print(f"A quantia foi adicionada, agora há {(produto_adicao_estoque.quantidade + quantidade_adicionada)} unidades de {produto_adicao_estoque.nome}!") 
                limpar_terminal()
                return produto_adicao_estoque, quantidade_adicionada
            else:
                print("Só há como adicionar quantidades maiores que 0! Tente novamente.")
                limpar_terminal()
                return
        except ValueError:
               print("❌ Só aceitamos números, tente novamente")
               limpar_terminal()
               return
    else:
        print("❌ Esse produto não está cadastrado.")
        limpar_terminal()
        return

def obter_saida_estoque():# Permite diminuir a quantidade de um produto
    produto_futuramente_subtracao_estoque = input("Qual produto você quer retirar quantidade?  ")
    produto_subtracao_estoque = procurar_produto_nalista(produto_futuramente_subtracao_estoque)
    if produto_subtracao_estoque is not None:
        try:
            quantidade_retirada = int(input(f"Quanto foi vendido de {produto_subtracao_estoque.nome}?  "))
            if quantidade_retirada > 0 and produto_subtracao_estoque.quantidade >= quantidade_retirada:
                print(f"A quantia foi retirada, agora há {produto_subtracao_estoque.quantidade} unidades de {produto_subtracao_estoque.nome}!")
                limpar_terminal()
                return produto_subtracao_estoque, quantidade_retirada
            else:
                print("Só há como adicionar quantidades maiores que 0 e menores que a quantidade inicial! Tente novamente.")
                limpar_terminal()
                return
        except ValueError:
            print("❌ Só aceitamos números, tente novamente")
            limpar_terminal()
            return
    else:
        print("❌ Esse produto não está cadastrado.")
        limpar_terminal()
        return

def obter_produto_editado():#Permite editar informações de um produto
    produto_futuramente_editado = input("Qual Produto deseja editar?  ")
    produto_editado = procurar_produto_nalista(produto_futuramente_editado)
    if produto_editado is not None:
        novo_nome = input("Qual nome deseja colocar nesse produto?  ").title().strip()
        if novo_nome is not None:
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
                    print("Seu produto foi editado!")
                    limpar_terminal()
                    return produto_editado, novo_nome, nova_quantidade, novo_preço_compra, novo_preço_venda
            except ValueError:
                print("❌ Só aceitamos números, tente novamente")
                limpar_terminal()
                return
        else:
            print('❌ O produto tem que ter um nome!')
            limpar_terminal()
            return
    else:
        print("❌ Esse produto não está cadastrado.")
        limpar_terminal()
        return

def escolha_filtrohistorico():#Escolhe o estilo do filtro
    print("Escolha o modo de filtro!\n" "1-Todo histórico\n" "2-Histórico de um produto")
    try:
        escolha = int(input("Qual opção deseja?  "))
        match escolha:
            case 1:
                if len(Histórico) > 0:
                    for registro in Histórico:
                        print(registro)
                    limpar_terminal()
                    return
                else:
                    print("Ainda não há histórico de mudanças de estoque")
                    limpar_terminal()
                    return
            case 2:
                procurar_historico_produto()
                limpar_terminal()
                return
            case _:
                print('❌ Sinal inválido, tente novamente!')
                limpar_terminal()
                return
    except ValueError:
        print("❌ Só aceitamos números, tente novamente")
        limpar_terminal()
        return    
    
def procurar_historico_produto(): #Procura o histórico do produto
    produto_busca = input("Qual Produto você deseja ver histórico?  ")
    produto = produto_busca.title()
    operacao = input("Digite + para entrada, - para saída ou / para os dois.  ").strip()
    match operacao:
        case '+' | '-' | '/' :
            mostrar_historico(produto, operacao)
        case _:
            print("❌ Só aceitamos os sinais, tente novamente")
            limpar_terminal()
            return
        
def mostrar_historico(produto, operação): #Mostra o estoque do produto e operação escolhida por usuário
    if len(Histórico) > 0:
        verificacao = None
        for registro in Histórico:
            if produto in  registro and (operação in registro or operação == '/'):
                print(registro)
                verificacao = True
        print("❌ Não há registro desse produto com essa operação") if verificacao is None else ''
        limpar_terminal()
        return
    else:
        print(" ❌Ainda não há histórico de mudanças de estoque")
        limpar_terminal()
        return