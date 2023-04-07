from aiogram import Bot, Dispatcher, executor, types

import python_weather



bot = Bot(token="API")
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL, locale="ru-RU")

@dp.message_handler()
async def echo(message: types.message):
    weather = await client.find(message.text)
    celsius = round((weather.current.temperature - 32) / 1.8)



    resp_msg = weather.location_name + "\n"
    resp_msg += f"Текущая температура: {celsius}°\n"
    resp_msg += f"Состояние погоды: {weather.current.sky_text}\n"
    resp_msg += f"Погода на неделю: \n"

    for forecast in weather.forecasts:
        resp_msg += f"{celsius}°|"
        resp_msg += f"{forecast.date}\n"


    await message.answer(resp_msg)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
