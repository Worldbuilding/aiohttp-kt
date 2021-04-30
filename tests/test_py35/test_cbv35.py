from unittest import mock

from aiohttp_kt import web
from aiohttp_kt.web_urldispatcher import View


async def test_render_ok():
    resp = web.Response(text='OK')

    class MyView(View):
        async def get(self):
            return resp

    request = mock.Mock()
    request.method = 'GET'
    resp2 = await MyView(request)
    assert resp is resp2
