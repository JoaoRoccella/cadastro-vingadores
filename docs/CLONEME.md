# Clonando seu repositório do projeto

Para clonar o repositório do projeto, você deve ter o Git instalado em sua máquina. Caso não tenha, você pode baixá-lo aqui: <https://git-scm.com/downloads>.

Com o Git instalado, abra o terminal do Git (Git Bash) e execute o seguinte comando:

```bash
git clone <url-do-repositorio> <nome-da-pasta-opcional> 
```

Substitua `<url-do-repositorio>` pela URL do repositório do projeto e `<nome-da-pasta-opcional>` pelo nome da pasta que você deseja que o repositório seja clonado. Caso você não informe o nome da pasta, o repositório será clonado na pasta atual e será criada uma pasta com o mesmo nome do repositório. 

Após clonar o repositório, você terá uma pasta com o nome do repositório na pasta em que você executou o comando. Para acessar a pasta do projeto, execute o comando:

```bash
code -r <nome-da-pasta>
```

Substitua `<nome-da-pasta>` pelo nome da pasta do repositório.

Pronto! Agora você tem o repositório do projeto clonado em sua máquina e pode começar a trabalhar no projeto. Caso você queira utilizar a interface gráfica do Git, você pode instalar o [GitHub Desktop](https://desktop.github.com/) ou clonar o repositório diretamente pelo Visual Studio Code.

## Porque é importante utilizar o Git e o GitHub?

O Git é uma ferramenta de controle de versão que permite que você mantenha um histórico de todas as alterações feitas em um projeto. Isso é importante para que você possa acompanhar o desenvolvimento do projeto e, caso algo dê errado, você possa voltar para uma versão anterior do projeto. Já o GitHub é uma plataforma que permite que você hospede seus repositórios de forma gratuita e compartilhe seu código com outras pessoas. Além disso, o GitHub oferece diversas ferramentas que facilitam o trabalho em equipe, como issues, pull requests e projetos.

Caso você deseje prosseguir na carreira de desenvolvimento de software, é essencial que você aprenda a utilizar o Git e o GitHub, pois essas são ferramentas amplamente utilizadas no mercado de trabalho. Além disso, o Git e o GitHub são ferramentas poderosas que podem te ajudar a se tornar um desenvolvedor mais eficiente e produtivo. É o arroz com feijão do desenvolvedor!

## Após clonar o repositório

Após clonar o repositório, você deve seguir os passos abaixo para configurar o ambiente de desenvolvimento do projeto.

### Criação do ambiente virtual

Um ambiente virtual é uma ferramenta que permite que você crie um ambiente isolado para cada projeto, evitando conflitos entre as dependências dos projetos. Siga os passos abaixo para criar um ambiente virtual para o projeto:

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

9. Em seguida execute o script de ativação em um terminal do PowerShell com o comando:

    ```bash
    .\.venv\Scripts\Activate.ps1`
    ```
### Instalação das dependências do projeto

Depois de criar o ambiente virtual, você deve instalar as dependências do projeto. Você pode fazer isso utilizando o `pip`, que é o gerenciador de pacotes do Python. Manualmente, você pode instalar as dependências do projeto executando o seguinte comando:

```bash
pip install <nome-da-dependencia>
```

Caso você tenha o arquivo `requirements.txt` no repositório, você pode instalar todas as dependências do projeto de uma vez só, executando o seguinte comando:

```bash
pip install -r requirements.txt
```

Esse comando irá instalar todas as dependências do projeto que estão listadas no arquivo `requirements.txt`. Caso você ainda não tenha o Python instalado em sua máquina, você pode baixá-lo aqui: <https://www.python.org/downloads/>.

#### Como criar o arquivo `requirements.txt`

Para criar o arquivo `requirements.txt`, você deve executar o seguinte comando no terminal após instalar todas as dependências do projeto:

```bash
pip freeze > requirements.txt
```

Isso irá criar um arquivo `requirements.txt` na raiz do projeto com todas as dependências do projeto e suas versões. Esse arquivo é útil para que você ou outras pessoas possam instalar as dependências do projeto de uma vez só nas próximas vezes que clonarem o repositório. Você deve, portanto, versionar o arquivo `requirements.txt` no repositório.

### Configuração do arquivo `.env`

Para proteger suas credenciais de acesso ao banco de dados, você deve criar um arquivo `.env` na raiz do projeto. Esse arquivo conterá as variáveis de ambiente que serão utilizadas para conectar a aplicação ao banco de dados. Siga os passos abaixo para configurar o arquivo `.env`:

1. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

    ```env
    BD_HOST = '' # endereço do host do banco de dados
    BD_USER = '' # usuário do banco de dados
    BD_PSWD = '' # senha do banco de dados
    BD_DATABASE = '' # nome do banco de dados (schema)
    ```

2. Adicionalmente, crie um arquivo `.env.example` com as variáveis de ambiente, mas sem os valores, e adicione-o ao repositório. Assim, os colaboradores do projeto poderão copiar o arquivo `.env.example` e criar o arquivo `.env` com suas próprias credenciais. Caso já exista um arquivo `.env.example` no repositório, você pode copiá-lo e renomeá-lo para `.env`.

## Banco de dados

Para conectar nossa aplicação com o banco de dados, utilizaremos o MySQL. Você deve instalar o MySQL em sua máquina e criar um banco de dados para a aplicação. Caso você não tenha o MySQL instalado em sua máquina, você pode baixá-lo aqui: <https://dev.mysql.com/downloads/mysql/>.

Após instalar o MySQL, você deve criar um banco de dados para a aplicação importando o arquivo `vingadores.sql` que você exportou do MySQL Workbench. Para importar o arquivo `vingadores.sql`, você pode executar o seguinte comando no terminal do Prompt de Comando (CMD):

```bash
mysql -u <usuario> -p <nome-do-banco> < .\data\vingadores.sql
```

Ou, no terminal do PowerShell:

```bash
Get-Content .\data\vingadores.sql -Raw | & mysql -u <usuario> -p
```

Verifique se o seu arquivo `vingadores.sql` está na pasta `data` do projeto. Substitua `<usuario>` pelo usuário do MySQL e `<nome-do-banco>` pelo nome do banco de dados que você deseja importar o arquivo `vingadores.sql` (**somente informe o nome do banco de dados se o arquivo `vingadores.sql` não contiver a instrução `CREATE DATABASE`**).

Se preferir, você pode importar o arquivo `vingadores.sql` utilizando o MySQL Workbench. Para isso, abra o MySQL Workbench, conecte-se ao seu servidor MySQL e clique em `File > Run SQL Script...`. Selecione o arquivo `vingadores.sql` e clique em `Run`.