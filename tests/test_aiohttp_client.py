

import aiohttp_client
import lru


async def test_session_is_reused_across_calls():
    async with aiohttp_client.get('https://o.onna.io') as resp:
        assert resp.status == 200

    async with aiohttp_client.get('https://o.onna.io') as resp:
        assert resp.status == 200

    assert len(aiohttp_client._sessions) == 1

    resp = await aiohttp_client.get('https://www.google.com')
    assert resp.status == 200
    assert len(aiohttp_client._sessions) == 2

    resp = await aiohttp_client.get('https://www.google.com')
    assert resp.status == 200
    assert len(aiohttp_client._sessions) == 2

    assert aiohttp_client._counts['o.onna.io'] == 2
    assert aiohttp_client._counts['www.google.com'] == 2


async def test_sessions_are_purged_on_max_number_of_sessions():
    aiohttp_client._sessions = lru.LRU(
        1, callback=aiohttp_client.session_purged)

    resp = await aiohttp_client.get('https://o.onna.io')
    assert resp.status == 200

    sess = aiohttp_client.get_session('https://o.onna.io')
    resp = await aiohttp_client.get('https://www.google.com')
    assert resp.status == 200

    assert sess.closed == True

    # restore original
    aiohttp_client._sessions = lru.LRU(
        aiohttp_client._max_number_sessions,
        callback=aiohttp_client.session_purged
    )


async def test_session_is_closed_on_max_requests():
    old = aiohttp_client._max_requests
    aiohttp_client._max_requests = 1
    sess = aiohttp_client.get_session('https://o.onna.io')
    _ = await aiohttp_client.get('https://o.onna.io')
    _ = await aiohttp_client.get('https://o.onna.io')
    assert sess.closed
    # restore original
    aiohttp_client._max_requests = old