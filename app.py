import telebot
import requests
import json
import random
from kbbi import KBBI


api = '1591355584:AAG-gjzmlYpuyZAZL3AB5NHC6lN__JwKEFM'
bot = telebot.TeleBot(api)
handlermsg = '''
Hai berikut menu dari bot ini!!
/waifu
/neko
/fortune
/loli
/anime
/hentai
/quotes

/donate
/reportBug
'''



@bot.message_handler(commands=['start'])
def send_welcome(message):
	nama = message.from_user.first_name
	bot.reply_to(message, 'Halo {} ada yang bisa saya bantu?\nKetik /menu untuk menggunakan bot ini'.format(nama))

@bot.message_handler(commands=['menu'])
def send_menu(message):
	bot.reply_to(message, handlermsg)

@bot.message_handler(commands=['fortune'])
def send_fortune(message):
	url = requests.get('http://yerkee.com/api/fortune')
	json = url.json()
	print(json)
	fortune = json['fortune']
	bot.reply_to(message, fortune)

@bot.message_handler(commands=['neko'])
def send_neko(message):
	urlneko = requests.get('https://arugaz.herokuapp.com/api/nekonime')
	jsonneko = urlneko.json()
	jadi = jsonneko["result"]
	bot.send_photo(message.chat.id, jadi)

@bot.message_handler(commands=['waifu'])
def send_waifu(message):
	urlwaifu = requests.get('https://arugaz.herokuapp.com/api/waifu')
	jsonwaifu = urlwaifu.json()
	waifu = jsonwaifu["image"]
	bot.send_photo(message.chat.id, waifu)

@bot.message_handler(commands=["loli"])
def loli(message):
	urlchar = requests.get('https://tobz-api.herokuapp.com/api/randomloli?apikey=BotWeA')
	jsonchar = urlchar.json()
	loli = jsonchar["result"]
	bot.send_photo(message.chat.id, loli)

@bot.message_handler(commands=["anime"])
def anime(message):
	urlanim = requests.get('https://tobz-api.herokuapp.com/api/randomanime?apikey=BotWeA')
	jsonanim = urlanim.json()
	anime = jsonanim["result"]
	bot.send_photo(message.chat.id, anime)

@bot.message_handler(commands=["hentai"])
def hen(message):
	urlhen = requests.get('https://tobz-api.herokuapp.com/api/hentai?apikey=BotWeA')
	jsonhen = urlhen.json()
	hentai = jsonhen["result"]
	bot.send_photo(message.chat.id, hentai)

@bot.message_handler(commands=["quotes"])
def quotes(message):
	urlq = requests.get('https://tobz-api.herokuapp.com/api/randomquotes?apikey=BotWeA')
	jsonq = urlq.json()
	q = jsonq["quotes"] 
	bot.reply_to(message.chat.id, q)

@bot.message_handler(commands=["donate"])
def donate(message):
	reply_to(message.chat.id, "Silahkan Donasi Ke \nhttps://trakteer.id/syn1901")

@bot.message_handler(commands=["reportBug"])
def report(message):
	reply_to(message.chat.id, "Report Ke => @Syn71")
	
print('bot sedang berjalan')
bot.polling()

