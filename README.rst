Introduction
============

A module to automatically manage `aiohttp.ClientSession` objects for you
to improve performance.

The package manages a global cache of `aiohttp.ClientSession` objects based
on the host a particular request is connecting to so connections can be
reused between requests.

It also simplifies the API.


Usage
-----

The usage is similar to the python `requests` library::

    import aiohttp_client
    async with aiohttp_client.get('http://www.google.com') as resp:
        # do something here
