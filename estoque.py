from Modelos.produtos import Produtos
from Interface.menu import mostrar_menu
from Servicos.arquivo_service import carregar_dados


if __name__ == '__main__':
    Estoque, Histórico = carregar_dados()
    while True:
        mostrar_menu(Estoque, Histórico)





