from datetime import datetime
import os
import json
import re

#deixar o sistema de erro mais otimizado, voltar para oq errou, não tudo

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
        print("-" * 18, "Cadastro de Paciente", "-" * 18)
        print(f"\n{' ' * 4}[1]Cadastrar Paciente{' ' * 4}[2]Já tenho cadastro\n\n{' ' * 23}[3]Sair")
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == '3':
            print("\nSaindo...")
            return
        
        elif opcao == '2':
            cpf = input("\nDigite o seu CPF (xxx.xxx.xxx-xx): ").strip()
            if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}',cpf):
                print("\nCPF inválido! Use o formato xxx.xxx.xxx-xx")
                continue
            if cpf not in banco:
                print("\nCPF não encontrado! Por favor, faça o cadastro.")
            else:
                print("\nCPF encontrado!")
                print("\nDados encontrados:")
                for chave, valor in banco[cpf].items():
                    print(f"\n  {chave.title()}: {valor}")
            continue
        elif opcao == '1':
            cpf = input("\nDigite o seu CPF (xxx.xxx.xxx-xx): ").strip()
            if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
                print("\nCPF inválido! Use o formato xxx.xxx.xxx-xx")
                continue
            
            if cpf in banco:
                print("\nVocê já está cadastrado!")
                print("\nDados encontrados:")
                for chave, valor in banco[cpf].items():
                    print(f"\n  {chave.title()}: {valor}")
                continue
            
            # Se não estiver cadastrado, pede os dados
            nome = input("\nDigite o nome completo: ").strip().title()
            
            data_nascimento = input("\nDigite a data de nascimento (dd/mm/aaaa): ").strip()
            idade = calcular_idade(data_nascimento)
            if idade is None or idade < 0 or idade > 120:
                print(f"\nData inválida! Use o formato abaixo:\n'dd/mm/aaaa'\n\n")
                continue
            
            cartao_sus = input("\nDigite o número do Cartão SUS (formato xxx xxxx xxxx xxxx): ").strip()
            if not re.match(r'\d{3} \d{4} \d{4} \d{4}', cartao_sus):
                print("\nNúmero do Cartão SUS inválido! Use o formato abaixo:\n(xxx xxxx xxxx xxxx)\n")
                continue
            
            email = input("\nDigite o seu email: ").strip().lower()
            if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                print("\nEmail inválido!\n")
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