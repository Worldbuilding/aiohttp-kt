import pathlib

from aiohttp_kt import web

app = web.Application()
app.router.add_static('/', pathlib.Path(__file__).parent, show_index=True)

web.run_app(app)
