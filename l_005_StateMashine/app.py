if __name__ == '__main__':
    from aiogram import executor
    from src.teleBot.aiogram._005_StateMashine.handlers.users.testing import dp, send_to_admin

    executor.start_polling(dp, on_startup=send_to_admin)