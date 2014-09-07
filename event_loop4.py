import asyncio


loop = asyncio.get_event_loop()


def func():
    print('{}: test'.format(loop.time()))


def set_interval(timeout, callback, *args, **kwargs):
    """Эквивалент функции setInterval из javascript"""
    callback(*args, **kwargs)
    loop.call_later(timeout, set_interval, timeout, callback, *args, **kwargs)

    if not loop.is_running():
        loop.run_forever()


set_interval(3, func)