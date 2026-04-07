import json
from datetime import datetime
import os
from Modelos.produtos import Produtos



def salvar_dados(): #Salva as mudanças no estoque no arquivo json
    with open("dados.json", "w", encoding= 'utf-8') as arquivo:
        json.dump([v.to_dict() for v in Estoque], arquivo, indent=4, ensure_ascii=False)

def adicionar_historico(registro_recebido):#Adiciona as modificações ao arquivo json
    registro = datetime.now()
    registro_formatado = f'{registro_recebido} às {registro.strftime("%H:%M")} do dia {registro.strftime("%d/%m/%Y")}'
    Histórico.append(registro_formatado)
    with open('historico.json', 'w', encoding='utf-8') as arquivo:
         json.dump([h for h in Histórico], arquivo, indent=4, ensure_ascii=False)

# USO DOS DADOS --------------------------------------------------------------------------

dados = [ ]
registro_hist = [ ]
if os.path.exists("dados.json"):
    with open("dados.json", "r", encoding="utf-8" ) as arquivo:
        dados = json.load(arquivo)
if os.path.exists('historico.json'):
     with open("historico.json", "r", encoding="utf-8" ) as arquivo2:
        registro_hist = json.load(arquivo2)

Histórico = [r for r in registro_hist]
Estoque = [Produtos(d["Nome"], d["Quantidade"], d["Preço_compra"], d["Preço_venda"]) for d in dados]