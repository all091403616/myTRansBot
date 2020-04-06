# -*- coding: utf-8 -*-
from googletrans import Translator
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove

updater=Updater('1198842168:AAFeVzxwsX-99HjOdxMReY-M-uaQT3p51kw')

PoE,EoP,MODE,ROBOTS=range(4)

def start_command(bot, update):
    try:
        b = bot.get_chat_member('-1001206881648', update.message.from_user.id)
        if b.status == 'left':
            bot.send_message(update.message.chat.id,"برای استفاده از ربات لطفا در کانال زیز عضو شوید و مجددا روی /start کلیک کنید\n @jok_khone")
        else:
            keyboards=[
                ["🇮🇷فارسی به انگلیسی🇮🇷",'🏴󠁧󠁢󠁥󠁮󠁧󠁿انگلیسی به فارسی🏴󠁧󠁢󠁥󠁮󠁧󠁿'],
                ['🤖دیگر ربات های ما🤖','🥁تبلیغات🥁']
            ]
            reply_markup=ReplyKeyboardMarkup(keyboards,  one_time_keyboard=True)
            update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید",reply_markup=reply_markup)
            del keyboards
            del reply_markup
            return MODE
    except Exception as ex:
        print(str(ex))
    del b


def buttons(bot, update):
    if update.message.text=="🇮🇷فارسی به انگلیسی🇮🇷":
        update.message.reply_text("لطفا متن فارسی خود را وارد کنید. برای توقف عملیات /cancel را وارد کنید",reply_markup=ReplyKeyboardRemove())
        return PoE
    elif update.message.text == '🏴󠁧󠁢󠁥󠁮󠁧󠁿انگلیسی به فارسی🏴󠁧󠁢󠁥󠁮󠁧󠁿':
        update.message.reply_text("لطفا متن انگلیسی خود را وارد کنید. برای توقف عملیات /cancel را وارد کنید",reply_markup=ReplyKeyboardRemove())
        return EoP
    elif update.message.text == '🥁تبلیغات🥁':
        update.message.reply_text('برای تبلیغات با آیدی زیر در ارتباط باشید.\n @Ashoj79')
        keyboards = [
            ["🇮🇷فارسی به انگلیسی🇮🇷", '🏴󠁧󠁢󠁥󠁮󠁧󠁿انگلیسی به فارسی🏴󠁧󠁢󠁥󠁮󠁧󠁿'],
            ['🤖دیگر ربات های ما🤖', '🥁تبلیغات🥁']
        ]
        reply_markup = ReplyKeyboardMarkup(keyboards, one_time_keyboard=True)
        update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
        del keyboards
        del reply_markup
        return MODE
    elif update.message.text == '🤖دیگر ربات های ما🤖':
        keyboard = [
            [InlineKeyboardButton('ربات متن جادویی', url='https://t.me/magic_txt_bot')],
            [InlineKeyboardButton('ربات دانلود از اینستاگرام', url='https://t.me/insta_down_load_bot')],
            [InlineKeyboardButton('ربات دانلود از یوتیوب', url='https://t.me/youtube_down_load_bot')],
            [InlineKeyboardButton('ربات کوتاه کننده لینک', url='https://t.me/short_url_bot')],
            [InlineKeyboardButton('ربات آب و هوا فارسی', url='https://t.me/weather_persian_bot')],
            [InlineKeyboardButton('توقف', callback_data='cancel')]
        ]
        reply_markup=InlineKeyboardMarkup(keyboard)
        update.message.reply_text('ربات های ما', reply_markup=reply_markup)
        del keyboard
        del reply_markup
        return ROBOTS


def EoP_translator(bot, update):
    if '/cancel' not in update.message.text:
        translator = Translator()
        result = translator.translate(update.message.text, src='en', dest='fa')
        update.message.reply_text(result.text)
        del translator
        del result

    keyboards = [
        ["🇮🇷فارسی به انگلیسی🇮🇷", '🏴󠁧󠁢󠁥󠁮󠁧󠁿انگلیسی به فارسی🏴󠁧󠁢󠁥󠁮󠁧󠁿'],
        ['🤖دیگر ربات های ما🤖', '🥁تبلیغات🥁']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboards, one_time_keyboard=True)
    update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
    del keyboards
    del reply_markup
    return MODE


def PoE_translator(bot, update):
    if '/cancel' not in update.message.text:
        translator = Translator()
        result = translator.translate(update.message.text, src='fa', dest='en')
        update.message.reply_text(result.text)
        del translator
        del result

    keyboards = [
        ["🇮🇷فارسی به انگلیسی🇮🇷", '🏴󠁧󠁢󠁥󠁮󠁧󠁿انگلیسی به فارسی🏴󠁧󠁢󠁥󠁮󠁧󠁿'],
        ['🤖دیگر ربات های ما🤖', '🥁تبلیغات🥁']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboards, one_time_keyboard=True)
    update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
    del keyboards
    del reply_markup
    return MODE


def robots(bot,update):
    query=update.callback_query
    if query.data == 'cancel':
        keyboards = [
            ["🇮🇷فارسی به انگلیسی🇮🇷", '🏴󠁧󠁢󠁥󠁮󠁧󠁿انگلیسی به فارسی🏴󠁧󠁢󠁥󠁮󠁧󠁿'],
            ['🤖دیگر ربات های ما🤖', '🥁تبلیغات🥁']
        ]
        reply_markup = ReplyKeyboardMarkup(keyboards, one_time_keyboard=True)
        update.callback_query.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
        del keyboards
        del reply_markup
        return MODE


def error(update,context):
    print('error: '+context.error)

    keyboards = [
        ["🇮🇷فارسی به انگلیسی🇮🇷", '🏴󠁧󠁢󠁥󠁮󠁧󠁿انگلیسی به فارسی🏴󠁧󠁢󠁥󠁮󠁧󠁿'],
        ['🤖دیگر ربات های ما🤖', '🥁تبلیغات🥁']
    ]
    reply_markup=ReplyKeyboardMarkup(keyboards,  one_time_keyboard=True)
    update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید",reply_markup=reply_markup)
    del keyboards
    del reply_markup
    return MODE


def cancel(bot, update):
    update.message.reply_text("عملیات متوقف شد", reply_text=ReplyKeyboardRemove())

    keyboards = [
        ["🇮🇷فارسی به انگلیسی🇮🇷", '🏴󠁧󠁢󠁥󠁮󠁧󠁿انگلیسی به فارسی🏴󠁧󠁢󠁥󠁮󠁧󠁿'],
        ['🤖دیگر ربات های ما🤖', '🥁تبلیغات🥁']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboards, one_time_keyboard=True)
    update.message.reply_text("لطفا گزینه مورد نظر خود را انتخاب کنید", reply_markup=reply_markup)
    del keyboards
    del reply_markup
    return MODE

conv_handler=ConversationHandler(
    entry_points=[CommandHandler('start',start_command)],
    states={
        MODE:[MessageHandler(Filters.regex("^(🇮🇷فارسی به انگلیسی🇮🇷|🏴󠁧󠁢󠁥󠁮󠁧󠁿انگلیسی به فارسی🏴󠁧󠁢󠁥󠁮󠁧󠁿|🥁تبلیغات🥁|🤖دیگر ربات های ما🤖)$"),buttons)],
        EoP:[MessageHandler(Filters.text,EoP_translator)],
        PoE:[MessageHandler(Filters.text,PoE_translator)],
        ROBOTS:[CallbackQueryHandler(robots)]
    },
    fallbacks=[CommandHandler('cancel',cancel)]
)

dp=updater.dispatcher

dp.add_handler(conv_handler)

updater.start_polling()

updater.idle()

# translator=Translator()
# result=translator.translate('Hello, how are you',src='en',dest='fa')
# print(result.text)