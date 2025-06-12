# Caipyra 2025 - Se virando com Docker

Aplicação de exemplo para criaçao das imagens Docker

## Requerimentos

- Python 3.12+
- FastAPI
- Redis SDK
- Virtual Environment
- pip
- pip-tools (Opcional)

## Quickstart

Crie um ambiente virtual

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Instale as dependências

```shell
$ pip install -r reqs/dev-requirements.txt -r reqs/requirements.txt
```

Rodando os testes

```shell
$ pytest
```

Rodando a aplicação em `localhost`

```shell
$ fastapi dev main.py
```
