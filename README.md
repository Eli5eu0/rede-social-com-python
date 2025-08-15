# 📱 Rede Social com Python

Uma aplicação de rede social desenvolvida em Python, estruturada com módulos para API, serviços, camadas de dados, autenticação e configuração.

## 📂 Estrutura do Projeto

```
src/
│
├── api/
│   ├── dtos/
│   │   ├── posts.py
│   │   └── users.py
│   ├── exceptions/
│   │   └── user.py
│   └── routes/
│       ├── home.py
│       ├── post.py
│       ├── users.py
│       ├── application.py
│       ├── authentication.py
│       └── configuration.py
│
├── datalayer/
│   ├── models/
│   │   ├── base.py
│   │   ├── post.py
│   │   └── user.py
│
├── services/
│   ├── post.py
│   └── user.py
│
├── utils/
│
├── db.sqlite3
├── dev.py
├── dev.sh
├── pyproject.toml
├── poetry.lock
├── requirements.txt
└── TODO.md
```

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI** — Framework web rápido e moderno
* **SQLite** — Banco de dados leve
* **Pydantic** — Validação de dados
* **Poetry** — Gerenciador de dependências

## ⚙️ Instalação e Execução

1️. **Clonar o repositório**

```bash
git clone https://github.com/Eli5eu0/rede-social-com-python.git
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
## 💻 Executar o projeto

### Ambiente de desenvolvimento

```bash
task dev
```

### Ambiente de produção

```bash
task prod
```

### Acessar a API

* Documentação Swagger: `http://127.0.0.1:8000/docs`
* Documentação ReDoc: `http://127.0.0.1:8000/redoc`

## 📌 Funcionalidades

* Criar, listar e gerenciar usuários
* Criar, listar e gerenciar posts
* Autenticação e autorização
* Estrutura modular para fácil manutenção

## 📜 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.
