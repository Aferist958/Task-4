import asyncio

from aiohttp import ClientSession


async def weather(city):
    async with ClientSession() as session:
        url = f'http://api.weatherapi.com/v1/current.json?key=825f3541c21c4733b23120028240710&q={city}&aqi=no'
        params = {'q': city, 'APPID': '825f3541c21c4733b23120028240710'}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            return weather_json

async def main(city):
    task = asyncio.create_task(weather(city))
    result = await asyncio.gather(task)
    print(result)

city1 = input()

asyncio.run(main(city1))