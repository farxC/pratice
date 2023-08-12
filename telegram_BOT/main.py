import logging
from telegram import Update
from telegram.ext import *
import keys
import functions

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
def main() -> None: 
    application = Application.builder().token(keys.token).build()
   

    # Commands
    help_handler = CommandHandler('help', functions.help)
    caps_handler = CommandHandler('caps', functions.caps)
    start_handler = CommandHandler('start', functions.start)
    echo_handler = CommandHandler('echo', functions.echo)
    

    # Messages
    unknown_handler = MessageHandler(filters.COMMAND, functions.unknown) 

    application.add_handler(echo_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(caps_handler)
    application.add_handler(unknown_handler) 

    application.run_polling()


if __name__ == '__main__':
    main()
   

# /spec www.siteescolhido.com
# A ideia é abrir um site digitado pelo usuário e pegar as informações do mesmo, como IP e localização. 
# Após isso também registrar a data e horário da requisição. 
