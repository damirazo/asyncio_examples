import re
import asyncio
import aiohttp


RE_TITLE = re.compile('<h1 class="title">\s+<a.+?>(.+?)</a>\s+</h1>', re.M)


@asyncio.coroutine
def task():
    response = yield from aiohttp.request('GET', 'http://habrahabr.ru/')

    if response.status == 200:
        body = yield from response.read()
        titles = RE_TITLE.findall(body.decode())

        for title in titles:
            print(title + '\n')

    response.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(task())