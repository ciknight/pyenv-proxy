# -*- coding: utf-8 -*-
import json

from app import load_versions


versions = load_versions()

with open("versions.json", "w") as fp:
    json.dump(versions, fp)
