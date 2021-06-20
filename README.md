# SSYS Employee Manager

Descrição para executar o projeto e utilizar a sua API


### Instalação


Na mesma pasta do arquivo docker-compose execute:
```
sudo docker-compose up --build
```
Esse comando vai criar os container e imagens docker e executar o projeto, que por sua vez poderá ser acessado na url local [http://localhost/](http://localhost/)


API para o CRUD:

* GET: http://localhost:8000/employees/ (employee list)
* POST: http://localhost:8000/employees/ (employee create)
* UPDATE http://localhost/employees/ID/ (employee update)
* DELETE http://localhost:8000/employees/ID/ (employee delete)
* GET  http://localhost:8000/employees/ID/ (employee detail)

API com relatórios:
* GET  http://localhost:8000/reports/employees/salary/ (salary report)
* GET  http://localhost:8000/reports/employees/age/ (age report)

API para autenticação:
* POST http://localhost:8000/api-token-auth/ (Post com o username e password a API retorna um token para acessar os demais endpoint)

O projeto em questão vai ser executado com o banco de dados sqlite3 ja com alguns dados cadastrados e o usuário ssysAdmin (senha: senhassys) para testes. 

Para acessar os endpoints é necessario autenticação via token, assim iniciamente para obter o token deve-se encaminhar uma requisição com o metodo http POST na url http://localhost:8000/api-token-auth/ com username e password no body. Exemplo:
* {
        "username": "ssysAdmin",
        "password": "senhassys"
} 

OBS:. O banco de dados ja tem um usuário que pode ser utilizado para teste caso desejado, as as credenciais 
        username: ssysAdmin e
        password: senhassys.
        
Com o token retornado na operação anterio pode-se acessar os demais endpoints encaminhando o token no header da requisição. Exemplo:
curl -X GET http://localhost:8000/employees/ -H 'Authorization: Token c05d9b6486e8d952c9dbc9cbe1dc488eab2091fe'

A mesma aplicação pode ser acessada em https://infinite-basin-92701.herokuapp.com/ com os mesmo endpoint citados anteriomente. A autenticação do usuario permanece igual e o mesmo usuario e senha de teste se encontra no banco de dados. Assim para realizar os mesmo teste é so trocar http://localhost:8000/employees/ por https://infinite-basin-92701.herokuapp.com/employees/. O mesmo vale para os demais endpoint.



## Executado com

* [Sqlite3] - Versão Docker e [PostgreSQL] na versão hospedada
* [Django](https://www.djangoproject.com/) - Framework usado em conjunto com o Django Rest Framework para criação de API's
* [Heroku] - Usado para deploy
* [Docker] - Usado para testes locais

## Autores

* **Deocleci dos Santos Dias** - *Desenvolvedor* 


