from Pessoa import Pessoa

class ControlPessoa:
    def __init__(self):
        self.person = Pessoa() #Instanciando a Classe Pessoa
        self.opcao = -1

    def menu(self):
            print("Escolha uma das opções abaixo: \n\n" +
                  "0. Sair\n" +
                  "1.Cadastrar\n" +
                  "2.Consultar\n")
            self.opcao = int(input())

    def operacao(self):
        while(self.opcao != 0):
            self.menu()#Chamando o Menu
        if self.opcao == 0:
            print("Obrigado!")
        if self.opcao == 1:
            print("Informe o Nome: ")
        nome = input()
        print("\nInforme o Telefone: ")
        telefone = input()
        print("\nInforme o Endereço: ")
        endereco = input()

        self.person.cadastrar(nome, telefone, endereco)
        elif self.opcao == 2:
        print(self.consultarTudo())

        else:
        print("Opção Inválida!")