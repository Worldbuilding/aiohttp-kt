import pytest

import aiohttp_kt as aiohttp
from aiohttp_kt import web
from aiohttp_kt.test_utils import TestClient as _TestClient
from aiohttp_kt.test_utils import TestServer as _TestServer


@pytest.fixture
def app(loop):
    async def handler(request):
        return web.Response(body=b"OK")

    app = web.Application(loop=loop)
    app.router.add_route('*', '/', handler)
    return app


async def test_server_context_manager(app, loop):
    async with _TestServer(app) as server:
        async with aiohttp.ClientSession(loop=loop) as client:
            async with client.head(server.make_url('/')) as resp:
                assert resp.status == 200


@pytest.mark.parametrize("method", [
    "head", "get", "post", "options", "post", "put", "patch", "delete"
])
async def test_client_context_manager_response(method, app, loop):
    async with _TestClient(app) as client:
        async with getattr(client, method)('/') as resp:
            assert resp.status == 200
            if method != 'head':
                text = await resp.text()
                assert "OK" in text
