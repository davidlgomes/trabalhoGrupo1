import os
import csv
from datetime import datetime

def validar_resposta(resposta):
    # Verifica se a resposta contém apenas números 1, 2 ou 3
    if resposta not in ['1', '2', '3']:
        return False
    return True

def validar_resposta1(genero):
    # Verifica se a resposta contém apenas números de 1 a 10
    if genero not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        return False
    return True

def validar_idade(idade):
    try:
        idade = int(idade)
        if idade >= 0 and idade <= 120:
            return True
        else:
            return False
    except ValueError:
        return False

def main():
    # Define as perguntas da pesquisa
    perguntas = [
        "Você pratica atividade física regularmente? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>> ",
        "Você consome pelo menos 5 porções de frutas e vegetais por dia? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>> ",
        "Você costuma dormir pelo menos 7 horas por noite? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>> ",
        "Você fuma atualmente? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>> "
    ]

    # Verifica se o arquivo já existe e está vazio
    if not os.path.exists('dados_pesquisa.csv') or os.path.getsize('dados_pesquisa.csv') == 0:
        with open('dados_pesquisa.csv', 'w', newline='') as arquivo_csv:
            # Abre o arquivo CSV para escrita
            escritor_csv = csv.writer(arquivo_csv)

            # Escreve o cabeçalho do arquivo CSV
            escritor_csv.writerow(
                ['Idade', 'Genero', 'Resposta 1', 'Resposta 2', 'Resposta 3', 'Resposta 4', 'Data', 'Hora'])

    # Abre o arquivo CSV para adição
    with open('dados_pesquisa.csv', 'a', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)

        # Loop para inserção contínua de respostas
        while True:
            idade = input("Informe a sua idade (00 para sair): ")
            if idade == '00':
                break
            if not validar_idade(idade):
                print("Idade inválida. Por favor, informe a sua idade novamente.")
                continue

            genero = input("Qual o seu gênero?\n1- Masculino\n2- Feminino\n3- Não binário\n4- Agênero\n5- Gênero fluido\n6- Bigênero\n7- Transgênero\n8- Intersexo\n9- Outro\n10- Prefiro não dizer\n>> ")
            while not validar_resposta1(genero):
                genero = input("Opção inválida. Por favor, selecione uma das opções de gênero listadas: ")

            respostas = []
            for pergunta in perguntas:
                resposta = input(pergunta)
                while not validar_resposta(resposta):
                    resposta = input("Resposta inválida. Por favor, selecione uma das opções listadas: ")
                respostas.append(resposta)

            # Obtém data e hora atual
            data_atual = datetime.now().strftime('%Y-%m-%d')
            hora_atual = datetime.now().strftime('%H:%M:%S')

            # Escreve os dados no arquivo CSV
            escritor_csv.writerow([idade, genero] + respostas + [data_atual, hora_atual])

    print("Dados salvos com sucesso no arquivo 'dados_pesquisa.csv'!")

main()
