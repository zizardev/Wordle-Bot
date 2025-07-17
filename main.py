import asyncio
from aiogram import Bot, Dispatcher


from app.handlers import router


async def main():
    bot = Bot(token='8143853300:AAE9VbLh4gqVu38OtxjTXofO9X3ivMprpXk')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
    print("alo")


if __name__ == '__main__':
    try:
        print("alo")
        asyncio.run(main())        
    except KeyboardInterrupt:
        print('Бот остановлен юзером')
