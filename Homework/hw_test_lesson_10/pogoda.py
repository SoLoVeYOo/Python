import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

sayt = 'https://world-weather.ru/pogoda/russia/balakovo/'
zapros = requests.get(sayt)
soup = BeautifulSoup(zapros.text, 'html.parser')

def zapros_pogody(sayt, zapros, soup):

    for temp in soup.find_all('div', id = 'weather-now-number'):
        temp = temp.next

    for obl in soup.find_all('span', id = 'weather-now-icon'):
        obl = obl.get('title')

    for timew in soup.find_all('div', class_ = 'weather-now-info'):
        timew = timew.text[6:-3]

    for dr in soup.find_all('div', id = 'weather-now-description'):
        line = dr.text
        last_index = 0
        itog = []
        for i, char in enumerate(line[1:-9]):
            if char.istitle() or i == len(line[1:-10]):
                itog.append(line[last_index:i+1])
                last_index = i + 1
        itog.append(line[-10: -4])
        itog.append(line[-4:])
        dr = ' '.join(itog[:-5])

    send_tg = 'Погода в Балаково: ' + '\n' + temp + ' ' + obl + '\n' + dr + '\n' + 'Данные на: ' + timew

    return send_tg

def prognoz(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Prognoz {zapros_pogody(sayt, zapros, soup)}')

updater = Updater('TOKEN')

updater.dispatcher.add_handler(CommandHandler('prognoz', prognoz))

print('server start')
updater.start_polling()
updater.idle()