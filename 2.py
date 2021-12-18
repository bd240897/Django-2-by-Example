import time
import asyncio
from hashlib import md5
import aiohttp
import time
from random import randint
from hashlib import md5
from aiohttp import ClientSession


# мои тестовые данные
urls = ["http://python.org", "http://microsoft.com", "http://python.org"]
base_url = "https://nocvko-python.mocklab.io/delayed/"
numbers = [randint(1, 8) for _ in range(4)]
urls = [base_url + str(number) for number in numbers]


async def make_request(url):
    """Делает 1 запрос на сайт"""
    async with aiohttp.request('GET', url) as response:
        r = await response.json() # преобразуем в json
        return r['message'] # вытащим поле message из json


async def make_many_requests(urls):
    """Делаем несколько асинхр запросов"""
    tasks = [] # лист задача
    for url in urls:
        task = asyncio.ensure_future(make_request(url)) # создали задачу и обрнули ее в крутину
        tasks.append(task)
    results = await asyncio.gather(*tasks) # запустили параельно задачи
    return results

def count_hash(urls):
    """Главная функция"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    results = loop.run_until_complete(make_many_requests(urls))

    s = "".join(sorted(results)).encode('utf-8')
    return md5(s).hexdigest()


## Тест 1 - через главную функцию
# count_hash(urls)

## Тест 2 - запускал до этого так
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# # tasks = [loop.create_task(make_request("https://nocvko-python.mocklab.io/delayed/1"))]
# # loop.run_until_complete(asyncio.wait(tasks))
# loop.run_until_complete(count_hash(urls))

## Тест 3
base_url = "https://nocvko-python.mocklab.io/delayed/"
def test():
    numbers = [randint(1, 8) for _ in range(4)]
    max_time = sum(numbers)
    urls = [base_url + str(number) for number in numbers]
    begin = time.time()
    result = count_hash(urls)
    end = time.time()
    assert begin - end < max_time, "Время исполнения запроса превысило ожидание. Вероятно, запросы выполняются не параллельно"
    result_strings = sorted([f"delayed_{i}000" for i in numbers])
    result_string = "".join(result_strings).encode('utf-8')
    assert result == md5(result_string).hexdigest()

if __name__ == "__main__":
    test()