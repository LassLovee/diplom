import requests
import telebot
import time
import sys
from bs4 import BeautifulSoup as BS 
pas = 1
papa = "341918490"
block = 1
bot = telebot.TeleBot("1018084294:AAEernK_NQQIUreX331NMEITUVbBiRwqFZ4")
@bot.message_handler(commands=['start'])
def main(message):
#	global block
	bot.send_message(message.chat.id, "Привіт, " + message.from_user.first_name + "\nЯ бот, створений @LassLovee, для пошуку інформації." )
	bot.send_message(message.chat.id, "Твій ID: " + str(message.chat.id))	
#	message = 0
#	time.sleep(2)
#	@bot.message_handler(content_types=['text'], block = 0)
#	def main(message):
#		global block
#		if block == 0:
#			global papa
#			papa = message.text
#			block = 1
#			print (papa)		
#			bot.send_message(message.chat.id, "Добавлено")
#			return papa, block
#
#		else: 
#			bot.send_message(message.chat.id, "Айди попечителя уже введен, для изменения напишите моему создателю @LassLovee")	
##			message = 0
##			time.sleep(2)
##			@bot.message_handler( content_types=['text'])
##			def main2(message):
##				print("123")
##				if message.text == "1488":
##					global papa
#					global block
#					papa = message.text
#					block = 1
#					print (papa)
#					return papa, block
#					bot.send_message(message.chat.id, "Айди изменен")
#				else: 
#					bot.send_message(message.chat.id, "пароль не верный")


@bot.message_handler(commands=['add'])
def main(message):

	global block
	if block == 1:
		global papa
		add=message.text
		print( add[5:])
		papa = add[5:]
		bot.send_message(message.chat.id, "ID додано")
		block = 0
		return papa
	else:
		bot.send_message(message.chat.id, "ID вже введено")

@bot.message_handler(commands=['switch'])
def main(message):

	global papa
	print (papa)
	print (message.chat.id)
	if str(message.chat.id) == str(message.chat.id):
		global pas
		if pas == 1:
			pas = 0
			bot.send_message(papa, "Пошук вимкено")
		else:
			pas = 1
			bot.send_message(papa, "Пошук увімкнено")
		print (pas)
		return pas
	else:
		bot.send_message(message.chat.id, "Отказано в доступе")

@bot.message_handler(content_types=['sticker'])
def main(message):

	print(message.chat.id)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def main(message):
	global pas
	if pas == 1:

		global papa
		print(message.from_user.first_name)
		ans = message.text
		html1 = 0
		home2 = 0
		if ans == "Наркотики" or ans == "наркотики" or ans == "?":

			bot.send_message(papa, "Користувач шукає " + str(ans))
			print("Сработала защита")
			print(pas)
			bot.send_message(message.chat.id, "Нічого не знайдено")

			return
		bot.send_message(papa, "Користувач шукає: " + str(ans))
		ans = ans.replace(" ", "_")
		r = requests.get('https://ru.wiktionary.org/wiki/'+ans)
		html = BS(r.content, 'html.parser')
		for link in html.find_all(class_="mw-parser-output"):
			for home in link.find_all("ol", limit=1):
				for home1 in home.find_all("li", limit=1):
					html1 = home1.get_text()
					html1 = html1.replace("[≈ 1][≠ 1][▲ 1][▼ 1]", "")	
				for home2 in home.find_all("li", limit=2):
					html2 = home2.get_text()
					html2 = html2.replace("[≈ 2][≠ 2][▲ 2][▼ 2]", "")	
				for home3 in home.find_all("li", limit=3):
					html3 = home3.get_text()
					html3 = html3.replace("[≈ 3][≠ 3][▲ 3][▼ 3]", "")	
		print(ans)
		#print(link)
		if bool(html1) == 0:
			bot.send_message(message.chat.id, "Нічого не знайдено")
		else:
			bot.send_message(message.chat.id, "Знайдена інформація:\n" + str(html1))
			time.sleep(1)
			if bool(html2) == 0:
				bot.send_message(message.chat.id, "На этом все, определение может зависить от употребления заглавных букв, не рекомендую использовать их")
			else:	
				bot.send_message(message.chat.id, "Друге визначення:\n" + str(html2))
				time.sleep(1)
				if bool(html3) == 0:
					bot.send_message(message.chat.id, "На этом все, определение может зависить от употребления заглавных букв, не рекомендую использовать их")
				else:	
					bot.send_message(message.chat.id, "Третє визначення:\n" + str(html3))
			#time.sleep(1)
			#bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAICzl5zjgrRfCVT-QcMkETYdzP5XInSAAJrAANUBmIB62khzUkNwN8YBA')
	else: 
		bot.send_message(message.chat.id, "Пошук вимкено")
	#bot.send_message(message.chat.id, html[dlina*60::dlina*60])
	time.sleep(5)
	#bot.send_message(308927749, html[dlina*120:])

@bot.message_handler(content_types=['voice'])
def main(message):

	print("В розробці")
	bot.send_message(message.chat.id, "Голосове керування в розробці")

bot.polling(none_stop=True, interval=1)

#while True:
#	try:
		
#	except:
#		print("Net Error")
#		time.sleep(1)