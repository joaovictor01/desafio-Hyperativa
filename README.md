# Desafio Hyperativa

Para rodar a API será necessário ter `docker` e `docker-compose` instalados.

_Deixei o .env no git como não é uma aplicação real em produção, para facilitar quando forem rodar._

## Uso

```bash
docker-compose up --build
```

### API

A API foi feita utilizando o django-rest-framework, com autenticação via token JWT utilizando Simple-JWT.

**Registro de usuário**

```bash
curl --request POST \
  --url http://localhost:8000/api/users/register/ \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/9.3.2' \
  --data '{
    "username": "test",
		"email": "test1@email.com",
    "password": "test"
}'
```

**Login**

```bash
curl --request POST \
  --url http://localhost:8000/api/users/login/ \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/9.3.2' \
  --data '{
    "username": "test",
    "password": "test"
}'
```

**Adicionar um cartão**

```bash
curl --request POST \
  --url http://localhost:8000/api/cards/add/ \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyMjI4NjA5LCJpYXQiOjE3MjIyMjUwMDksImp0aSI6ImM4MzZhYzkzNThjMzQ4MDc5ZTZmYjkwMWE1NmU4N2Y1IiwidXNlcl9pZCI6MX0.YlZ0JNqQlJ2X07JT9LXLS2g75YONa_v7Fo3OG76oDWg' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/9.3.2' \
  --data '{
	"name": "testcard",
	"card_number": "4456897999999991"
}'
```

**Adicionar um arquivo em lotes de cartões**

```bash
curl --request POST \
  --url http://localhost:8000/api/cards/batch/ \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyMjI1NzE1LCJpYXQiOjE3MjIyMjIxMTUsImp0aSI6IjUxYzc3YWNmNzM1NDQ4MGQ5ZTY4ZDRlYTczZWExMDdkIiwidXNlcl9pZCI6MX0.ltvZAVLnkNcAKpOng1gprxNvnvVRm4yGg9e2-LH6Wv0' \
  --header 'Content-Disposition: attachment; filename=cards_batch.txt' \
  --header 'Content-Type: multipart/form-data' \
  --header 'User-Agent: insomnia/9.3.2' \
  --form file=@/home/joaovictor/code/cards_batch_example.txt
```

**Obter id do cartão pelo número**

```bash
curl --request GET \
  --url 'http://localhost:8000/api/cards/get_by_number/4456897999999991?=' \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyMjI1NzE1LCJpYXQiOjE3MjIyMjIxMTUsImp0aSI6IjUxYzc3YWNmNzM1NDQ4MGQ5ZTY4ZDRlYTczZWExMDdkIiwidXNlcl9pZCI6MX0.ltvZAVLnkNcAKpOng1gprxNvnvVRm4yGg9e2-LH6Wv0' \
  --header 'User-Agent: insomnia/9.3.2'
```

## Testes

Para rodar os testes unitários, use o comando:

```bash
docker-compose run web pytest
```

## Teste com Insomnia

Importe o arquivo `insomnia_collection.json` no `Insomnia` para utilizar algumas requisições já configuradas.
