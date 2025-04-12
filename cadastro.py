from datetime import datetime
import os
import json
import re

ARQUIVO_BANCO = 'dados_sus.json'

# Função para carregar o banco de dados
def carregar_banco():
    if os.path.exists(ARQUIVO_BANCO):
        with open(ARQUIVO_BANCO, 'r') as f:
            return json.load(f)
    return {}  # Se não existir, retorna dicionário vazio

# Função para salvar no banco
def salvar_banco(banco):
    with open(ARQUIVO_BANCO, 'w') as f:
        json.dump(banco, f, indent=4)
        
# Função para calcular a idade
def calcular_idade(data_nascimento):
    try:
        data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%y')
        hoje = datetime.today()
        idade = hoje.year - data.nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
        return idade
    except ValueError:
        print("Data inválida! Use o formato dd/mm/aaaa")
        return None
    
# Função principal
def cadastrar_paciente():
    banco = carregar_banco()
    while True:
        print("-" * 20, "Cadastro de Paciente", "-" * 20)
        print('''1. Cadastrar Paciente
2. Sair
3. Ja tenho cadastro''')
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == '2':
            print("Saindo...")
            return
        
        elif opcao == '3':
            cpf = input("Digite o seu CPF (xxx.xxx.xxx-xx): ").strip()
            if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}',cpf):
                print("CPF inválido! Use o formato xxx.xxx.xxx-xx")
                continue
            if cpf not in banco:
                print("CPF não encontrado! Por favor, faça o cadastro.")
            else:
                print("CPF encontrado!")
                print(f"Dados: {banco[cpf]}")
            continue
        
        elif opcao == '1':
            cpf = input("Digite o seu CPF (xxx.xxx.xxx-xx): ").strip()
            if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
                print("CPF inválido! Use o formato xxx.xxx.xxx-xx")
                continue
            
            if cpf in banco:
                print("CPF já cadastrado!")
                print(f"Dados: {banco[cpf]}")
                continue
            
            # Se não estiver cadastrado, pede os dados
            nome = input("Digite o nome completo: ").strip().title()
            
            data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ").strip()
            idade = calcular_idade(data_nascimento)
            if idade is None or idade < 0 or idade > 120:
                print("Data inválida! Use o formato dd/mm/aaaa")
                continue
            
            cartao_sus = input("Digite o número do Cartão SUS (formato xxx xxxx xxxx xxxx): ").strip()
            if not re.match(r'\d{3} \d{4} \d{4} \d{4}', cartao_sus):
                print("Número do Cartão SUS inválido! Use o formato correto")
                continue
            
            email = input("Digite o seu email: ").strip().lower()
            if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                print("Email inválido!")
                continue
            
            # Adiciona os dados ao banco
            banco[cpf] = {
                "nome": nome,
                "data_nascimento": data_nascimento,
                "idade": idade,
                "cartao_sus": cartao_sus,
                "email": email
            }

            salvar_banco(banco)
            print("Paciente cadastrado com sucesso!\n")

'''cadastrar_paciente()
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
}#falta ordenar os sintomas e adicionar mais sintomas'''
