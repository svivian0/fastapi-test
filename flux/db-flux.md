# Fluxograma de Banco de Dados (Database ERD & Flow)

Este documento descreve o fluxo de criação e relacionamento do banco de dados para a aplicação, contendo as entidades de **Usuário**, **Pedido** e **Itens do Pedido**.

---

## 📊 Diagrama de Entidade-Relacionamento (ERD)

Abaixo está o modelo relacional em formato de diagrama Mermaid:

```mermaid
erDiagram
    USUARIO {
        int id PK "Autoincremento"
        string nome "Nome do usuário"
        string email UK "E-mail único para login"
        string senha_hash "Senha criptografada"
        datetime criado_em "Data de cadastro"
    }

    PEDIDO {
        int id PK "Autoincremento"
        int usuario_id FK "Chave Estrangeira -> USUARIO.id"
        string status "Ex: Pendente, Pago, Enviado, Cancelado"
        float total "Valor total do pedido"
        datetime criado_em "Data de criação do pedido"
    }

    ITEM_PEDIDO {
        int id PK "Autoincremento"
        int pedido_id FK "Chave Estrangeira -> PEDIDO.id"
        string produto "Nome do produto/serviço"
        int quantidade "Quantidade de itens"
        float preco_unitario "Preço por unidade"
    }

    USUARIO ||--o{ PEDIDO : "realiza (1:N)"
    PEDIDO ||--|{ ITEM_PEDIDO : "contém (1:N)"
```

---

## 🔄 Fluxo de Criação das Tabelas (Ordem de Dependência)

Para criar o banco de dados com chaves estrangeiras sem violar restrições de integridade referencial, a criação deve seguir o fluxo abaixo:

```mermaid
flowchart TD
    Start([Início da Criação]) --> TableUser[1. Criar Tabela 'USUARIO']
    TableUser --> TablePedido[2. Criar Tabela 'PEDIDO' <br> com FK para USUARIO]
    TablePedido --> TableItemPedido[3. Criar Tabela 'ITEM_PEDIDO' <br> com FK para PEDIDO]
    TableItemPedido --> End([Banco de Dados Pronto])

    style TableUser fill:#f9f,stroke:#333,stroke-width:2px
    style TablePedido fill:#bbf,stroke:#333,stroke-width:2px
    style TableItemPedido fill:#bfb,stroke:#333,stroke-width:2px
```

---

## 📝 Descrição das Tabelas e Atributos

### 1. Tabela: `usuario`
Armazena as informações cadastrais dos clientes/usuários.

| Campo | Tipo | Restrições | Descrição |
| :--- | :--- | :--- | :--- |
| `id` | `Integer` | Primary Key, Autoincrement | Identificador único do usuário. |
| `nome` | `String(150)` | Not Null | Nome completo do usuário. |
| `email` | `String(150)` | Not Null, Unique, Index | Endereço de e-mail (usado para login). |
| `senha_hash` | `String(255)` | Not Null | Hash da senha de segurança. |
| `criado_em` | `DateTime` | Not Null, Default `func.now()` | Timestamp de quando o registro foi criado. |

### 2. Tabela: `pedido`
Armazena o cabeçalho das compras feitas na plataforma.

| Campo | Tipo | Restrições | Descrição |
| :--- | :--- | :--- | :--- |
| `id` | `Integer` | Primary Key, Autoincrement | Identificador único do pedido. |
| `usuario_id` | `Integer` | Foreign Key (`usuario.id`), Not Null | Relaciona o pedido a um usuário específico. |
| `status` | `String(50)` | Not Null, Default `'pendente'` | Estado atual (ex: `pendente`, `pago`, `cancelado`). |
| `total` | `Float` | Not Null, Default `0.0` | Valor total acumulado do pedido. |
| `criado_em` | `DateTime` | Not Null, Default `func.now()` | Data e hora em que a compra foi iniciada. |

### 3. Tabela: `item_pedido`
Armazena as linhas de detalhes (produtos) que pertencem a cada pedido.

| Campo | Tipo | Restrições | Descrição |
| :--- | :--- | :--- | :--- |
| `id` | `Integer` | Primary Key, Autoincrement | Identificador único do item. |
| `pedido_id` | `Integer` | Foreign Key (`pedido.id`), Not Null | Relaciona o item a um pedido específico. |
| `produto` | `String(100)` | Not Null | Nome ou descrição do produto comprado. |
| `quantidade` | `Integer` | Not Null, Default `1` | Quantidade comprada desse produto. |
| `preco_unitario` | `Float` | Not Null | Preço de cada unidade do produto no momento da compra. |
