from aiogram import Router, types
from database import db

router = Router()


@router.callback_query(lambda c: c.data and c.data.startswith("role_"))
async def cb_set_role(callback: types.CallbackQuery):
    role = callback.data.split("_", 1)[1]
    user_id = callback.from_user.id
    await db.set_role(user_id, role)
    await callback.answer("Роль сохранена")
    await callback.message.answer(f"Вы выбрали роль: <b>{role}</b>")


def register_auth(dp):
    dp.include_router(router)