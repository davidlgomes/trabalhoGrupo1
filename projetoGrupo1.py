import os
import csv
from datetime import datetime

def main():
    # Define as perguntas da pesquisa
    perguntas = [
        "Você pratica atividade física regularmente? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>>",
        "Você consome pelo menos 5 porções de frutas e vegetais por dia? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>>",
        "Você costuma dormir pelo menos 7 horas por noite? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>>",
        "Você fuma atualmente? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>>"
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
            genero = input("Qual o seu gênero?\n1- Masculino\n2- Feminino\n3- Não binário\n4- Agênero\n5- Gênero fluido\n6- Bigênero\n7- Transgênero\n8- Intersexo\n9- Outro\n10- Prefiro não dizer\n>>")
            respostas = []
            for pergunta in perguntas:
                resposta = input(pergunta)
                respostas.append(resposta)

            # Obtém data e hora atual
            data_atual = datetime.now().strftime('%Y-%m-%d')
            hora_atual = datetime.now().strftime('%H:%M:%S')

            # Escreve os dados no arquivo CSV
            escritor_csv.writerow([idade, genero] + respostas + [data_atual, hora_atual])

    print("Dados salvos com sucesso no arquivo 'dados_pesquisa.csv'!")

main()

