# Projeto de Teste e Aprendizado - FastAPI, Uvicorn & SQLAlchemy

Este repositório contém um projeto de teste e aprendizado desenvolvido para fins de estudo e experimentação com o ecossistema **FastAPI**, **Uvicorn** e **SQLAlchemy**. O objetivo principal é construir uma **REST API** robusta, performática e bem estruturada, aplicando boas práticas de desenvolvimento de software.

## 🚀 Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/):** Framework web moderno, rápido (de alto desempenho) para construir APIs com Python 3.8+ baseado em type hints padrões do Python.
- **[Uvicorn](https://www.uvicorn.org/):** Servidor web ASGI de alta performance para Python, responsável por rodar a aplicação FastAPI.
- **[SQLAlchemy](https://www.sqlalchemy.org/):** O principal kit de ferramentas SQL para Python e Mapeador Objeto-Relacional (ORM), utilizado para interagir de forma eficiente com o banco de dados.

---

## 📁 Estrutura do Projeto

A estrutura de diretórios foi pensada para manter a separação de responsabilidades e permitir a escalabilidade da aplicação:

```text
FastAPI/
├── src/
│   ├── main.py                # Ponto de entrada da aplicação FastAPI
│   └── routes/                # Definição das rotas (APIRouter) da API
│       ├── auth_routes.py     # Endpoints relacionados à autenticação
│       └── order_routes.py    # Endpoints relacionados aos pedidos (orders)
├── .gitignore                 # Arquivo de configuração para ignorar arquivos no Git
└── README.md                  # Este arquivo de documentação
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
pip install fastapi uvicorn sqlalchemy
```
*(Nota: Recomenda-se também a instalação de um driver de banco de dados apropriado, como `psycopg2` para PostgreSQL ou usar o padrão `sqlite` integrado).*

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

## 🎯 Próximos Passos (Estudos)

Para expandir este projeto de aprendizado, os seguintes tópicos estão planejados:
1. **Configuração do Banco de Dados com SQLAlchemy:** Implementar a conexão com o banco de dados, definição da engine e do `sessionmaker`.
2. **Criação de Modelos (Models):** Definir as tabelas de banco de dados (ex: `User`, `Order`) usando a base declarativa do SQLAlchemy.
3. **Esquemas com Pydantic (Schemas/Serializers):** Utilizar Pydantic para validação e serialização de dados de entrada e saída.
4. **Operações de CRUD:** Implementar a criação, leitura, atualização e exclusão de registros no banco de dados.
5. **Autenticação e Segurança:** Implementar segurança com JWT (JSON Web Tokens) e hash de senhas de usuários.
6. **Migrações com Alembic:** Gerenciar o versionamento do banco de dados.
