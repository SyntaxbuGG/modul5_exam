from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.markdown import hbold
from sqlalchemy.orm import Session

from core.db.db_connect import engine, User, Messaglar

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    from sqlalchemy.orm import Session

    with Session(engine) as session:
        spongebob = User(
            user_telegram_id=message.from_user.id,
            username=message.from_user.username,
            created=message.date.today())

        session.add(spongebob)
        session.commit()

        await message.answer(f"Hello, {hbold(message.from_user.full_name)}!"
                             f"Bu bot habarlarni saklaydi ")


@router.message()
async def messages(message: Message):
    with Session(engine) as session:
        msg = Messaglar(
            text=message.text,
            created=message.date.today())
        session.add(msg)
        session.commit()

    await message.answer('Saqlandi')
