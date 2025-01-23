from aiogram import Router, html, Bot, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, BotCommand, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main = Router()

class ButtonState(StatesGroup):
    category = State()


async def meny(bot: Bot) -> None:
    ls = [
        BotCommand(command='restart', description='restart'),
        BotCommand(command='info', description="Ma'lumot saqlaydigan bot")
    ]
    await bot.set_my_commands(ls)

@main.message(ButtonState.category, F.text == 'Back')
@main.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!")
    info = f"Siz bizning bot orqali rasm, video, hujjatlariz va boshqa turdagi ma'lumotlarizni saqlab qo'yishingiz mumkun!"
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text='File send'),
        KeyboardButton(text='Your file category')
    )
    rkb.adjust(2)
    rkb = rkb.as_markup(resize_keyboard=True)
    await message.answer(info, reply_markup=rkb)

@main.message(F.text == 'Your file category')
async def contact(message: Message, state :FSMContext) -> None:
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text='List images', request_contact=True),
        KeyboardButton(text='List videos', request_location=True),
        KeyboardButton(text='List documents'),
        KeyboardButton(text='List others'),
        KeyboardButton(text='Back')
    )
    rkb.adjust(2, 2, 1)
    rkb = rkb.as_markup(resize_keyboard=True)
    await state.set_state(ButtonState.category)
    await message.answer("Choose", reply_markup=rkb)


@main.message(F.text == 'File send')
async def contact(message: Message) -> None:
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text='Images'),
        KeyboardButton(text='Video'),
        KeyboardButton(text='Documents'),
        KeyboardButton(text='Others'),
    )
    rkb.adjust(2)
    rkb = rkb.as_markup(resize_keyboard=True)
    await message.answer(f'Chose', reply_markup=rkb)