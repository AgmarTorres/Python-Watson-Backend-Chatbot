
import requests
from telegram.ext import MessageHandler, Filters

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import BASE_API_URL, TELEGRAM_TOKEN

def welcome(update, context):
    message = "Olá, usuário!"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    
def start(bot, update):
  #  response = requests.get("https://machinepythonapi.herokuapp.com/produto")
    response_message =  "O Olá! Sou assistente digital da Start Química. Consigo te ajudar com dúvidas sobre nossos produtos. Qual o produto deseja informação?"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def products(bot, update, args):
    response_message = args[0]
    nome= "Água Sanitária"
    descricao = " é indicada para oalvejamento de roupas, limpeza e desinfecçãode superfícies em geral. Possui excelente açãobactericida na desinfecção dos alimentos. Açãobactericida frente às cepas de Salmonella choleraesuis, Escherichia coli, Staphylococcus aureus e Enterococcus faecium."
    instrucao= "Alvejamento de Roupas: Dilua 1 copo (200 ml) de ÁGUA SANITÁRIA START para cada 20L de água. Adicione as roupas e deixe de molho por 30 minutos antes de iniciar a lavagem no tanque ou na máquina. Atenção: Não utilizar ÁGUA SANITÁRIA START em tecidos de lã, seda, couro, poliuretano (lycra-elastano), roupas coloridas e em roupas com este sinal na etiqueta interna: . Desinfecção Geral: Para desinfetar ralos e vasos sanitários: Utilize ÁGUA SANITÁRIA START pura, deixe agir por no mínimo 10 minutos e em seguida, enxague com água em abundância. Para remover incrustações de pisos e azulejos, lavar superfícies encardidas, vidrarias e cerâmicas: Dilua 1 copo (200 ml) de ÁGUA SANITÁRIA START em 5L de água. Aplique a solução diretamente sobre a superfície a ser limpa e esfregue com o auxílio de uma esponja ou pano úmido até que os resíduos sejam removidos. Em seguida, enxágüe com água em abundância. Desinfecção de frutas, hortaliças, verduras e legumes: Dilua em uma bacia plástica 1 colher de sopa (8 ml) de ÁGUA SANITÁRIA START em 1L de água. Deixe de molho por 10 minutos e em seguida, enxague com água em abundância. Importante: Use luvas ao manusear o produto e suas diluições. "
    
    #response = requests.get("https://machinepythonapi.herokuapp.com/produto")
    #print(response)
    bot.send_message(
        chat_id=update.message.chat_id,
        text=descricao
    )

def AX(bot, update, args):
    response_message = args
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

    #bot.sendPhoto(
    #    chat_id=update.message.chat_id,
    #    photo=BASE_API_URL + args[0]
    #)


def unknown(bot, update):
    response_message = "Comando desconhecido"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher
    
    dispatcher.add_handler( CommandHandler('start', start) )
    dispatcher.add_handler( CommandHandler('produto', products, pass_args=True))
    dispatcher.add_handler( CommandHandler('AX', AX, pass_args=True) )
    dispatcher.add_handler( MessageHandler(Filters.command, unknown) )

    dispatcher.add_handler(MessageHandler(Filters.status_update, unknown))
    
    updater.start_polling(timeout=30, clean=True)

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()