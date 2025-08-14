# Rede Social com Python

Uma API de rede social desenvolvida em **Python** seguindo princípios de **arquitetura limpa** e **camadas bem definidas**.

## 📂 Estrutura do Projeto

```
src/
│
├── api/                 # Camada de API (endpoints)
│   ├── dtos/             # Objetos de transferência de dados (Data Transfer Objects)
│   ├── exceptions/       # Exceções customizadas
│   └── routes/           # Rotas HTTP (FastAPI)
│
├── datalayer/            # Acesso a dados e modelos
│   └── models/           # Definições de entidades
│
├── services/             # Regras de negócio (services)
│
├── utils/                # Funções utilitárias
│
├── db.sqlite3            # Base de dados SQLite
├── requirements.txt      # Dependências do projeto
├── pyproject.toml        # Configuração do Poetry
└── dev.sh                # Script de desenvolvimento
```

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI** — Framework web rápido e moderno
* **SQLite** — Banco de dados leve
* **Pydantic** — Validação de dados
* **Poetry** — Gerenciador de dependências

## ⚙️ Instalação e Execução

1. **Clonar o repositório**

```bash
git clone https://github.com/SEU_USUARIO/rede-social-com-python.git
cd rede-social-com-python
```

2. **Criar ambiente virtual e instalar dependências**
   Se estiver usando Poetry:

```bash
poetry install
```

Ou usando pip:

```bash
pip install -r requirements.txt
```

3. **Executar a aplicação**

```bash
python src/dev.py
```

Ou:

```bash
./dev.sh
```

4. **Acessar a API**

* Documentação Swagger: `http://127.0.0.1:8000/docs`
* Documentação ReDoc: `http://127.0.0.1:8000/redoc`

## 📌 Funcionalidades

* Criar, listar e gerenciar usuários
* Criar, listar e gerenciar posts
* Autenticação e autorização
* Estrutura modular para fácil manutenção

