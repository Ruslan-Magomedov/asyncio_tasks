# TODO: Напишите асинхронную программу, которая отправляет HTTP-запросы к трём различным веб-сайтам:
#  "https://www.yandex.com", "https://www.google.com" и "https://www.python.org".
#  Как только от одного из сайтов будет получен ответ,
#  необходимо отменить выполнение запросов к остальным сайтам
#  и вывести время, затраченное на получение первого ответа.


import asyncio
import aiohttp

import time


async def first_response():
    pass


async def main(links: list):
    tasks = [asyncio.create_task(first_response(link)) for link in links]

    for compiled in asyncio.as_completed(tasks):
        result = await compiled
        
        if result.done():
            pass


if __name__ == "__main__":
    web_links = [
        "https://www.yandex.com",
        "https://www.google.com",
        "https://www.python.org"
    ]
    asyncio.run(main())
 