'''Одновременное выполнение функций'''
import time
import asyncio



async def f1(n: int):
    print(n * 10)
    await asyncio.sleep(3)
    print(f'Функция F1 закончила работу')

async def f2(n: int):
    print(n ** 2)
    await asyncio.sleep(2)
    print(f'Функция F2 закончила работу')

async def main():
    # f1(5)
    # f2(10)
    tasks1 = asyncio.create_task(f1(5))
    tasks2 = asyncio.create_task(f2(10))
    await tasks1
    await tasks2

if __name__ == '__main__':
    start = time.time()
    # main()
    asyncio.run(main())
    stop = time.time()
    print(f'Время выполнения: {stop - start:.2f} сек.')

