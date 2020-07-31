from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from bank_api import Register, Add, Transfer, Balance

# check for new messages --> polling
updater = Updater(token="1315934142:AAGAnh801OaNHM-qZgBT06AnrxW0c2xpLVM", use_context=True)

# allows to register handler -> command, text, video, audio etc
dispatcher = updater.dispatcher


# define a command callback function
def start(update, context):
    start = context
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello, Welcome to KaheyForBankBot!!!")


# create a command handler
start_handler = CommandHandler("start", start)

# add command handler to dispatcher
dispatcher.add_handler(start_handler)


def job(update, context):
    job = context.job
    context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text.upper())


# create a text handler
text_handler = MessageHandler(Filters.text, job)

dispatcher.add_handler(text_handler)


def option(update, context):
    option = context.option
    button = [
        [InlineKeyboardButton("Option 1", callback_data="1"),
         InlineKeyboardButton("Option 2", callback_data="2")],
        [InlineKeyboardButton("Option 3", callback_data="3")]
    ]
    reply_markup = InlineKeyboardMarkup(button)

    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Choose one option..",
                             reply_markup=reply_markup)


option_handler = CommandHandler("option", option)
dispatcher.add_handler(option_handler)


def get_location(update,context):
    get_location = context.get_location
    button = [
        [KeyboardButton("Share Location", request_location=True)]
    ]
    reply_markup = ReplyKeyboardMarkup(button)
    context.bot.send_message(chat_id=update.message.chat_id,
                     text="Mind sharing location?",
                     reply_markup=reply_markup)


get_location_handler = CommandHandler("location", get_location)
dispatcher.add_handler(get_location_handler)


def location(update, context):
    location = context
    lat = update.message.location.latitude
    lon = update.message.location.longitude
    context.bot.send_message(chat_id=update.message.chat_id,
                     text=forecasts,
                     reply_markup=ReplyKeyboardRemove())


location_handler = MessageHandler(Filters.location, location)
dispatcher.add_handler(location_handler)

# start polling
updater.start_polling()
updater.idle()


if __name__ == '__main__':
    main()