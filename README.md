# pyenv proxy

Download python acceleration in China

## How to run

### Update pyenv version map

```shell
# clone pyenv repo
$ git clone https://github.com/pyenv/pyenv.git
$ sh update_version_map.sh
```

### Run http server and set pyenv mirror url

```shell
$ pipenv install
$ python app.py
$ export PYTHON_BUILD_MIRROR_URL="http://127.0.0.1:10000"
$ pyenv install 3.11.9
```

```shell
$ curl --head http://127.0.0.1:10000/9b1e896523fc510691126c864406d9360a3d1e986acbda59cda57b5abda45b87

HTTP/2 301
location: https://cdn.npmmirror.com/binaries/python/3.11.9/Python-3.11.9.tar.xz
```

## Use pyenv.ibeats.top

```shell
export PYTHON_BUILD_MIRROR_URL="https://pyenv.ibeats.top"
```
