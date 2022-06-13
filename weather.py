
import python_weather
import asyncio

async def getweather():

    client = python_weather.Client(format=python_weather.IMPERIAL, locale="ru-RU")


    weather = await client.find("Ростов на дону, Россия")

    celsius = (weather.current.temperature - 32) / 1.8
    print(str(round(celsius)) + "°")
    print(weather.current.sky_text)
    print(weather.location_name)


    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())