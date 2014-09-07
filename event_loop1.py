import asyncio

loop = asyncio.get_event_loop()


def coro():
    i = 0

    while True:
        print(i)
        yield from asyncio.sleep(1)

        if i == 5:
            break

        i += 1


# loop.run_until_complete(coro())


asyncio.async(coro())
loop.run_forever()