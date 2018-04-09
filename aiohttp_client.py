import aiohttp
import asyncio
import lru
import os
import urllib.parse


# max # of requests per session
_max_requests = int(os.environ.get('AIOHTTP_SESSION_MAX_REQUESTS', '5000'))
_max_number_sessions = int(os.environ.get('AIOHTTP_SESSION_SIZE', '100'))

def session_purged(key, value):
    asyncio.ensure_future(value.close())


_sessions = lru.LRU(_max_number_sessions, callback=session_purged)
_counts = {}


def get_session(url):
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc not in _sessions:
        _sessions[parsed.netloc] = aiohttp.ClientSession()
        _counts[parsed.netloc] = 0
    if _counts[parsed.netloc] > _max_requests:
        asyncio.ensure_future(_sessions[parsed.netloc].close())
        _sessions[parsed.netloc] = aiohttp.ClientSession()
        _counts[parsed.netloc] = 0
    _counts[parsed.netloc] += 1
    return _sessions[parsed.netloc]


async def close():
    for session in _sessions.values():
        await session.close()
    _sessions.clear()
    _counts.clear()


def post(url, *args, **kwargs):
    session = get_session(url)
    return session.post(url, *args, **kwargs)


def get(url, *args, **kwargs):
    session = get_session(url)
    return session.get(url, *args, **kwargs)


def patch(url, *args, **kwargs):
    session = get_session(url)
    return session.patch(url, *args, **kwargs)


def delete(url, *args, **kwargs):
    session = get_session(url)
    return session.delete(url, *args, **kwargs)


def head(url, *args, **kwargs):
    session = get_session(url)
    return session.head(url, *args, **kwargs)


def put(url, *args, **kwargs):
    session = get_session(url)
    return session.put(url, *args, **kwargs)


def options(url, *args, **kwargs):
    session = get_session(url)
    return session.options(url, *args, **kwargs)
