from apscheduler.schedulers.background import BackgroundScheduler
from .models import *
from django.utils import timezone
import pandas as pd
import requests.status_codes
import json

def StartChatBotScheduler():
    scheduler = BackgroundScheduler()
    scheduler.remove_all_jobs()
    scheduler.add_job(ChatBotJob, 'interval', seconds=2)
    scheduler.start()


#1 -) PROCURAR NO BANCO DE DADOS NA TABELA CHATBOT QUAIS DADOS
#     ESTÃO DONE=FALSE E SCHEDULED_DATE <= NOW() -->timezone

#2 -) EXECUTAR UM FOR PARA CADA ITEM RETORNADO E LER O ARQUIVO FILE
#     USANDO O PANDAS (pip install pandas)

#3 -) FAÇA UM FOR DE CADA LINHA DO EXCEL E CHAME A FUNÇÃO 
#     sendMessage()  ONDE NESTA FUNÇÃO VOCÊ VAI DAR
#     UM PRINT NO TERMINAL DO NÚMERO DE TELEFONE E DO NOME E 
#     A MENSAGEM A SER ENVIADA

#4 -) APÓS EXECUTAR O ARQUIVO INTEIRO, SALVE O MODEL DO CHATBOT PARA DONE=TRUE
#pip install pandas openpyxl
def SendMessage(message, phone):
    print('Message: ', message, phone)

def envia(message, phone):
    url = 'https://graph.facebook.com/v18.0/283933774806594/messages'
    headers = {'content-type': 'application/json',
               'Authorization': 'Bearer EAAOAHOc0oOcBO83muP6DNXZC36fD8CxLgZBoTN4rYyTwzqpEGZC8JIRYaYJY0BFlqgmg6lUeO9RrgGmHOGnKHkp2PyX4iCPKM5hZARJsQVA9QTzfJKMkJtXzUERGpnB2TWz9ZBUyacuH6BJGRkKju0S36ewjjChkRmsWON9hQIzZBv1Qr8C5QolYUbNV05LwNQBzSCmOGcjZB6kJ6wk7tQZD'
               }
    payload = {
    "messaging_product": "whatsapp",
    "to": "5519987457001",
    "type": "template",
    "template": {
        "name": "aulaaa",
        "language": {
            "code": "pt_br"
        }
    }
}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r)


    
    if r.status_code != 200:
        r = json.loads(r.text) # transformando jason em string
        print(r['error']['error_data']['details'])
        novo_registro = FileLogs(
        chatbotFK=ChatBot.chatbot,  # Substitua chatbot_instancia pela instância real do ChatBot
        response=r['error']['error_data']['details'],
        type='4',
        row=1,
        phoneNumber="123456789"
    )
    novo_registro.save()



 

# def ChatBotJob():
#     print('Running ChatBot Job...')
#     chatBots = ChatBot.objects.filter(done=False).filter(scheduledDate__lte=timezone.now())
#     for bot in chatBots:
#         file = pd.read_excel(bot.file.path)
#         for index,row in file.iterrows():
#             if row['Telefone'] is not None:
#                 SendMessage(bot.message.replace('{name}',row['Nome']),row['Telefone'])
#         bot.done = True
#         bot.save()
    

def ChatBotJob():
    print('Running ChatBot Job...')
    chatBots = ChatBot.objects.filter(done=False).filter(scheduledDate__lte=timezone.now())
    for bot in chatBots:
        file = pd.read_excel(bot.file.path)
        for index,row in file.iterrows():
            if row['Telefone'] is not None:
                # SendMessage(bot.message.replace('{name}',row['Nome']),row['Telefone'])
                envia(bot.message.replace('{name}',row['Nome']),row['Telefone'])
        bot.done = True
        bot.save()