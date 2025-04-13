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
        nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')

        hoje = datetime.today()
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        return idade
    except ValueError:
        return None
    
# Função principal
def cadastrar_paciente():
    banco = carregar_banco()
    while True:
        print("-" * 20, "Cadastro de Paciente", "-" * 20)
        print('''1. Cadastrar Paciente.''')
        print('''2. Sair3.''')
        print('''3. Ja tenho cadastro''')
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
                print("\nCPF encontrado!")
                print("Dados encontrados:")
                for chave, valor in banco[cpf].items():
                    print(f"  {chave.title()}: {valor}")
            continue
        elif opcao == '1':
            while True:
                cpf = input("\nDigite o seu CPF (xxx.xxx.xxx-xx): ").strip()
                if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
                    print("CPF inválido! Use o formato xxx.xxx.xxx-xx \n")
                    continue

                if cpf in banco:
                    print("\nVocê já está cadastrado!")
                    print("Dados encontrados: \n")
                    for chave, valor in banco[cpf].items():
                        print(f"  {chave.title()}: {valor}")
                    continue
                break
            
            # Se não estiver cadastrado, pede os dados
            while True:
                nome = input("\nDigite o nome completo: ").strip().title()
                #verifica se o nome digitado realmente é um nome completo
                nome_valido = len(nome)
                if nome_valido < 15:
                    print('Por favor digite seu nome Completo!  \n')
                    continue
                else:
                    break

            while True:
                data_nascimento = input("\nDigite a data de nascimento (dd/mm/aaaa): ").strip()
                idade = calcular_idade(data_nascimento)
                if idade is None or idade < 0 or idade > 120:
                    print("Data inválida! Use o formato dd/mm/aaaa \n")
                    continue
                break
            
            while True:
                cartao_sus = input("\nDigite o número do Cartão SUS (formato xxx xxxx xxxx xxxx): ").strip()
                if not re.match(r'\d{3} \d{4} \d{4} \d{4}', cartao_sus):
                    print("Número do Cartão SUS inválido! Use o formato correto \n")
                    continue
                break
            
            while True:
                email = input("\nDigite o seu email: ").strip().lower()
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                    print("Email inválido! \n")
                    continue
                break

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

cadastrar_paciente()

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
    