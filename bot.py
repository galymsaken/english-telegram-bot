import telebot
import os
import random



TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)



word_list = [
    {"word": "apple", "translate": "яблоко", "example": "I eat an apple every day."},
    {"word": "run", "translate": "бегать", "example": "She runs in the morning."},
    {"word": "book", "translate": "книга", "example": "This book is very interesting."},
    {"word": "dog", "translate": "собака", "example": "The dog is barking loudly."},
    {"word": "water", "translate": "вода", "example": "Drink more water every day."},
]



@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "👋 Привет! Я помогу тебе учить английские слова!\n"
                     "🧠 Используй команду /word для слова дня.\n"
                     "🔁 Используй команду /repeat для случайного слова.")



@bot.message_handler(commands=['word'])
def word_of_the_day(message):
    word = word_list[0]
    text = f"📘 Слово дня: *{word['word']}* — {word['translate']}\n" \
           f"_Пример_: {word['example']}"
    bot.send_message(message.chat.id, text, parse_mode="Markdown")



@bot.message_handler(commands=['repeat'])
def random_word(message):
    word = random.choice(word_list)
    text = f"🔁 Повторим: *{word['word']}* — {word['translate']}\n" \
           f"_Пример_: {word['example']}"
    bot.send_message(message.chat.id, text, parse_mode="Markdown")



bot.infinity_polling()
