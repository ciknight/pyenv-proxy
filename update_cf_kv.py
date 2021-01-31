#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 andy <andy@andys-Air.lan>
#
# Distributed under terms of the MIT license.
from src.app import load_versions
import os

namespace_id = ""


versions = load_versions()
for k, v in versions.items():
    os.system(f"wrangler kv:key put --namespace-id={namespace_id} {k} '{v}'")
    raise Exception()
