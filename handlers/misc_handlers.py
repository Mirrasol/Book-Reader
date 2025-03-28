from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def process_unknown(message: Message):
    await message.answer('Такую команду книжному боту не под силу понять.')
