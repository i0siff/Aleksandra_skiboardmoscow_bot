from email import message
from typing import Text
import config
import string
import time 
from aiogram import  Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ParseMode

#from typing import Text
#import config
#import logging
#import aiogram
#import asyncio

import os, json, string
import keyboards as kb

bot = Bot(token=os.getenv('TOKEN'))

async def on_startup(_):
    print('Бот в сети')

# Диспетчер для бота
dp = Dispatcher(bot)

#Декоратор
@dp.message_handler(commands=['help'])
async def start_command(message : types.Message):
    await bot.send_message(message.from_user.id, "Понравился бот? \nХотите себе такого же? \n\nНапишите @i0siff - он поможет с разработкой ботов")

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    start_msg_1 = Text("*Что может делать этот бот* \nБот помогает ребятам и девушкам, которые ведут активный образ жизни. \nПодскажет чаты где люди ищут компанию на склоне и в оранизации прочих активностей 🛼🚴\n \n А так же, бот помогает админам следить за соблюдением правил в чатах.")
    
   #  first_msg_1 = 'Ставь в настройках своё имя, фото и заполняй тест.'
   #  first_msg_2 = 'Расскажи о себе и будь культурным. Мат и оскорбления запрещены (https://t.me/skiboardAFISHA/985)!'
   #  first_msg_3 = 'Пиши с хештегом слово #тест, через пробел имя и далее отвечай на вопросы:'

   #  form_msg_1 = '1. Дата и год рождения. Мы любим поздравлять)'
   #  form_msg_2 = '2. Умеешь ли ты готовить? Какое коронное блюдо?'
   #  form_msg_3 = '3. Есть парень/девушка?'
   #  form_msg_4 = '4. Размер деталек? (ахаха, понимай, как хочешь)'
   #  form_msg_5 = '5. Какой у тебя рост?'
   #  form_msg_6 = '6. Кем работаешь?'
   #  form_msg_7 = '7. Инстаграм.'
   #  form_msg_8 = '8. Где живёшь/район?'
   #  form_msg_9 = '9. На чём катаешь: 🏂или⛷?'
   #  form_msg_10 = '10. Другие твои спортивные активности и хобби.'
   #  form_msg_11 = '11. Где конкретно узнал(а) про чат?'
    

    await message.answer('Привет, ' +message.chat.first_name+ ' \nДобро пожаловать в секту =) ⛷🏂  \nПомни, не важно лыжник ты или сноубордист, главное, что Лыжебордер! 2017 ©', reply_markup=kb.Start_kb_markup1)
    #await bot.send_message(message.from_user.id, first_msg_1 + "\n" + first_msg_2 + "\n" + first_msg_3 + "\n \n" + form_msg_1 + "\n" + form_msg_2 + "\n" + form_msg_3 + "\n" + form_msg_4 + "\n" + form_msg_5 + "\n" + form_msg_6 + "\n" + form_msg_7 + "\n" + form_msg_8 + "\n" + form_msg_9 + "\n" + form_msg_10 + "\n" + form_msg_11 + "\n")
    #await message.answer(start_msg_1, parse_mode=ParseMode.MARKDOWN)
    await bot.send_message(message.from_user.id, "Понравился бот? \nХотите себе такого же? \n\nНапишите @i0siff - он поможет с разработкой ботов")

	
@dp.message_handler(commands=['mute'], is_chat_admin=True)
@dp.message_handler(lambda message: message.text.startswith("мут"), is_chat_admin=True)
async def mute(message):
      name1 = message.from_user.get_mention(as_html=True)
      if not message.reply_to_message:
         await message.reply("Не хватает аргументов!\nПример:\n`/мут 1 ч причина")
         return
      try:
         muteint = int(message.text.split()[1])
         mutetype = message.text.split()[2]
         comment = " ".join(message.text.split()[3:])
      except:
         await message.reply('Не правильно написано!\nПример:\n`/мут 1 ч причина`')
         return
      if mutetype == "ч" or mutetype == "час" or mutetype == "часов" or mutetype == "h":
         await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date=int(time.time()) + muteint*3600)
         await message.answer(f' <b> Нарушитель:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n<b>Вам запретил</b> {name1} отправлять сюда сообщения в течении ⏰  {muteint} {mutetype}\n<b>Причина:</b> {comment}',  parse_mode='html')
      elif mutetype == "мин" or mutetype == "м" or mutetype == "минут" or mutetype == "m":
         await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date=int(time.time()) + muteint*60)
         await message.answer(f' <b> Нарушитель:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n<b>Вам запретил</b> {name1} отправлять сюда сообщения в течении ⏰  {muteint} {mutetype}\n<b>Причина:</b> {comment}',  parse_mode='html')
 #     elif mutetype == "д" or mutetype == "дней" or mutetype == "день":
 #        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date=int(time.time()) + muteint*86400)
 #        await message.answer(f' | <b>Решение было принято:</b> {name1}\n | <b>Нарушитель:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | <b>Срок наказания:</b> {muteint} {mutetype}\n | <b>Причина:</b> {comment}',  parse_mode='html')




#КЛАВИАТУРА
@dp.message_handler(lambda message: message.text=="Горнолыжки Москвы и Подмосковья")
async def kb_moscow(message: types.Message):
    await message.answer("Горнолыжки Москвы и Подмосковья:", reply_markup=kb.inline_kb_moscow)

@dp.message_handler(lambda message: message.text=="Большие курорты")
async def kb_BigResorts(message: types.Message):
    await message.answer("Большие курорты:", reply_markup=kb.inline_kb_BigResorts)                 

@dp.message_handler(lambda message: message.text=="Чаты по темам")
async def kb_ChatsByTopic(message: types.Message):
    await message.reply("Раздел в разработке.")


#ПРИВЕТСТВИЕ НОВЕНЬКИХ В ЧАТЕ

chat_id_skiboardSWIM = int(-1001589723428)
chat_id_skiboardSOROCHANY = int(-1001184019127)
chat_1 = int(-1001808461901)

#Приветствие
@dp.message_handler(content_types=["new_chat_members"])
async def new_members_handler(message : types.Message):
    if message.chat.id == chat_1:
        name = message.new_chat_members[0]
#      await bot.reply(message.chat.id, f"Добро пожаловать, {name.mention}!. В чат 2222")
        await message.delete()
        await bot.send_message(message.chat.id, f' <a href="tg://user?id={message.new_chat_members[0].id}">{message.new_chat_members[0].first_name}</a>, Добро пожаловать!👋 \n \n👇 Правила чата и полезное здесь 👇 \n https://t.me/skiboardSOROCHANY/188360 ' , disable_web_page_preview=True,  parse_mode='html')
        
    elif message.chat.id == chat_id_skiboardSWIM:
 #     name = message.new_chat_members[0]
        await message.delete()
        await bot.send_message(message.chat.id, f'Добро пожаловать, <a href="tg://user?id={message.new_chat_members[0].id}">{message.new_chat_members[0].first_name}</a>, в чат! 🤗 \nНам будет интересно немного узнать о Вас ☺️ и о Ваших взаимных «отношениях» с плаванием 🏊🏻‍♀️🏊🏻' ,  parse_mode='html')
    elif message.chat.id == chat_id_skiboardSOROCHANY:
        await message.delete()
        await bot.send_message(message.chat.id, f' <a href="tg://user?id={message.new_chat_members[0].id}">{message.new_chat_members[0].first_name}</a>, Добро пожаловать!👋 \n \nПравила чата и полезное здесь👇 \n https://t.me/skiboardSOROCHANY/188360 ' , disable_web_page_preview=True,  parse_mode='html')
# 
#     else:
#      name = message.new_chat_members[0]
#      await message.reply(message.chat.id, f"Добро пожаловать, {name.mention}!")
#      await bot.send_message(message.chat.id, f"Добро пожаловать, {name.mention}!")




# @dp.message_handler()
# async def echo_send(message : types.Message):
#     await message.answer(message.text)


@dp.message_handler()
async def echo_send(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('МАТ ЗАПРЕЩЁН!\nСмотри правила:\nt.me/skiboardAFISHA/985', disable_web_page_preview=True)
        await message.delete()


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)