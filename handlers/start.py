from aiogram import Router, types
from aiogram.filters import CommandStart
from keyboards.auth_buttons import role_keyboard

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет! Выбери роль:", reply_markup=role_keyboard())


def register_start(dp):
    dp.include_router(router)