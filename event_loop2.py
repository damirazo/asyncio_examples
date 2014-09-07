import random
import string
import asyncio


def rand_letter():
    """Случайный символ из латинского алфавита"""
    return random.choice(string.ascii_lowercase)


@asyncio.coroutine
def coro1():
    while True:
        l1 = rand_letter()
        yield from coro2(l1)


@asyncio.coroutine
def coro2(l1):
    l2 = rand_letter()
    l2 += l1
    yield from coro3(l2)


@asyncio.coroutine
def coro3(l2):
    l3 = rand_letter()
    l3 += l2
    print('Result word: {}'.format(l3))
    print('-----------------------------')
    yield from asyncio.sleep(1)


loop = asyncio.get_event_loop()
loop.run_until_complete(coro1())