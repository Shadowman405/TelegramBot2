from aiogram import Bot, Dispatcher

import config
from filters import IsOwnerFilter
from config import *

#init
bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

#activate filters
dp.filters_factory.bind(IsOwnerFilter)