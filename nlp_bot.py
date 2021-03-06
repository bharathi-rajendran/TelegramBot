# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 23:02:17 2020

@author: Bharathi Rajendran
""" 
import logging

from predict import prediction
from telegram.ext import Updater, MessageHandler, Filters


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def some_func(bot, update):
    pass
    if not update.effective_message.text:
        update.effective_message.reply_text(text = "Cannot handle given format, getting aware now")
    else:
        msg = update.effective_message.text
        update.effective_message.reply_text(text = prediction(msg))
        
def main():
    updater = Updater('1080386031:AAHOyT_1zFoik-vF-UuaJXoWK3o4xupaOh4')
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.all, some_func))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
