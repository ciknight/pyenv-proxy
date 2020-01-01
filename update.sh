#!/usr/bin/env bash

echo > src/versions.map
for file in pyenv/plugins/python-build/share/python-build/*; do
  if [ -f "$file" ]; then
    basename="$(basename "$file")"
    sha2name="$(cat $file | grep 'Python-' | grep 'tgz' | awk -F '#' '{print $2}' | awk -F '"' '{print $1}')"
    if [ -n "$sha2name" ]; then
      echo $basename $sha2name >> src/versions.map
    fi
  fi
done
