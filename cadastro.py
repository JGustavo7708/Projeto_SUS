from datetime import datetime
import os
import json
import re

#melhorar o calculo dos sintomas, criar um dicionario com os sintomas e os pesos, e depois fazer a média dos pesos

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
    
#função para validar o CPF
def validar_cpf():
    while True:
        cpf = input("\nDigite o seu CPF (xxx.xxx.xxx-xx): ").strip()
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            print("CPF inválido! Use o formato xxx.xxx.xxx-xx")
            continue
        return cpf
    
#função para validar o email	
def validar_email():
    while True:
        email = input("\nDigite o seu email: ").strip().lower()
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            print("Email inválido!")
            continue
        return email
    
# Função principal
def cadastrar_paciente():
    banco = carregar_banco()
    while True:
        print("-" * 18, "Cadastro de Paciente", "-" * 18)
        print(f"\n{' ' * 4}[1]Cadastrar Paciente{' ' * 4}[2]Já tenho cadastro\n\n{' ' * 23}[3]Sair")
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == '3':
            print("\nSaindo...")
            return
        
        elif opcao == '2':
            cpf = validar_cpf()
            
            if cpf not in banco:
                print("\nCPF não encontrado! Por favor, faça o cadastro.")
            else:
                print("\nCPF encontrado!")
                print("\nDados encontrados:")
                for chave, valor in banco[cpf].items():
                    print(f"\n  {chave.title()}: {valor}")
            # continue
            break
        elif opcao == '1':
            while True:
                cpf = validar_cpf()

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

            # 1. Regex: nome com ao menos 2 palavras, cada uma com 2+ letras
                if not re.match(r'^([A-Za-zÀ-ÿ]{2,}\s+){1,}[A-Za-zÀ-ÿ]{2,}$', nome):
                    print("Digite pelo menos nome e sobrenome, com cada palavra tendo 2 ou mais letras.")
                    continue

            # 2. Verifica se há palavras inválidas no final
                palavras = nome.split()
                conectivos = ["da", "de", "do", "dos", "das"]
                if palavras[-1].lower() in conectivos:
                    print("Nome não pode terminar com palavras como 'da', 'de', 'do'... Digite o nome completo.")
                    continue

            # 3. Verifica se o nome tem menos de 15 caracteres (tamanho mínimo)
                if len(nome) < 15:
                    print("O nome está muito curto, verifique se está completo.")
                    continue
                
                break
            
            # Após o nome, pede a data de nascimento
            while True:
                data_nascimento = input("\nDigite a data de nascimento (dd/mm/aaaa): ").strip()
                idade = calcular_idade(data_nascimento)
                if idade is None or idade < 0 or idade > 120:
                    print("Data inválida! Use o formato dd/mm/aaaa \n")
                    continue
                break
            
            # Após a data de nascimento, pede o Cartão SUS
            while True:
                cartao_sus = input("\nDigite o número do Cartão SUS (formato xxx xxxx xxxx xxxx): ").strip()
                if not re.match(r'\d{3} \d{4} \d{4} \d{4}', cartao_sus):
                    print("Número do Cartão SUS inválido! Use o formato correto \n")
                    continue
                break
            
            # Após o Cartão SUS, pede o email
            while True:
                email = validar_email()
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
            print("\n\nPaciente cadastrado com sucesso!\n:)\n")

cadastrar_paciente()

ARQUIVO_SINTOMAS = 'sintomas.json'
peso_base = []

def carregar_sintomas():
    if os.path.exists(ARQUIVO_SINTOMAS):
        with open(ARQUIVO_SINTOMAS, 'r') as s:
            return json.load(s)
    return {}

def salvar_sintoma(sintoma):
    with open(ARQUIVO_SINTOMAS, 'w') as s:
        json.dump(sintoma, s, indent=4)

def calcular_media_peso_sintoma(nivel_de_incomodo):
    peso_base.append(nivel_de_incomodo)
    media_peso_sintoma = sum(peso_base) / len(peso_base)
    return media_peso_sintoma

def cadastrar_sintoma():
    sintomas = carregar_sintomas()
    
    while True:
        print("\n", "-" * 14, " Triagem ", "-" * 14)

        sintoma_sentido = str(input("\nO que está sentindo? ")).title()

        if sintoma_sentido in sintomas:
            tempo_de_sintoma = str(input(f"\nHá quanto tempo está sentindo {sintoma_sentido} (X Dias)? ").strip())
            nivel_de_incomodo = int(input(f"\nNuma escala de 0-10, qual o nível de desconforto do seu(sua) {sintoma_sentido}? "))
            media_peso = calcular_media_peso_sintoma(nivel_de_incomodo)

            sintomas[sintoma_sentido] = {
                "Sintoma": sintoma_sentido,
                "Peso": media_peso
            }

            salvar_sintoma(sintomas)
            
        else:
            nivel_de_incomodo = int(input(f"\nNuma escala de 0-10, qual o nível de desconforto do seu(sua) {sintoma_sentido}? "))
            media_peso = calcular_media_peso_sintoma(nivel_de_incomodo)

            sintomas[sintoma_sentido] = {
                "Sintoma": sintoma_sentido,
                "Peso": media_peso
            }

            salvar_sintoma(sintomas)
            #cadastrado!
            
        continuar = input("\nEstá sentindo mais alguma coisa? (s/n): ").lower()
        if continuar != 's':
            break
    
'''
{
    "145.745.758-07": {
        "nome": "Janderson Alves de Sousa",
        "cartao_sus": "123.456.789-00"
    },
    "123.456.789-08": {
        "nome": "Juliana Bonde",
        "data_nascimento": "20/04/1990",
        "idade": 34,
        "cartao_sus": "789 6543 2109 3548",
        "email": "julianabondebb5@redmail.com"
    }
}
'''
