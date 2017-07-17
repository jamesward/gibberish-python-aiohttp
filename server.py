import os
from aiohttp import web
import aiohttp
import asyncio

async def word():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://random-word.herokuapp.com") as response:
            return await response.text()

async def handle(request):
    async with aiohttp.ClientSession() as session:
        async with session.get("http://randnum.herokuapp.com") as response:
                num = int(await response.text())
                words = await asyncio.gather(*[word() for i in range(num)])
                return web.Response(text=" ".join(words))

app = web.Application()
app.router.add_get('/', handle)

port = port = int(os.environ.get("PORT", 8080))

web.run_app(app, port=port)

