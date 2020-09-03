from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import BASE_API_URL, TELEGRAM_TOKEN

def welcome(update, context):
    message = "Olá, usuário!"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    
def start(bot, update):
    response_message = "Start Start"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def products(bot, update, args):
    response_message = args[0]
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def AX(bot, update, args):
    response_message = args[0]
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

    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        CommandHandler('produto', products, pass_args=True)
    )

    dispatcher.add_handler(
        CommandHandler('AX', AX, pass_args=True)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()