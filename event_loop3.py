import asyncio


def task(num):
    print('test {}'.format(num))


loop = asyncio.get_event_loop()

loop.call_later(3, task, 1)
loop.call_soon(task, 2)

loop.run_forever()