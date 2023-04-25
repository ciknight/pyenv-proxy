pyenv proxy

Accelerate pyenv download python

---

## Run

### Update pyenv version map

```
# clone pyenv repo
$ git clone https://github.com/pyenv/pyenv.git
$ sh update_version_map.sh
```

### Run server and set pyenv proxy

```
$ pipenv install
$ python app.py

$ export PYTHON_BUILD_MIRROR_URL="http://127.0.0.1:10000"
$ pyenv install 3.11.3
```

## Using

```
export PYTHON_BUILD_MIRROR_URL="https://pyenv.ibeats.top"
```
