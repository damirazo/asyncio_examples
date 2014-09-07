import asyncio


@asyncio.coroutine
def coro():
    # печатаем список существующих задач
    print(asyncio.Task.all_tasks())
    yield from asyncio.sleep(3)

    # печатаем информацию о текущей задаче
    print(asyncio.Task.current_task())
    yield from asyncio.sleep(3)

    print('Hello, World!')


loop = asyncio.get_event_loop()

# В python 3.4.2+
# task = loop.create_task(coro)

task = asyncio.async(coro())
loop.run_until_complete(task)