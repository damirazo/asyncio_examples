import asyncio


@asyncio.coroutine
def operation(future):
    i = 0

    while True:
        yield from asyncio.sleep(1)
        print(i)
        i += 1

        if i == 5:
            future.set_result('Выполнение успешно завершено')
            # future.set_exception(RuntimeError('message'))
            break


def on_complete(future):
    print(future.result())


future = asyncio.Future()
future.add_done_callback(on_complete)

loop = asyncio.get_event_loop()
loop.run_until_complete(operation(future))