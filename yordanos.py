import requests
import logging
from telegram.ext import *
from telegram.ext import Updater, CommandHandler
import responses
def send_message_to_telegram_bot(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, params=params)
    updates_data = response.json()
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message.")
bot_token = "6856450947:AAFOacFQ7TrLxd3im1B-4F3_W2usiWmz5bQ"
chat_id = "959875626"
url = 'https://ethiopianhistory.com/'
response = requests.get(url)
content = response.content
from bs4 import BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')
category = soup.find_all('li', class_="list-group-item")
catli = [li.text for li in category[:5]]
print(catli)
scraped_data = '\n'.join(catli) 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('starting bot...')
def command1(update, context):
 messages = []
 for product_name in zip(catli):
    message = f"Product: {product_name} \n"
    messages.append(message)
 final_message = ''.join(messages)
 send_message_to_telegram_bot(bot_token, chat_id, final_message.strip())
def mess_handl(update, context):
   text = str(update.message.text).lower()
   logging.info(f'user ({update.message.chat.id}) sayes: {text}')
   update.message.reply_text(text)
def error(update, context):
   logging.error(f'update {update} cused error {context.error}')
if __name__ == '__main__':
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('command1', command1))
    dp.add_handler(MessageHandler(Filters.text, mess_handl))
    dp.add_error_handler(error)
    updater.start_polling(1.0)
    updater.idel()