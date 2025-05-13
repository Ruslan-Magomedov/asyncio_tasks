# TODO: Создайте несколько асинхронных задач с разными задержками.
#  Используйте asyncio.as_completed() для обработки результатов задач по мере их завершения.
#  Выведите результаты каждой задачи сразу после ее завершения.


import asyncio
import random


async def wait_random():
    delay = random.randint(1, 5)
    await asyncio.sleep(delay)
    return f"Задача завершилась через {delay} секунд"


async def main():
    tasks = [asyncio.create_task(wait_random()) for _ in range(5)]

    for compiled in asyncio.as_completed(tasks):
        print(await compiled)


if __name__ == "__main__":
    asyncio.run(main())
