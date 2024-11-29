from model.database import Database

class Vingador:
    
    CATEGORIAS_PERMITIDAS = ['Humano', 'Meta-humano', 'Androide', 'Deidade', 'Alienígena']
    lista_vingadores = []

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

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        categoria = categoria.capitalize()
        if categoria not in self.CATEGORIAS_PERMITIDAS:
            print(f"Categoria '{categoria}' inválida.")
            self._categoria = self._solicitar_categoria_valida()
        else:
            self._categoria = categoria

    @property
    def tornozeleira(self):
        return 'Sim' if self._tornozeleira else 'Não'

    @tornozeleira.setter
    def tornozeleira(self, valor):
        self._tornozeleira = valor

    @property
    def chip_gps(self):
        return 'Sim' if self._chip_gps else 'Não'

    @chip_gps.setter
    def chip_gps(self, valor):
        self._chip_gps = valor

    @property
    def convocado(self):
        return 'Sim' if self._convocado else 'Não'
    
    @convocado.setter
    def convocado(self, valor):
        self._convocado = valor

    def _solicitar_categoria_valida(self):
        while True:
            categoria = input(f"Digite uma categoria válida ({', '.join(self.CATEGORIAS_PERMITIDAS)}): ").capitalize()
            if categoria in self.CATEGORIAS_PERMITIDAS:
                return categoria
            print(f"Categoria '{categoria}' inválida.")

    @classmethod
    def listar_vingadores(cls):
        print(f"{'Nome do Herói'.ljust(20)} |  {'Nome Real'.ljust(20)} |  {'Categoria'.ljust(15)} |  {'Tornozeleira'.ljust(15)} |  {'Rastreado'.ljust(15)}")
        print('-' * 95)
        for vingador in cls.lista_vingadores:
            print(vingador)

    def listar_detalhes_vingador(self):
        print()
        print(f"Vingador: {self.nome_heroi}")
        print(f"Nome Real: {self.nome_real}")
        print(f"Categoria: {self.categoria}")
        print(f"Poderes: {', '.join(self.poderes)}")
        print(f"Poder Principal: {self.poder_principal}")
        print(f"Fraquezas: {', '.join(self.fraquezas)}")
        print(f"Nível de Força: {self.nivel_forca}")
        print(f"Convocado: {self.convocado}")
        print(f"Tornozeleira: {self.tornozeleira}")
        print(f"Chip GPS: {self.chip_gps}")
        return None

    def __str__(self):
        return f'{self.nome_real.ljust(20)} |  {self.nome_heroi.ljust(20)} |  {self.categoria.ljust(15)} |  {self.tornozeleira.ljust(15)} |  {self.chip_gps.ljust(15)}'

    def aplicar_tornozeleira(self):
        if self._convocado:
            if self.nome_heroi == 'Thor':
                return '"Eu sou Thor, Deus do Trovão, filho de Odin! Nenhuma corrente ou restrição pode me controlar. \nTentem colocar-me uma tornozeleira, e verão o que acontece quando um deus é desafiado..."'
            elif self.nome_heroi == 'Hulk':
                return '"Hulk esmaga! Hulk mais forte tornozeira!"'
            self.tornozeleira = True
            return 'Tornozeleira aplicada com sucesso!'
        return f'{self.nome_heroi} não foi convocado ainda.'

    def aplicar_chip_gps(self):
        if not self._tornozeleira:
            return f'{self.nome_heroi} precisa estar com a tornozeleira aplicada.'
        self.chip_gps = True
        return 'Chip GPS aplicado com sucesso!'

    def convocar(self):
        self.convocado = True
        return f'{self.nome_heroi} convocado!'

    def prender(self):
        return f'{self.nome_heroi} teve o mandado de prisão emitido!'

    def listar_poderes(self):
        return self.poderes
    
    @staticmethod
    def carregar_herois():
        try:
            db = Database()
            db.connect()

            query = 'SELECT heroi_id, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca FROM heroi'
            herois = db.select(query) # retorna uma lista de tuplas
            for heroi in herois:
                Vingador(*heroi)
        except Exception as e:
            print(f'Erro: {e}')
        finally:
            db.disconnect()