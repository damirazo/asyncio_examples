import re
import asyncio
import aiohttp


RE_TITLE = re.compile('<h1 class="title">\s+<a.+?>(.+?)</a>\s+</h1>', re.M)


@asyncio.coroutine
def task(page=1):
    response = yield from aiohttp.request(
        'GET', 'http://habrahabr.ru/page{}/'.format(page))

    if response.status == 200:
        body = yield from response.read()
        titles = RE_TITLE.findall(body.decode())

        for title in titles:
            print('Page {}: {}\n'.format(page, title))

    response.close()


loop = asyncio.get_event_loop()

tasks = [
    # Для python 3.4.2+
    # loop.create_task(task(1)),
    # loop.create_task(task(2)),
    # loop.create_task(task(3)),
    # loop.create_task(task(4)),
    # loop.create_task(task(5)),

    asyncio.async(task(1)),
    asyncio.async(task(2)),
    asyncio.async(task(3)),
    asyncio.async(task(4)),
    asyncio.async(task(5)),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()