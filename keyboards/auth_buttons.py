from aiogram.utils.keyboard import InlineKeyboardBuilder


def role_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="Заказчик", callback_data="role_customer")
    kb.button(text="Водитель", callback_data="role_driver")
    kb.adjust(2)
    return kb.as_markup()