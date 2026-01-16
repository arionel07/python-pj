import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from openai import OpenAI


logging.basicConfig(level=logging.INFO)

# create 2 varible for chatbot api and for openai api and past in client openai and bot bot

#client = OpenAI(api_key="")

#bot = Bot(token="")
dp = Dispatcher()

@dp.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer(
        "👋 Привет!\n\n"
        "Я бот arionel 🤖\n"
        "Напиши /chat и свой вопрос, и я отвечу."
    )

@dp.message(Command('chat'))
async def chat_handler(message: types.Message):
    prompt = message.text.replace("/chat", "").strip()

    if not prompt:
        await message.answer("Напиши текст после команды /chat")
        return
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"user", "content": prompt}
        ]
    )

    await message.answer(response.choices[0].message.content)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())