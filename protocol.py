import asyncio


HOST = '127.0.0.1'
PORT = 5555


class EchoServer(asyncio.Protocol):
    def __init__(self):
        super().__init__()
        self.transport = None

    def connection_made(self, transport):
        """Вызывается при создании соединения"""
        self.transport = transport
        peername = self.transport.get_extra_info('peername')
        print("Установлено соединение с {}...".format(peername))

    def connection_lost(self, exc):
        """Вызывается при разъединении"""
        print("Соединение разорвано...")
        server.close()

    def data_received(self, data):
        """Вызывается при получении данных"""
        print('Получены данные: {}'.format(data))
        self.transport.write(b'echo:')
        self.transport.write(data)


loop = asyncio.get_event_loop()
server_gen = loop.create_server(EchoServer, HOST, PORT)
server = loop.run_until_complete(server_gen)

try:
    loop.run_forever()
finally:
    loop.close()
    server.close()