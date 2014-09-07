import asyncio


@property
def event_loop():
    # return asyncio.get_event_loop_policy().get_event_loop()
    return asyncio.get_event_loop()


class CustomEventLoopPolicy(asyncio.DefaultEventLoopPolicy):
    """ Измененная политика
    для фиксирования обращения к методу get_event_loop
    """

    def get_event_loop(self):
        loop = super().get_event_loop()
        print('Зафиксировано обращение к Event Loop Policy')

        return loop


# Установка измененной политики
asyncio.set_event_loop_policy(CustomEventLoopPolicy())


@asyncio.coroutine
def task():
    yield from asyncio.sleep(2)
    print('Hello, World!')

loop = asyncio.get_event_loop()
loop.run_until_complete(task())