# Demonstração do método fetchall() em Python

Um dos pontos-chave dessa demonstração é compreender que os dados de uma tabela de um banco de dados são **carregados em memória** para serem manipulados pelo programa. O método `fetchall()` é utilizado para **retornar todos os registros** de uma consulta ao banco de dados. Esses registros são retornados em uma **lista de tuplas**, onde cada tupla representa um registro da tabela.

Para demonstrar o método `fetchall()`, vamos criar uma tabela simples de vingadores e inserir alguns registros. Em seguida, vamos criar um método na classe `Database` para executar uma query e retornar todos os registros da tabela. Por fim, vamos carregar os dados dos herois em memória como objetos da classe `Vingador` e exibir os registros na tela.

Vamos começar criando uma tabela simples de vingadores, chamada `heroi`, com os seguintes campos:

```sql
CREATE TABLE `heroi` (
  `heroi_id` int NOT NULL AUTO_INCREMENT,
  `nome_heroi` varchar(45) DEFAULT NULL,
  `nome_real` varchar(45) DEFAULT NULL,
  `categoria` varchar(45) DEFAULT NULL,
  `poderes` varchar(45) DEFAULT NULL,
  `poder_principal` varchar(45) DEFAULT NULL,
  `fraquezas` varchar(45) DEFAULT NULL,
  `nivel_forca` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`heroi_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

> Note que a tabela não se preocupa com os tipos de dados, apenas com a estrutura, para simplificar a demonstração. Esta tabela também não se procupa em fornecer dados da convocação, da tornozeleira eletrônica e do chip de localização, que **deverão ser modeladas por você no seu projeto** com a correta cardinalidade e relacionamento com a tabela `heroi`.

Agora, podemos inserir alguns dados na tabela:

```sql
INSERT INTO `heroi` (`nome_heroi`, `nome_real`, `categoria`, `poderes`, `poder_principal`, `fraquezas`, `nivel_forca`) VALUES
('Homem de Ferro', 'Tony Stark', 'Humano', 'Inteligência, Tecnologia', 'Armadura', 'Arrogância', '100'),
('Thor', 'Thor', 'Deidade', 'Força, Relâmpagos, Mjolnir', 'Rompe-tormentas', 'Orgulho, Fortnite', '1000');
```

Na classe `Database`, vamos criar um método `select()` que executará uma query e retornará todos os registros da tabela:

```python
def select(self, query):
    try:
        self.cursor.execute(query)
        return self.cursor.fetchall()
    except Error as e:
        print(f'Erro: {e}')
        return None
```

No `app.py` vamos adicionar um código para retornar todos os registros da tabela `heroi` e imprimir os registros na tela:

```python
try:
    db = Database()
    db.connect()
    query = "SELECT * FROM heroi"
    vingadores = db.select(query)
    for vingador in vingadores:
        print(vingador)
except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    db.disconnect()

# Interface().menu_principal() # Comente essa linha para executar apenas a demonstração
```

Com esse código, ao executar o arquivo `app.py`, você verá a saída dos registros da tabela `heroi`:

```
(1, 'Homem de Ferro', 'Tony Stark', 'Humano', 'Inteligência, Tecnologia', 'Armadura', 'Arrogância', '100')
(2, 'Thor', 'Thor', 'Deidade', 'Força, Relâmpagos, Mjolnir', 'Rompe-tormentas', 'Orgulho, Fortnite', '1000')
```

> Observe que o retorno do método `fetchall()` é uma **lista de tuplas**, onde cada tupla representa um registro da tabela. As tuplas contêm os valores dos campos do registro na ordem em que foram selecionados na query. Lembre-se de que tuplas são **imutáveis**, ou seja, não é possível alterar os valores de uma tupla após sua criação, e isso é importante para garantir a integridade dos dados.

Ainda no arquivo `app.py`, podemos utilizar esses registros retornados para carregar os dados dos herois em memória, instanciando objetos da classe `Vingador`:

```python	
try:
    db = Database()
    db.connect()
    query = "SELECT * FROM heroi"
    vingadores = db.select(query)
    for vingador in vingadores:
        Vingador(vingador[1], vingador[2], vingador[3], vingador[4], vingador[5], vingador[6], vingador[7], vingador[8], vingador[9])
except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    db.disconnect()
```

> Note que dessa forma, ao executar `app.py`, os registros da tabela `heroi` serão **carregados em memória** como objetos da classe `Vingador`.

Em seguida, com o código testado no arquivo `app.py`, você pode implementar o método `carregar_vingadores()` na classe `Vingador` para carregar os dados dos herois em memória:

```python
def carregar_vingadores():
    try:
        db = Database()
        db.connect()
        query = 'SELECT * FROM heroi'
        vingadores = db.select(query)
        for vingador in vingadores:
            Vingador(vingador[1], vingador[2], vingador[3], vingador[4], vingador[5], vingador[6], vingador[7])
    except Exception as e:
        print(f'Erro: {e}')
    finally:
        db.disconnect()
```

Com esse método, você pode carregar os dados dos herois em memória a partir de qualquer parte do código, chamando `Vingador.carregar_vingadores()`. Vamos fazer isso no arquivo `app.py` para carregar os dados dos herois ao iniciar a aplicação (**esse método pode ser chamado também no método `__init__` da classe `Interface`**):

```python
from model.interface import Interface
from model.vingador import Vingador
# from model.database import Database

def main():
    Vingador.carregar_vingadores()
    Interface().menu_principal()

if __name__ == '__main__':
    main()
```

Veja como ficaria no método `__init__` da classe `Interface`:

```python
def __init__(self):
    Vingador.carregar_vingadores()
    self.menu_principal()
```

Estamos chegando ao final da demonstração do método `fetchall()`. Ainda podemos utilizar um recurso do Python para simplificar a criação dos objetos da classe `Vingador` a partir dos registros da tabela `heroi`. Vamos utilizar o **desempacotamento de tuplas** para passar os valores diretamente para o construtor da classe `Vingador`. Para isso, vamos modificar a query para selecionar apenas os campos necessários e correspondentes aos parâmetros do construtor da classe `Vingador`:

```python
def carregar_vingadores():
    try:
        db = Database()
        db.connect()
        query = 'SELECT nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca FROM heroi'
        vingadores = db.select(query)
        for vingador in vingadores:
            Vingador(*vingador)
    except Exception as e:
        print(f'Erro: {e}')
    finally:
        db.disconnect()
```

> Considere acrescentar um atributo `id` na classe `Vingador` para armazenar o `heroi_id` do registro da tabela `heroi`. Isso será importante para identificar cada objeto da classe `Vingador` e realizar operações de atualização e exclusão no banco de dados com novos métodos que serão implementados.

```python
class Vingador:
    def __init__(self, id, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca, convocado=False, tornozeleira=False, chip_gps=False):
        self.id = id
        self.nome_heroi = nome_heroi
        self.nome_real = nome_real
        self.categoria = categoria.capitalize()
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.nivel_forca = nivel_forca
        self._convocado = convocado
        self._tornozeleira = tornozeleira
        self._chip_gps = chip_gps
        self.lista_vingadores.append(self)
```

> **Atenção:** Como modificamos o construtor da classe `Vingador`, precisamos ajustar a chamada do construtor em todas as partes do código onde ele é utilizado. Podemos já ajustar a chamada no método `cadastrar_vingador()` da classe `Interface`:

```python
# Esta chamada foi movida para o bloco try/except do método cadastrar_vingador()
Vingador(cursor.lastrowid, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca)
```

Com essas modificações, a demonstração do método `fetchall()` está concluída. Você pode executar o arquivo `app.py` para ver a saída dos registros da tabela `heroi` e carregar os dados dos herois em memória como objetos da classe `Vingador`. Teste o cadastramento de novos herois e a listagem dos herois cadastrados.