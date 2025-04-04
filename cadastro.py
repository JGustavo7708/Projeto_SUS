from datetime import datetime #vai ser usado futuramente para talvez calcular a idade do usuário
class Usuario():
    def __init__(self):
        self._ = 0 #variável '_' de convenção

    def cadastro(self):
        #cadastro0 do usuario
        print("-" * 20,"Cadastro","-" * 20)
        self.nome = str(input("\nDigite o seu nome: ")) #nome do usuário    
        self.email = str(input("Digite o seu email: ")) #email do usuário
        self.cpf = int(input("Digite o seu cpf: ")) #cpf do usuário
        self.email = int(input("Digite o seu número do SUS: ")) # nº cpf do usuário
        self.data = str(input("Digite sua data de nascimento: ")) #data de nascimento do usuário

    def data_nascimento(self):
        #Separa a data no formato dia/mes/ano em variáveis únicas
        dia, mes, ano = map(int, self.data.split("/"))
        #o calculo de idade ainda precisa ser completado

#criando um usuário 
usuario = Usuario() 

#chamando a função Cadastro dentro da classe Usuarios      
usuario.cadastro()

#chamando a função data_nascimento() dentro da classe Usuários Lara teste
usuario.data_nascimento()

#dados adicionados por janderson
dados = {
        'Pedro': '123.456.789-00',
        'Lucas': '123.456.789-01',
        'Ana': '123.456.789-02',
        'Marcos': '123.456.789-03',
        'Fernanda': '123.456.789-04',
        'Roberta': '123.456.789-05',
        'Carlos': '123.456.789-06',
        'Alice': '123.456.789-07',
        'Juliana': '123.456.789-08'}

dados_sus = {
        '123.456.789-00':'789 6543 2109 3540',
        '123.456.789-01':'789 6543 2109 3541',
        '123.456.789-02':'789 6543 2109 3542',
        '123.456.789-03':'789 6543 2109 3543',
        '123.456.789-04':'789 6543 2109 3544',
        '123.456.789-05':'789 6543 2109 3545',
        '123.456.789-06':'789 6543 2109 3546',
        '123.456.789-07':'789 6543 2109 3547',
        '123.456.789-08':'789 6543 2109 3548'  }#definindo o dicionário com os dados do SUS

cpf = dados.get("Lucas")  # Pega o CPF do Lucas
cartao_sus = dados_sus.get(cpf)  # Pega o Cartão SUS desse CPF
print(f"O cartão do SUS de Lucas é: {cartao_sus}")

cpf = input("Digite o seu CPF: ")
if cpf in dados.values():
    print("CPF já cadastrado.")
else:
    nome = input("Digite o seu nome: ")
    dados[nome] = cpf
    print("Cadastro realizado com sucesso.")

print(dados)

sintomas = {
    "dor de cabeça": 0.2,
    "diarreia": 0.2,
    "febre": 0.2
}#falta ordenar os sintomas e adicionar mais sintomas


