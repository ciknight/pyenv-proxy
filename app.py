# -*- coding: utf-8 -*-
import json

from aiohttp import web

MIRROR_URL = "https://cdn.npmmirror.com/binaries/python"
VERSION_MAP: dict = {}


def load_versions():
    global VERSION_MAP
    with open("versions.map", "r") as fp:
        lines = [line.strip() for line in fp.readlines() if line.strip()]

    for line in lines:
        if len(line.split(" ")) == 3:
            version, sha2name, sha2xzname = line.split(" ")
            VERSION_MAP[sha2name] = (version, "tgz")
            VERSION_MAP[sha2xzname] = (version, "tar.xz")
        if len(line.split(" ")) == 2:
            version, sha2name = line.split(" ")
            VERSION_MAP[sha2name] = (version, "tgz")

    with open("versions.json", "w") as fp:
        json.dump(VERSION_MAP, fp)

    return VERSION_MAP


async def handle(request):
    name = request.match_info.get("sha2name")
    version, suffix = VERSION_MAP.get(name, (None, None))
    if version is None:
        raise web.HTTPNotFound()

    raise web.HTTPFound(f"{MIRROR_URL}/{version}/Python-{version}.{suffix}")


load_versions()

app = web.Application()
app.add_routes([web.get("/{sha2name}", handle)])

if __name__ == "__main__":
    web.run_app(app, port=10000)
