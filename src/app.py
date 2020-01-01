#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aiohttp import web

MIRROR_URL = 'https://npm.taobao.org/mirrors/python'
VERSION_MAP: dict = {}


def load_versions():
    global VERSION_MAP
    with open('src/versions.map', 'r') as fp:
        VERSION_MAP = {line.split(' ')[1].strip(): line.split(' ')[0] for line in fp.readlines() if line}


async def handle(request):
    name = request.match_info.get('sha2name')
    version = VERSION_MAP.get(name)
    if version is None:
        raise web.HTTPNotFound()

    raise web.HTTPFound(f'{MIRROR_URL}/{version}/Python-{version}.tgz')


load_versions()
app = web.Application()
app.add_routes([web.get('/{sha2name}', handle)])
