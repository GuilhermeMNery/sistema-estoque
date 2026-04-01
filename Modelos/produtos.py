class Produtos:
    def __init__(self, nome, quantidade, preço_de_compra, preço_de_venda):
        self._nome = nome
        self.quantidade = quantidade
        self._preço_de_compra = preço_de_compra
        self._preço_de_venda = preço_de_venda

    def __str__(self):
        alerta = " ⚠ ESTOQUE BAIXO" if self.quantidade < 3 else ""
        return f'Nome: {self.nome} - Quantidade: {self.quantidade} {alerta} - Preço: R${round(self._preço_de_venda, 2)} - Lucro: {self.calcular_margemde_lucro()}'
    
    def calcular_margemde_lucro(self):
        lucro = self._preço_de_venda - self._preço_de_compra
        margem_de_lucro = lucro / self._preço_de_compra * 100
        return f"O lucro por venda é de {lucro} tendo uma margem de {round(margem_de_lucro, 2)}%"

    @property
    def nome(self):
        return self._nome
    
    def to_dict(self):
        return {"Nome": self.nome, "Quantidade": self.quantidade, "Preço_compra": self._preço_de_compra, "Preço_venda": self._preço_de_venda}
    
    
