/*
 * index.js
 * Copyright (C) 2021 andy <andy@andys-Air.lan>
 *
 * Distributed under terms of the MIT license.
 */
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

MIRROR_URL = "https://cdn.npm.taobao.org/dist/python"
statusCode = 301

/**
 * Respond to the request
 * @param {Request} request
 */
async function handleRequest(request) {
  const url = new URL(request.url)
  sha2name = url.pathname.replace("/", "")
  config = JSON.parse(await PYENV_PROXY.get("config"))
  version = config[sha2name][0]
  suffix = config[sha2name][1]
  return Response.redirect(MIRROR_URL + "/" + version + "/Python-" + version + "." + suffix, statusCode)
}
