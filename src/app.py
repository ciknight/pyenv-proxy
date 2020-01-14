#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aiohttp import web

MIRROR_URL = "https://npm.taobao.org/mirrors/python"
VERSION_MAP: dict = {}


def load_versions():
    global VERSION_MAP
    with open("src/versions.map", "r") as fp:
        lines = [line.strip() for line in fp.readlines() if line.strip()]

    for line in lines:
        if len(line.split(" ")) == 3:
            version, sha2name, sha2xzname = line.split(" ")
            VERSION_MAP[sha2name] = (version, "tgz")
            VERSION_MAP[sha2xzname] = (version, "tar.xz")
        if len(line.split(" ")) == 2:
            version, sha2name = line.split(" ")
            VERSION_MAP[sha2name] = (version, "tgz")


async def handle(request):
    name = request.match_info.get("sha2name")
    version, suffix = VERSION_MAP.get(name, (None, None))
    if version is None:
        raise web.HTTPNotFound()

    raise web.HTTPFound(f"{MIRROR_URL}/{version}/Python-{version}.{suffix}")


load_versions()
app = web.Application()
app.add_routes([web.get("/{sha2name}", handle)])
