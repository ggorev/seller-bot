from aiogram.types import Message

from filters import IsUser
from loader import db, dp
from .menu import delivery_status


@dp.message_handler(IsUser(), text=delivery_status)
async def process_delivery_status(message: Message):
    orders = db.fetchall("SELECT * FROM orders WHERE cid=?", (message.chat.id,))
    if len(orders) == 0:
        await message.answer("У Вас нет активных заказов.")
    else:
        await delivery_status_answer(message, orders)


async def delivery_status_answer(message, orders):
    res = ''

    for order in orders:
        res += f"Заказ <b>№{order[3]}</b>"
        answer = [
            ' лежит на складе.',
            ' уже в пути!',
            ' прибыл и ждет вас на почте!'
        ]
        res += answer[0]
        res += "\n\n"
    await message.answer(res)
