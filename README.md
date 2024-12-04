# Aplicação: cadastro de Vingadores

Esta aplicação fará o cadastro de vingadores, com nome, nome real, poderes, fraquezas, força e será utilizado para praticar a criação de uma aplicação backend com Python, MySQL e Flask.

Para clonar o repositório, execute o passo a passo descrito aqui: [CLONEME.md](docs/CLONEME.md).

Para visualizar a demostração do método fetchall() do objeto cursor, execute o passo a passo descrito aqui: [FETCHALL.md](docs/FETCHALL.md).

# Conectando nossa aplicação com o banco de dados

**1º passo**: Criaremos um ambiente virtual para instalar as dependências do projeto, impedindo que as mesmas sejam instaladas globalmente e interfiram em outros projetos. Podemos criar esse ambiente virtual no VS Code da seguinte forma:

1. Com um arquivo Python aberto (.py), clique na informação de ambiente (número da versão do Python) no canto inferior direito do VS Code;
2. Clique em "Criar ambiente virtual";
3. Em "Selecionar tipo de ambiente Python" escolha "venv";
4. Selecione a instalação do Python que deseja utilizar;
5. Aguarde a criação do ambiente virtual.
6. Após a criação do ambiente virtual, clique novamente na informação de ambiente e selecione o ambiente criado.
7. Abra o terminal do Powershell no VS Code. 
8. Para ativar o ambiente virtual, primeiro mude a política de execução do Powershell com o comando: 
```bash
Set-ExecutionPolicy Bypass -Scope Process
```
9. Em seguida execute o script de ativação com o comando:
```bash
.\.venv\Scripts\Activate.ps1`
```

**2º passo**: Para conectar nossa aplicação com o banco de dados, utilizaremos o MySQL. Para isso, precisamos instalar uma dependência, o pacote `mysql-connector-python`:

```bash
pip install mysql-connector-python
```

**3º passo**: Para proteger nossas credenciais de acesso ao banco de dados, criaremos um arquivo `.env` na raiz do projeto. Esse arquivo conterá as variáveis de ambiente que serão utilizadas para conectar a aplicação ao banco de dados. Precisamos, então, instalar a dependência `python-dotenv`:

```bash
pip install python-dotenv
```

**4º passo**: Criaremos um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
BD_HOST = 'localhost' # host do banco de dados
BD_USER = '' # usuário do banco de dados
BD_PSWD = '' # senha do banco de dados
BD_DATABASE = 'vingadores' # nome do banco de dados
```

Adicionalmente, crie um arquivo `.env.example` com as variáveis de ambiente, mas sem os valores, e adicione-o ao repositório. Assim, os colaboradores do projeto poderão copiar o arquivo `.env.example` e criar o arquivo `.env` com suas próprias credenciais. 

**5º passo**: Para utilizar as variáveis de ambiente do arquivo `.env`, precisamos importar a biblioteca `dotenv` e carregar as variáveis de ambiente no arquivo `app.py`:

```python
from dotenv import load_dotenv
load_dotenv() # carrega as variáveis de ambiente do arquivo .env
```

Você poderá acessar as variáveis de ambiente do arquivo `.env` da seguinte forma:

```python
from os import getenv
getenv('BD_HOST')
getenv('BD_USER')
getenv('BD_PSWD')
getenv('BD_DATABASE')
```

**IMPORTANTE**: O arquivo `.env` não deve ser versionado. Para isso, crie um arquivo `.gitignore` na raiz do projeto e adicione o arquivo `*.env` nele. Adicione também os diretórios `__pycache__` e `.venv` ao arquivo `.gitignore`.
