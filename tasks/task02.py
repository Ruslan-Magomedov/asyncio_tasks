# TODO: Создайте 4 корутины, каждая из которых возвращает строку.
#  Запустите их параллельно и соберите результаты в список.


import asyncio
import random


async def get_string():
    ls = [
        "hello",
        "Python",
        "Rom",
        "Web",
        "Strong"
    ]
    return random.choice(ls)


async def main():
    result = await asyncio.gather(*[get_string() for _ in range(4)])
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
