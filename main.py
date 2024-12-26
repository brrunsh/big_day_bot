from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import asyncio
import requests

TOKEN = '7313642733:AAGnbhTJal_kjBCih9SjenzXwA-X-O8ekMw'
bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
        await message.answer("Привет! Напиши мне название города и я пришлю сводку погоды.")

@dp.message(F.text)
async def get_weather(message: types.Message):
      city = message.text
      weather_token = 'a34cac9284a83607bdc1672949c0330e'
      try:
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}'
            weather_data = requests.get(url).json()
            print(json.dumps(weather_data, indent=2, ensure_ascii=False))

            temperature = weather_data['current']['temp_c']
            temperature_feels = weather_data['current']['feelslike_c']
            wind_speed = weather_data['current']['wind_kph']
            cloud_cover = weather_data['current']['cloud']
            humidity = weather_data['current']['humidity']

            await message.answer(f'Температура воздуха: {temperature}°C\n'
                                 f'Ощущается как: {temperature_feels}°C\n'
                                 f'Ветер: {wind_speed} м/c\n'
                                 f'Облачность: {cloud_cover}\n'
                                 f'Влажность: {humidity}%')


      except KeyError:
            await message.answer(f'Не удалось определить город: {city}')
            
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
      asyncio.run(main())
