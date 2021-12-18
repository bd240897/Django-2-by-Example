import time
import asyncio
from hashlib import md5
import aiohttp
import time
from random import randint
from hashlib import md5

# Источник: https://tonais.ru/library/asinhronnoe-programmirovanie-dlya-veb-razrabotki-v-python

# urls = ["http://python.org", "http://microsoft.com", "http://python.org"]
base_url = "https://nocvko-python.mocklab.io/delayed/"
numbers = [randint(1, 8) for _ in range(1)]
urls = [base_url + str(number) for number in numbers]


async def make_request(url, results=None):
    async with aiohttp.request('GET', url) as response:
        await response.headers["Matched-Stub-Name"]
        headers = response.headers["Matched-Stub-Name"]
        print(headers)
        # results.append(headers)

async def count_hash(urls):
    results = []
    # await asyncio.gather(*[make_request(url, results) for url in urls])
    await make_request(urls, results)
    print(results)
    # s = "".join(sorted(results)).encode('utf-8')
    # return md5(s).hexdigest()

def get_or_create_loop():
    loop = asyncio.get_event_loop()
    if loop.is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop

loop = get_or_create_loop()
tasks = [loop.create_task(make_request("https://nocvko-python.mocklab.io/delayed/1"))]
loop.run_until_complete(asyncio.wait(tasks))



#
#
# def test():
#     numbers = [randint(1, 8) for _ in range(4)]
#     max_time = sum(numbers)
#     urls = [base_url + str(number) for number in numbers]
#     begin = time.time()
#     result = count_hash(urls)
#     end = time.time()
#     assert begin - end < max_time, "Время исполнения запроса превысило ожидание. Вероятно, запросы выполняются не параллельно"
#     result_strings = sorted([f"delayed_{i}000" for i in numbers])
#     result_string = "".join(result_strings).encode('utf-8')
#     assert result == md5(result_string).hexdigest()
#
# if __name__ == "__main__":
#     test()