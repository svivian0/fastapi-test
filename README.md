# Projeto de Teste e Aprendizado - FastAPI, Uvicorn & SQLAlchemy

Este repositório contém um projeto de teste e aprendizado desenvolvido para fins de estudo e experimentação com o ecossistema **FastAPI**, **Uvicorn**, **SQLAlchemy** e **Alembic**. O objetivo principal é construir uma **REST API** robusta, performática e bem estruturada, aplicando boas práticas de desenvolvimento de software.

## 🚀 Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/):** Framework web moderno e rápido para construir APIs com Python baseado em type hints padrões do Python.
- **[Uvicorn](https://www.uvicorn.org/):** Servidor web ASGI de alta performance para Python, responsável por rodar a aplicação FastAPI.
- **[SQLAlchemy](https://www.sqlalchemy.org/):** Mapeador Objeto-Relacional (ORM) utilizado para interagir de forma eficiente com o banco de dados.
- **[SQLAlchemy-Utils](https://sqlalchemy-utils.readthedocs.io/):** Utilitários adicionais para SQLAlchemy (utilizado para o tipo de dados `ChoiceType`).
- **[Alembic](https://alembic.sqlalchemy.org/):** Ferramenta de migração de banco de dados leve para uso com o SQLAlchemy, responsável pelo versionamento do esquema de banco de dados.

---

## 📁 Estrutura do Projeto

A estrutura de diretórios foi pensada para manter a separação de responsabilidades e permitir a escalabilidade da aplicação:

```text
FastAPI/
├── alembic/                  # Arquivos e scripts de migração do Alembic
│   ├── env.py                # Script de configuração do ambiente de migração
│   └── versions/             # Histórico dos arquivos de migração gerados
├── data/                     # Diretório de dados local (ignorado no Git)
│   └── database.db           # Arquivo do banco de dados SQLite
├── flux/                     # Diagramas e fluxogramas do projeto
│   └── db-flux.md            # Diagrama ERD e fluxo das tabelas do banco de dados
├── src/
│   ├── main.py               # Ponto de entrada da aplicação FastAPI
│   ├── models.py             # Definição dos modelos SQLAlchemy (Users, Orders, Items)
│   └── routes/               # Definição das rotas (APIRouter) da API
│       ├── auth_routes.py    # Endpoints relacionados à autenticação
│       └── order_routes.py   # Endpoints relacionados aos pedidos (orders)
├── .gitignore                # Arquivo para ignorar arquivos/pastas no Git (como alembic.ini e data/)
├── alembic.ini               # Arquivo de configuração global do Alembic (ignorado no Git)
└── README.md                 # Este arquivo de documentação
```

---

## 🛠️ Instalação e Execução

### 1. Configurar o Ambiente Virtual (Recomendado)
Crie e ative um ambiente virtual para isolar as dependências do projeto:

**No Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**No Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar as Dependências
Instale as dependências necessárias para rodar o projeto:
```bash
pip install fastapi uvicorn sqlalchemy sqlalchemy-utils alembic
```

### 3. Executar o Servidor de Desenvolvimento
Para rodar a aplicação com recarregamento automático (auto-reload) durante o desenvolvimento:

**A partir do diretório raiz (`FastAPI`):**
```bash
python -m uvicorn src.main:app --reload
```

**Ou, se estiver dentro da pasta `src`:**
```bash
cd src
python -m uvicorn main:app --reload
```

A aplicação estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 💾 Banco de Dados & Migrações (Alembic)

O banco de dados do projeto utiliza **SQLite** e as migrações são gerenciadas pelo **Alembic**.

### Ordem de Execução das Migrações

O banco é estruturado com relacionamentos entre **Usuários**, **Pedidos** e **Itens do Pedido**. Os diagramas detalhados das tabelas e do fluxo de criação podem ser visualizados no arquivo [db-flux.md](file:///c:/Users/vivia/OneDrive/Documentos/FastAPI/flux/db-flux.md).

### Comandos Úteis do Alembic

Caso a chamada direta do comando `alembic` falhe no Windows (erro de comando não encontrado), execute sempre utilizando o prefixo `python -m alembic`:

* **Gerar uma nova migração automaticamente** (baseando-se nas alterações do arquivo `models.py`):
  ```bash
  python -m alembic revision --autogenerate -m "Criar tabelas iniciais"
  ```

* **Aplicar as migrações no banco de dados** (atualizar o banco de dados para a última versão):
  ```bash
  python -m alembic upgrade head
  ```

* **Desfazer a última migração aplicada**:
  ```bash
  python -m alembic downgrade -1
  ```

---

## 📖 Documentação Interativa da API

O FastAPI gera automaticamente duas interfaces de documentação interativa para a API:

- **Swagger UI:** Disponível em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (permite testar os endpoints diretamente no navegador).
- **ReDoc:** Disponível em [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) (documentação técnica limpa e detalhada).

---

## 🗺️ Endpoints Atuais

### 🔑 Autenticação (`/auth`)
*Arquivo correspondente: [auth_routes.py](file:///c:/Users/vivia/OneDrive/Documentos/FastAPI/src/routes/auth_routes.py)*
- `GET /auth/`: Endpoint padrão para autenticação de usuários.

### 📦 Pedidos (`/order`)
*Arquivo correspondente: [order_routes.py](file:///c:/Users/vivia/OneDrive/Documentos/FastAPI/src/routes/order_routes.py)*
- `GET /order/`: Endpoint padrão para listagem de pedidos.

---

## Base
Esse projeto está usando como base o curso gratuito no youtube da [Hashtag Programação](https://www.youtube.com/@HashtagProgramacao) sobre FastAPI, link do curso - [fastapi](https://www.youtube.com/watch?v=kI8uXm0W9eU&t=845s)
