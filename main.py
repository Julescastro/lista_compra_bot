from array import array
from operator import truediv
import time
from pprint import pp, pprint
from traceback import print_tb
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import ReplyKeyboardMarkup
import os
from dotenv import load_dotenv
load_dotenv()

updater = Updater(os.getenv("TOKEN") ,use_context=True)
compra = []



def start(update: Update, context: CallbackContext):
    	update.message.reply_text(
		"Hello sir, Bienvenido a RufoBot. Por favor escribe\
		/help para ver los comandos disponibles.")

def help(update: Update, context: CallbackContext):
    	update.message.reply_text("""Available Commands :-
	/add - Para añadir articulos a la lista
	/list - para listar los articulos
    /borrarTodo
	""")


def add(update: Update, context: CallbackContext):
    #pprint(compra)
    #update.message.text
    articulo = update.message.text
    #articulo = articulo.capitalize()
    if articulo in compra:
        print(articulo + ' Ya se encuentra la lista, añade otro')
    else:
        compra.append(articulo)
        update.message.reply_text("articulo añadido")
    return


def list(update: Update, context: CallbackContext):
    update.message.reply_text('lista de la compra:')
    update.message.reply_text('\n'.join(compra))

def borrarTodo(update: Update, context: CallbackContext):
    compra.clear()
    update.message.reply_text( "Borrado"'\n'.join(compra))


def ayuda():
    print('LISTA DE LA COMPRA RUFO MOLON')
    print("Que quieres hacer?")
    print("Introduzca: ")
    print("  - 1 Para añadir articulo")
    print("  - 2 Para listar")    



dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('add', add ))
dp.add_handler(CommandHandler('list', list ))
dp.add_handler(CommandHandler('help', help))
dp.add_handler(CommandHandler('BorrarTodo', borrarTodo))
dp.add_handler(MessageHandler(Filters.text, add))


updater.start_polling()

updater.idle()


