import asyncio


async def count(counter):
    print(f'Количество записей в списке: {len(counter)}')

    while True:
        await asyncio.sleep(1 / 1000)
        counter.append(1)


async def print_every_one_sec(counter):
    while True:
        await asyncio.sleep(1)
        print(f'- 1 секунда прошла.', f'Количество записей в списке: {len(counter)}')


async def print_every_5_sec():
    while True:
        await asyncio.sleep(5)
        print(f'---- 5 секунд прошло.')


async def print_every_10_sec():
    while True:
        await asyncio.sleep(10)
        print(f'-------- 10 секуна прошло.')


async def main():
    counter = list()

    tasks = [
        count(counter),
        print_every_one_sec(counter),
        print_every_5_sec(),
        print_every_10_sec()
    ]

    await asyncio.gather(*tasks)

asyncio.run(main())
