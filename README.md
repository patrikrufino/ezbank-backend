# API de Sistema Bancário

Esta é uma API simples de sistema bancário que permite realizar operações básicas, como criar contas, realizar depósitos, saques e transferências. Foi desenvolvida utilizando Python e Flask como framework web, e o banco de dados SQLite para armazenar os dados das contas.

## Requisitos

Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

- Python (versão 3.6 ou superior)
- Flask (instalado via pip)

## Instalação e Execução

Siga as etapas abaixo para instalar e executar a API:

1. Faça o clone deste repositório em sua máquina:

```
git clone <URL do repositório>
```

2. Acesse o diretório do projeto:

```
cd ezbank-backend
```

3. Crie e ative um ambiente virtual:

```
python -m venv venv
```

- Para Windows:
```
venv\Scripts\activate
```

- Para macOS/Linux:
```
source venv/bin/activate
```

4. Instale as dependências do projeto:

```
pip install -r requirements.txt
```

5. Execute a aplicação:

```
python app.py
```

A API estará disponível em `http://localhost:5000`.

## Endpoints

A API possui os seguintes endpoints disponíveis:

- `GET /users`: Retorna a lista de usuários cadastrados.
- `POST /users`: Cria um novo usuário.
- `GET /users/<int:user_id>`: Retorna os detalhes de um usuário específico.
- `PUT /users/<int:user_id>`: Atualiza os dados de um usuário específico.
- `DELETE /users/<int:user_id>`: Remove um usuário específico.
- `GET /contas`: Retorna a lista de contas cadastradas.
- `POST /contas`: Cria uma nova conta.
- `GET /contas/<int:conta_id>`: Retorna os detalhes de uma conta específica.
- `PUT /contas/<int:conta_id>`: Atualiza os dados de uma conta específica.
- `DELETE /contas/<int:conta_id>`: Remove uma conta específica.
- `POST /contas/<int:conta_id>/depositar`: Realiza um depósito em uma conta específica.
- `POST /contas/<int:conta_id>/sacar`: Realiza um saque em uma conta específica.
- `POST /contas/<int:conta_origem_id>/transferir/<int:conta_destino_id>`: Realiza uma transferência entre duas contas.

## Exemplos de Uso

- Criar um usuário:

```
POST /users
Body:
{
  "nome": "João",
  "senha": "senha123"
}
```

- Criar uma conta:

```
POST /contas
Body:
{
  "numero": "123456",
  "saldo": 1000.0,
  "limite": 5000.0,
  "usuario_id": 1
}
```

- Realizar um depósito:

```
POST /contas/1/depositar
Body:
{
  "valor": 500.0
}
```

- Realizar um saque:

```
POST /contas/1/sacar
Body:
{
  "valor": 200.0
}
```

- Realizar

 uma transferência:

```
POST /contas/1/transferir/2
Body:
{
  "valor": 300.0
}
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias, correções de bugs ou novos recursos.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).