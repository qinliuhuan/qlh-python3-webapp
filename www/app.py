import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

'''
异步函数通常被称作协程,
创建一个协程仅仅只需使用 async 关键字,
或者使用 @asyncio.coroutine 装饰器
'''
@asyncio.coroutine
def init(loop):
    app = web.Application(loop= loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(),
                                        '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000....')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()