from l_001_first_bot.handlers import send_to_admin
from l_005_StateMashine.loader import dp

if __name__ == '__main__':
    from aiogram import executor


    executor.start_polling(dp, on_startup=send_to_admin)