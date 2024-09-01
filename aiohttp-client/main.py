import aiohttp
import asyncio

async def fetch(url, num):
    async with aiohttp.ClientSession() as session:
        print(f"Отправляю запрос через асинхронный http, запрос по счету: {num}")
        async with session.get(url) as response:
            return await response.json()

async def main():
    url = 'http://0.0.0.0:8000/example-api/products/'

    results = await asyncio.gather(*(fetch(url+str(num), num) for num in range(100)))

    for result in results:
        print(result)

if __name__ == '__main__':
    asyncio.run(main())
