# 📦 Sistema de Estoque | Inventory System

> Sistema de controle de estoque via terminal desenvolvido em Python.
> Terminal-based inventory control system developed in Python.

---

## 🇧🇷 Português

### 📋 Sobre o Projeto

Sistema de gerenciamento de estoque que permite cadastrar, editar, excluir produtos e controlar entradas e saídas de estoque, com histórico de movimentações e persistência de dados em JSON.


### ✨ Funcionalidades

- ✅ Listar produtos com alerta de estoque baixo
- ✅ Cadastrar produtos com preço de compra e venda
- ✅ Excluir produtos
- ✅ Entrada e saída de estoque
- ✅ Editar informações de produtos
- ✅ Histórico de movimentações com data e hora
- ✅ Filtro de histórico por produto e tipo de operação
- ✅ Persistência de dados em arquivos JSON
- ✅ Cálculo automático de margem de lucro

### 🗂️ Estrutura do Projeto

```
sistema-estoque/
├── estoque.py              # Ponto de entrada da aplicação
├── Modelos/
│   └── produtos.py         # Classe Produtos
├── Servicos/
│   ├── estoque_service.py  # Lógica de negócio
│   └── arquivo_service.py  # Persistência em JSON
└── Interface/
    └── menu.py             # Interface com o usuário
```

### 🚀 Como Executar

**Pré-requisitos:** Python 3.10 ou superior

```bash
# Clone o repositório
git clone https://github.com/GuilhermeMNery/sistema-estoque.git

# Entre na pasta
cd sistema-estoque

# Execute
python estoque.py
```

### 🛠️ Tecnologias

- Python 3.10+
- JSON (persistência de dados)
- Módulos nativos: `os`, `json`, `datetime`

---

## 🇺🇸 English

### 📋 About

A terminal-based inventory management system that allows registering, editing and deleting products, controlling stock entries and exits, with a movement history and JSON data persistence.


### ✨ Features

- ✅ List products with low stock alerts
- ✅ Register products with purchase and sale price
- ✅ Delete products
- ✅ Stock entries and exits
- ✅ Edit product information
- ✅ Movement history with date and time
- ✅ History filter by product and operation type
- ✅ Data persistence in JSON files
- ✅ Automatic profit margin calculation

### 🗂️ Project Structure

```
sistema-estoque/
├── estoque.py              # Application entry point
├── Modelos/
│   └── produtos.py         # Products class
├── Servicos/
│   ├── estoque_service.py  # Business logic
│   └── arquivo_service.py  # JSON persistence
└── Interface/
    └── menu.py             # User interface
```

### 🚀 How to Run

**Requirements:** Python 3.10 or higher

```bash
# Clone the repository
git clone https://github.com/GuilhermeMNery/sistema-estoque.git

# Enter the folder
cd sistema-estoque

# Run
python estoque.py
```

### 🛠️ Tech Stack

- Python 3.10+
- JSON (data persistence)
- Native modules: `os`, `json`, `datetime`

---

## 👤 Autor | Author

**Guilherme Nery**

[![GitHub](https://img.shields.io/badge/GitHub-GuilhermeMNery-181717?style=flat&logo=github)](https://github.com/GuilhermeMNery)
