from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


import app.keyboard as kb


router = Router()


@router.message(CommandStart())
async def cmd_start(message):
    await message.answer('Привет, я Wordlet, давай сыграем', reply_markup = kb.main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку help')
