import asyncio
import sys
import telepot
import telepot.async
import settings
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardHide
from bot_functions import *

oferecer_carona = 'Oferecer Carona'
listar_caronas = 'Listar Caronas Disponíveis'

async def on_chat_message(msg):
    global oferecer_carona,listar_caronas

    content_type, chat_type, chat_id = telepot.glance(msg)

    command = ''

    save_id(chat_id)

    if content_type != 'text' and content_type != 'new_chat_member':
        return

    command = msg['text']

    first_name = msg['from']['first_name']
    # elif content_type == 'text':
    #     command = msg['text'].lower()

    if content_type == 'new_chat_member':
        if msg['new_chat_member']['id'] == BOT_ID:
            await bot.sendMessage(chat_id, 'Olá pessoal do <strong>' + msg['chat']['title'] + '</strong>! ' + (u'\U0001f596') + '\nSou o Caronas Piauí Bot!\nObrigado ao <strong>'+first_name+'</strong> por me adicionar.\nUsem os comandos ou enviem "/menu"! ' + (u'\U0001f603'), parse_mode='HTML')
        else:
            await bot.sendMessage(chat_id,'Olá <strong>' + msg['new_chat_member']['first_name'] +\
             '</strong>! '+'\nSeja bem-vindo ao <strong>' + msg['chat']['title'] +\
              '</strong>!\nSou o Caronas Piauí Bot!\nUse os comandos ou envie "/menu"! ' +\
               (u'\U0001f603') +(""+(u'\U0001f355') if chat_id==-1001031289268 else ""), parse_mode='HTML')
        return

    if '/start' in command:
        await bot.sendMessage(chat_id,'Olá <strong>' + first_name + '</strong>, sou o Caronas Piauí Bot! ' + (u'\U0001f596') + '\nUse os comandos ou envie "/menu"! ' + (u'\U0001f603'), parse_mode='HTML')
        return
    elif '/listar_caronas' in command:
        await bot.sendMessage(chat_id,"<strong>" + first_name + "</strong>, "+get_caronas()+"", parse_mode='HTML')
        return
    elif '/oferecer_carona' in command:
        await bot.sendMessage(chat_id,"<strong>" + first_name + "</strong>, "+set_new_carona()+"", parse_mode='HTML')
        return
    elif '/menu' in command:
        if chat_type == 'group' or chat_type == 'supergroup':
            markup = ReplyKeyboardMarkup(keyboard=[
                     [KeyboardButton(text=listar_caronas)],
                     [KeyboardButton(text=oferecer_carona)]
                 ], resize_keyboard=True, one_time_keyboard=True, selective=True)
        else:
            markup = InlineKeyboardMarkup(inline_keyboard=[
                     [InlineKeyboardButton(text=listar_caronas, callback_data=listar_caronas)],
                     [InlineKeyboardButton(text=oferecer_carona, callback_data=oferecer_carona)]
                 ])
        await bot.sendMessage(chat_id,'<strong>'+first_name+'</strong>, selecione qualquer item do menu:', reply_markup=markup, parse_mode='HTML',reply_to_message_id=msg['message_id'])
        return
    else:
        await reply_querys(chat_id, first_name, command)

async def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    chat_id = msg['message']['chat']['id']
    first_name = msg['from']['first_name']

    await reply_querys(chat_id,first_name, query_data, query_id)


async def reply_querys(chat_id, first_name, query_data, query_id=None):
    global oferecer_carona,listar_caronas
    if query_data == listar_caronas:
        if query_id != None:
            await bot.answerCallbackQuery(query_id,first_name+", " + get_caronas(),show_alert=True)
        await bot.sendMessage(chat_id,"<strong>" + first_name + "</strong>, " + get_caronas(), parse_mode='HTML',reply_markup=ReplyKeyboardHide())
    elif query_data == oferecer_carona:
        if query_id != None:
            await bot.answerCallbackQuery(query_id,first_name+", " + set_new_carona(),show_alert=True)
        await bot.sendMessage(chat_id,"<strong>" + first_name + "</strong>, " + set_new_carona(), parse_mode='HTML',reply_markup=ReplyKeyboardHide())
        #await bot.sendPhoto(chat_id, 'AgADAQAD87QxG_FKAgW731ne1kvXJ2CC5y8ABIgtN6sewlMVMsUAAgI')
        #await bot.sendLocation(chat_id, -5.088308, -42.810024)


if __name__ == '__main__':
    BOT_ID = settings.BOT_ID

    TOKEN = settings.TELEGRAM_API_KEY

    bot = telepot.async.Bot(TOKEN)
    answerer = telepot.async.helper.Answerer(bot)

    loop = asyncio.get_event_loop()
    loop.create_task(bot.message_loop({'chat': on_chat_message,
                                       'callback_query': on_callback_query}))
    print('Caronas Piaui Bot iniciado!')

    loop.run_forever()
