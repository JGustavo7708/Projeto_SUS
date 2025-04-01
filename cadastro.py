import time
class Usuario():
    def __init__(self):
        self._ = 0 #variável '_' de convenção

    def cadastro(self):
        #cadastro0 do usuario
        print("-" * 20,"Cadastro","-" * 20)
        self.nome = str(input("\nDigite o seu nome: ")) #nome do usuário    
        self.email = str(input("Digite o seu email: ")) #email do usuário
        self.cpf = int(input("Digite o seu cpf: ")) #cpf do usuário
        self.email = int(input("Digite o seu número do SUS: ")) #nº cpf do usuário
        self.data = str(input("Digite sua data de nascimento: ")) #data de nascimento do usuário

    def data_nascimento(self):
        #Separa a data no formato dia/mes/ano em variáveis únicas
        dia, mes, ano = map(int, self.data.split("/"))


#o calculo de idade ainda precisa ser completado
usuario = Usuario()        
usuario.cadastro()
usuario.data_nascimento()

#dados adicionados por janderson
dados ={'Pedro': '123.456.789-00',
        'Lucas': '123.456.789-01',
        'Ana': '123.456.789-02',
        'Marcos': '123.456.789-03',
        'Fernanda': '123.456.789-04',
        'Roberta': '123.456.789-05',
        'Carlos': '123.456.789-06',
        'Alice': '123.456.789-07',
        "Juliana": '123.456.789-08'}

