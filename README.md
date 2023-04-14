## Sumário

<ul>
    <li><a href="#kmdb-api">KMDB-API</a></li>
    <li><a href="##iniciando-a-aplicação">Iniciando a aplicação</a></li>
    <li><a href="#rodando-o-projeto">Rodando o projeto</a></li>
    <li>
        <a href="#endpoints">Endpoints</a>
        <ul>
            <li><a href="#post-apiusers">POST /api/users/</a></li>
            <li><a href="#post-apilogin">POST /api/login/</a></li>
            <li><a href="#get-apiusers">GET /api/users/</a></li>
            <li>
                <i>Criando usuário ADMIN via CLI</i>
                <ul>
                    <li><a href="#admin-padrão">Admin Padrão</a></li>
                    <li><a href="#admin-personalizado">Admin Personalizado</a></li>
                    <li><a href="#aviso">Possíveis Erros</a></li>
                </ul>
            </li>
            <li><a href="#get-apimovies">GET /api/movies/</a></li>
            <li><a href="#post-apimovies">POST /api/movies/</a></li>
        </ul>
    </li>
    <li><a href="#utilizando-o-django-admin-site">Utilizando o Django Admin Site</a></li>
</ul>

<br/><br/>

# KMDB-API

Uma API para gerenciamento de filmes e reviews.

<br/>

<h2 align="center">Iniciando a aplicação</h2>

<br/>

<p>Primeiro, é necessário criar um ambiente virtual para poder instalar os pacotes. Pode ser feito da seguinte forma no terminal aberto no diretório do projeto:</p>

<br/>

```Bash
python -m venv venv
```

> Obs: o segundo "venv" é o nome da pasta que deseja criar para a instalação dos pacotes, porém por boas práticas aconselhamos manter dessa forma!

<br/>

<p>Uma vez que a pasta já foi criada, basta rodar o seguinte comando para entrar o ambiente virtual</p>

<br/>

- Linux

```Bash
source venv/bin/activate
```

<br/>

- Windows

<p>Comando para verificação de entrada no ambiente virtual:</p>

```powershell
Get-ExecutionPolicy
```

<p>Caso o retorno seja "Restricted", basta inserir o seguinte código:</p>

```powershell
Set-ExecutionPolicy AllSigned
```

<p>Digite "S" ou "Y" para confirmar</p>

<br/>

<p>Após esse processo, basta inserir o seguinte comando:</p>

```powershell
.\venv\Scripts\activate
```

<br/>

> Obs: caso esteja utilizando o bash do Git, o comando para ativar o ambiente virtual é o seguinte:

<br/>

```Bash
source venv/Scripts/activate
```

<p>Agora que o ambiente virtual está criado e já entramos nele, basta rodar o seguinte comando para instalar as dependências:</p>

```Bash
pip intall -r requirements.txt
```

<br/>

<h2 align="center">Rodando o projeto</h2>

<p>Uma vez que as dependências do projeto foram instaladas de forma correta, para rodar o projeto localmente basta rodar o seguinte comando:</p>

```Bash
python manage.py runserver
```

<br/><br/>

## Endpoints

## `POST` /api/users/

Cria um novo usuário

<br/>
Parâmetros de requisição:

<ul>
    <li><strong>username:</strong> String</li>
    <li><strong>email:</strong> String</li>
    <li><strong>password:</strong> String</li>
    <li><strong>first_name:</strong> String</li>
    <li><strong>last_name:</strong> String</li>
    <li><strong>bio:</strong> Campo de texto</li>
    <li><strong>is_critic:</strong> Booleano</li>
</ul>

Retorno:

<ul>
    <li>status 200: Novo usuário criado com sucesso</li>
    <li>status 400: Dados não passaram pela validação</li>
</ul>

<br/>

Exemplo de requisição:

```json
POST api/users/ HTTP/1.1
Content-Type: application/json

{
    "username": "Igorttdp",
    "email": "igor@mail.com",
    "passoword": "123456",
    "first_name": "Igor",
    "last_name": "Torres",
    "bio": "Oi, meu nome é Igor :D",
    "is_critic": true
}
```

> O campo `is_critic`, caso true, referencia esse usuário como sendo um crítico de filmes. Um usuário `crítico` pode criar e publicar reviews dos filmes presentes no banco de dados da aplicação.

<br/>

Exemplo de resposta:

```json
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": "08a1f9f0-c0fd-435b-975f-0035b3749a8b",
    "username": "Igorttdp",
    "email": "igor@mail.com",
    "first_name": "Igor",
    "last_name": "Torres",
    "bio": "Sou o Igor :D",
    "is_critic": true,
    "is_superuser": false,
    "updated_at": "2023-04-13T20:20:38.765563Z"
}
```

## `POST` /api/login/

Retorna um token de acesso para o usuário.

<br/>

Parâmetros de requisição:

<ul>
    <li><strong>email</strong></li>
    <li><strong>password</strong></li>
</ul>

Retorno:

<ul>
    <li>status 200: Usuário autenticado com sucesso</li>
    <li>status 400: Dados não passaram pela validação</li>
    <li>status 401: Dados incorretos</li>
</ul>

<br/>

```json
POST /login HTTP/1.1
Content-Type: application/json

{
  "email": "igor@mail.com",
  "password": "123456"
}
```

<br/>

Exemplo de resposta:

```json
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MjAyMjc3NSwiaWF0IjoxNjgxNDE3OTc1LCJqdGkiOiJmNjEzYzYxMjlkMjg0YTgzYTNlOTgyZTY5ODAxY2M2MiIsInVzZXJfaWQiOiIwOGExZjlmMC1jMGZkLTQzNWItOTc1Zi0wMDM1YjM3NDlhOGIifQ.d3Qi4GPcr1xeSIS2kQDfwaivYm3KSpR6clu5K9vQr78",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxNTA0Mzc1LCJpYXQiOjE2ODE0MTc5NzUsImp0aSI6ImVlMGVmYTlhN2UzYjQ0ZmE4Yjk2ZTliZTJjNGE4Zjk2IiwidXNlcl9pZCI6IjA4YTFmOWYwLWMwZmQtNDM1Yi05NzVmLTAwMzViMzc0OWE4YiJ9.jmHLaBVYArfqoMLwbX10DiaElJPvF0B6_8qhhqglZ_8"
}
```

<h2 align="center">Rotas com autenticação</h2>

<p>Todas as rotas abaixo necessitam de autenticação. Deve ser configurada na requisição utilizando o token "access" de resposta em "/login".</p>

Inclua o token JWT em todas as requisições subsequentes no header `Authorization` utilizando o prefixo `Bearer`, como no exemplo abaixo:

```json
"Authorization": {
    "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxNTA0Mzc1LCJpYXQiOjE2ODE0MTc5NzUsImp0aSI6ImVlMGVmYTlhN2UzYjQ0ZmE4Yjk2ZTliZTJjNGE4Zjk2IiwidXNlcl9pZCI6IjA4YTFmOWYwLWMwZmQtNDM1Yi05NzVmLTAwMzViMzc0OWE4YiJ9.jmHLaBVYArfqoMLwbX10DiaElJPvF0B6_8qhhqglZ_8"
}
```

<br/>

## `GET` /api/users/

Retorna todos os usuários registrados no banco de dados desde que o token tenha permissão de `Administrador`.

> Só é possível criar um usuário administrador (super-usuário) por meio de um comando via CLI chamado "create_admin". Veja abaixo um exemplo

<br/>

<details id="admin-cli">

<summary>Criação de usuário admin via CLI</summary>

<br/>

### Admin Padrão

<br/>

Exemplo:

```bash
python manage.py create_admin
```

Resposta:

```bash
Admin `admin` successfully created!
```

> Nota: Os dados para logar são:
> <br/> username: admin
> <br/> password: admin1234

<br/>

### Admin Personalizado

<br/>

```bash
python manage.py create_admin --name Igor --email igor@mail.com --password senha1234
```

Resposta:

```bash
Admin `Igor` successfully created!
```

> Nota: Os atributos "--name", "--email" e "--password" são opcionais e se não forem passados, utilizarão os valores pré-definidos "name = Admin", "password = Admin1234" e "email = admin@mail.com > <br/>

## `Aviso`

Se o comando for enviado com dados repetidos, ele poderá retornar os seguintes erros:

```bash

Username `Admin` already taken.

#ou

Email `admin@mail.com` already taken.

```

</details>

<br/><br/>

Exemplo de resposta:

```json
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
	"count": 3,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": "209a1f71-6bed-422d-9448-1e57bab9c036",
			"username": "admin",
			"email": "admin@example.com",
			"first_name": "Admin",
			"last_name": "Adm",
			"bio": "Eu sou o admin",
			"is_critic": false,
			"is_superuser": true,
			"updated_at": "2023-04-13T20:41:20.786993Z"
		},
		{
			"id": "08a1f9f0-c0fd-435b-975f-0035b3749a8b",
			"username": "Igorttdp",
			"email": "igor@mail.com",
			"first_name": "Igor",
			"last_name": "Torres",
			"bio": "Sou o Igor :D",
			"is_critic": true,
			"is_superuser": false,
			"updated_at": "2023-04-13T20:20:38.765563Z"
		},
		{
			"id": "f9c08819-b9c1-457b-a8f3-0909225f0886",
			"username": "Rafael",
			"email": "",
			"first_name": "Rafael",
			"last_name": "Teixeira",
			"bio": "Olá, eu sou o Rafa!",
			"is_critic": false,
			"is_superuser": false,
			"updated_at": "2023-04-13T20:41:48.498022Z"
		}
	]
}
```

## `GET` /api/movies/

<br/>

Retorna uma lista contendo todos os filmes.

<br/>

Exmplo de Resposta:

```JSON
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "ee535837-83ce-4c72-bf85-16abcd99d97d",
            "genres": [
                {
                    "id": "e1589ff5-e015-4161-aacd-b665cb3153a3",
                    "name": "Action"
                },
                {
                    "id": "919d0ddb-0709-4e18-83e0-d7d204257fed",
                    "name": "Drama"
                }
            ],
            "title": "Jonh Wick 4",
            "duration": "03:00:00",
            "premiere": "2023-04-30",
            "budget": "20.00",
            "overview": "Jonh wick é um filme muito loko que no fim, depois de tomar tanto tiro ele se cansou e morreu. F"
        },
        {
            "id": "acbffdba-7630-4c26-8206-239a0b73530d",
            "genres": [
                {
                    "id": "e1589ff5-e015-4161-aacd-b665cb3153a3",
                    "name": "Action"
                },
                {
                    "id": "382479e4-bdf7-4b20-9d4d-7edc88b923d5",
                    "name": "Adventure"
                }
            ],
            "title": "Super Mario Bros. O Filme",
            "duration": "01:32:00",
            "premiere": "2023-04-13",
            "budget": "25.00",
            "overview": "Mario é um encanador junto com seu irmão Luigi. Um dia, eles vão parar no reino dos cogumelos, governado pela Princesa Peach, mas ameaçado pelo rei dos Koopas, que faz de tudo para conseguir reinar em todos os lugares."
        }
    ]
}
```

<br/>

## `POST` /api/movies/

Cria um novo filme.

<br/>

Exemplo de requisição:

```json
POST api/movies/ HTTP/1.1
Content-Type: application/json

{
    "title": "Jonh Wick 4",
    "duration": "03:00:00",
    "premiere": "2023-04-30",
    "budget": 20.00,
    "overview": "Com o preço por sua cabeça cada vez maior, o lendário assassino de aluguel John Wick leva sua luta contra o High Table global enquanto procura os jogadores mais poderosos do submundo, de Nova York a Paris, do Japão a Berlim.",
    "genres": ["Action", "Drama"],
}
```

> O campo genres deve ser uma lista de gêneros. Estes podem ser existentes ou não no banco de dados. Se o gênero não for existente, então ele será criado, caso contrário o gênero existente será referenciado no objeto de `Movie`.

<br/>

Exemplo de resposta:

```json
{
  "id": "ee535837-83ce-4c72-bf85-16abcd99d97d",
  "genres": [
    {
      "id": "e1589ff5-e015-4161-aacd-b665cb3153a3",
      "name": "Action"
    },
    {
      "id": "919d0ddb-0709-4e18-83e0-d7d204257fed",
      "name": "Drama"
    }
  ],
  "title": "Jonh Wick 4",
  "duration": "03:00:00",
  "premiere": "2023-04-30",
  "budget": "20.00",
  "overview": "Com o preço por sua cabeça cada vez maior, o lendário assassino de aluguel John Wick leva sua luta contra o High Table global enquanto procura os jogadores mais poderosos do submundo, de Nova York a Paris, do Japão a Berlim."
}
```

<br/><br>

## Utilizando o Django Admin Site

`Django Admin Site` é uma interface no frontend projetada para facilitar o gerenciamento de inserção e remoção de dados. Você pode utiliza-lá se tiver acesso de administrador.

<img src="./assets/djangoAdminSite.png" alt="Django Admin Site"/>

Para acessar, basta colocar as informações do usuário administrador e clicar em "Log In". Caso ainda não tenha criado um usuário admin, clique aqui: <a href="#admin-cli">Criação de usuário admin via CLI</a>.

<br/>

<img src="./assets/djangoAdmSiteOverview.png" alt="Django Admin Site Overview"/>

Aqui você tem acesso a todas as tabelas do banco de dados, assim como acesso a ações de criação e remoção de todos os dados!
