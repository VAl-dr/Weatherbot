from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from voice import text_to_speech
from weather import Weather
import config

bot_token = config.bot_token
button_city = sorted(['Днепр', 'Запорожье', 'Львов', 'Харьков', 'Одесса', 'Киев',])

def start(update, context):

    reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_city[0]),
                    KeyboardButton(text=button_city[1]),
                    KeyboardButton(text=button_city[2]),
                ],
                [
                    KeyboardButton(text=button_city[3]),
                    KeyboardButton(text=button_city[4]),
                    KeyboardButton(text=button_city[5]),
                ],
            ], resize_keyboard=True
        )

    update.message.reply_text(text=f'Hello {update.effective_user.first_name}', reply_markup=reply_markup)


def w_reply(update, context):

    update.message.reply_text(Weather.three_days_result(update.message.text))

    voice_file = text_to_speech(Weather.three_days_result(update.message.text))
    update.message.reply_voice(voice=open(voice_file, 'rb'))


def main():

    w_bot = Updater(bot_token)

    w_bot.dispatcher.add_handler(CommandHandler('start', start))
    w_bot.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, w_reply))

    w_bot.start_polling()
    w_bot.idle()


if __name__ == '__main__':
    main()
