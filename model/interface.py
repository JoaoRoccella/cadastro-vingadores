from model.vingador import Vingador
from model.database import Database
from string import capwords
from os import system

class Interface:

    def __init__(self):
        Vingador.carregar_vingadores()
        self.menu_principal()

    def menu_principal(self):
        self.exibe_titulo_app()
        while True:
            self.exibe_titulo("Menu Principal")
            print("1 - Cadastrar Vingador")
            print("2 - Listar Vingadores")
            print("3 - Convocar Vingador")
            print("4 - Aplicar Tornozeleira")
            print("5 - Aplicar Chip GPS")
            print("6 - Listar Detalhes do Vingador")
            print("7 - Emitir Mandado de Prisão")
            print("0 - Sair", end="\n\n")
            opcao = input("Digite a opção desejada: ")

            if opcao == '1':
                self.exibe_titulo_app()
                self.exibe_titulo("<< Cadastro de Vingador")
                self.cadastrar_vingador()
                self.aguardar_enter()
            elif opcao == '2':
                self.exibe_titulo_app()
                self.exibe_titulo("<< Lista de Vingadores")
                Vingador.listar_vingadores()
                self.aguardar_enter()
            elif opcao == '3':
                self.exibe_titulo_app()
                self.exibe_titulo("<< Convocação de Vingador")
                self.convocar_vingador()
                self.aguardar_enter()
            elif opcao == '4':
                self.exibe_titulo_app()
                self.exibe_titulo("<< Aplicação de Tornozeleira")
                self.aplicar_tornozeleira()
                self.aguardar_enter()
            elif opcao == '5':
                self.exibe_titulo_app()
                self.exibe_titulo("<< Aplicação de Chip GPS")
                self.aplicar_chip_gps()
                self.aguardar_enter()
            elif opcao == '6':
                self.exibe_titulo_app()
                self.exibe_titulo("<< Listar Detalhes do Vingador")
                self.listar_detalhes_vingador()
                self.aguardar_enter()
            elif opcao == '7':
                self.exibe_titulo_app()
                self.exibe_titulo("<< Emitir Mandato de Prisão")
                self.prender()
                self.aguardar_enter()
            elif opcao == '0':
                exit()
            else:
                print("Opção inválida.")
                self.aguardar_enter()
                self.menu_principal()

    def cadastrar_vingador(self):
        '''Exibe o formulário de cadastro de vingador e cria um novo vingador.'''
        nome_heroi = input("Nome do herói: ")
        nome_real = input("Nome real: ")
        categoria = input("Categoria: ").capitalize()
        poderes = input("Poderes (separados por vírgula): ").split(',') # armazena em uma lista
        poder_principal = input("Poder Principal: ")
        fraquezas = input("Fraquezas: (separadas por vírgula): ").split(',') # armazena em uma lista
        nivel_forca = int(input("Nível de Força: "))


        # Salva o vingador no banco de dados
        try:
            db = Database()
            db.connect()

            query = "INSERT INTO heroi (nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            
            values = (nome_heroi, nome_real, categoria, ', '.join(poderes), poder_principal, ', '.join(fraquezas), nivel_forca)

            cursor = db.execute_query(query, values) # executa a query, substituindo os placeholders pelos valores e retorna o cursor para a variável cursor
            
            Vingador(cursor.lastrowid, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca)
        except Exception as e:
            print(f"Erro ao salvar vingador no banco de dados: {e}")
        finally:
            db.disconnect()

        print(f"Vingador(a) '{nome_heroi}' cadastrado com sucesso.")
        self.aguardar_enter()

    def aguardar_enter(self):
        input("\nPressione Enter para continuar...")
        self.menu_principal()

    def convocar_vingador(self):
        nome_heroi = capwords(input("Nome do herói: "))
        for vingador in Vingador.lista_vingadores:
            if nome_heroi in vingador.nome_heroi or nome_heroi in vingador.nome_real:
                print(vingador.convocar())
                self.aguardar_enter()
                return
        print(f"Vingador(a) '{nome_heroi}' não encontrado.")
        self.aguardar_enter()

    def aplicar_tornozeleira(self):
        nome_heroi = capwords(input("Nome do herói: "))
        for vingador in Vingador.lista_vingadores:
            if nome_heroi in vingador.nome_heroi or nome_heroi in vingador.nome_real:
                print(vingador.aplicar_tornozeleira())
                self.aguardar_enter()
                return
        print(f"Vingador(a) '{nome_heroi}' não encontrado.")

    def aplicar_chip_gps(self):
        nome_heroi = capwords(input("Nome do herói: "))
        for vingador in Vingador.lista_vingadores:
            if nome_heroi in vingador.nome_heroi or nome_heroi in vingador.nome_real:
                print(vingador.aplicar_chip_gps())
                self.aguardar_enter()
                return
        print(f"Vingador(a) '{nome_heroi}' não encontrado.")
        self.aguardar_enter()

    def listar_detalhes_vingador(self):
        nome_heroi = capwords(input("Nome do herói: "))
        for vingador in Vingador.lista_vingadores:
            if nome_heroi in vingador.nome_heroi or nome_heroi in vingador.nome_real:
                vingador.listar_detalhes_vingador()
                self.aguardar_enter()
                return
        print(f"Vingador(a) '{nome_heroi}' não encontrado.")
        self.aguardar_enter()

    def prender(self):
        nome_heroi = capwords(input("Nome do herói: "))
        for vingador in Vingador.lista_vingadores:
            if nome_heroi in vingador.nome_heroi or nome_heroi in vingador.nome_real:
                print(vingador.prender())
                self.aguardar_enter()
                return
        print(f"Vingador(a) '{nome_heroi}' não encontrado.")
        self.aguardar_enter()

    @staticmethod
    def exibe_titulo(titulo):
        print(f"\n{titulo}")
        print('-' * len(titulo))

    @staticmethod
    def exibe_titulo_app():
        system('cls')
        print('''

███████████████▀█████████████████████████████████████
█▄─█─▄█▄─▄█─▄▄▄▄█▄─▄█▄─▄████▀▄─██▄─▀█▄─▄█─▄─▄─█▄─▄▄─█
██▄▀▄███─██─██▄─██─███─██▀██─▀─███─█▄▀─████─████─▄█▀█
▀▀▀▄▀▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀        
        ''')
