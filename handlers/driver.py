from aiogram import Router, types
from aiogram.filters import Command
from database import db

router = Router()


@router.message(Command("me"))
async def cmd_me(message: types.Message):
    # показать роль/машину
    cur = await db.db.execute(
        "SELECT role, car_model, active_order FROM users WHERE user_id = ?",
        (message.from_user.id,)
    )
    row = await cur.fetchone()
    if row:
        await message.answer(
            f"Роль: {row[0]}\nМашина: {row[1]}\nАктивный заказ: {row[2]}"
        )
    else:
        await message.answer("Вы не зарегистрированы. Нажмите /start и выберите роль.")


def register_driver(dp):
    dp.include_router(router)