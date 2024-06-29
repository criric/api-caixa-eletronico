# API de Simulação de Caixa Eletrônico

Esta API simula o funcionamento de um caixa eletrônico. Ela recebe um valor de saque desejado e retorna a quantidade de cédulas de cada valor necessárias para compor esse saque, utilizando a menor quantidade de cédulas possível. As cédulas consideradas são: 100, 50, 20, 10, 5 e 2.

## Requisitos

- Python 3.6+
- Flask

## Instalação

1. Clone o repositório:
    ```sh
    git clone <url-do-repositorio>
    cd <nome-do-repositorio>
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    venv\Scripts\activate  # No Windows
    source venv/bin/activate  # No macOS/Linux
    ```

3. Instale as dependências:
    ```sh
    pip install Flask
    ```

## Uso

1. Execute o servidor Flask:
    ```sh
    python app.py
    ```

2. Acesse o endpoint `/api/saque` para realizar um saque. Use um cliente HTTP como Postman ou `curl`.

### Exemplo de Requisição com `curl`

```sh
curl -X POST -H "Content-Type: application/json" -d '{"valor": 380}' http://127.0.0.1:5000/api/saque
```

## Testes

1. Para executar os testes, use o comando:
```sh
python test_app.py
```
