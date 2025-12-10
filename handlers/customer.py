from aiogram import Router, types
from database import db

router = Router()


@router.message()
async def customer_flow(message: types.Message):
    # Если пользователь — в сессии, обработаем шаги.
    # Здесь можно вставить простую реализацию: если role == customer и нет сессии, начать ввод заказа.
    # Для краткости — если пользователь написал текст и role==customer — просто сохраняем как заказ (упрощённо).
    user = await db.db.execute("SELECT role FROM users WHERE user_id = ?", (message.from_user.id,))
    row = await user.fetchone()
    role = row[0] if row else None
    if role == "customer":
        # упрощённо сохраняем как новый order с cargo=message.text
        cur = await db.db.execute(
            "INSERT INTO orders (customer_id, cargo, status, phone) VALUES (?, ?, ?, ?)",
            (message.from_user.id, message.text, "open", "")
        )
        await db.db.commit()
        await message.answer("Заказ сохранён (упрощенно). Спасибо!")
    # если не заказчик — пропускаем


def register_customer(dp):
    dp.include_router(router)

# Примечание: customer.py здесь простая — позже можно заменить более точной пошаговой сессией.