import logging
from aiogram import Bot, Dispatcher, executor, types
from tok_save import toks
import os

PATH = os.path.abspath(__file__+"/../..")

print(PATH)

try:
    from tokns import tok
except:
    tok = input("Введите токен.")
    toks(tok)