#!/usr/bin/env bash

echo > src/versions.map
for file in pyenv/plugins/python-build/share/python-build/*; do
  if [ -f "$file" ]; then
    basename="$(basename "$file")"
    sha2name="$(cat $file | grep 'Python-' | grep 'tgz' | awk -F '#' '{print $2}' | awk -F '"' '{print $1}')"
    sha2xzname="$(cat $file | grep 'Python-' | grep 'tar.xz' | awk -F '#' '{print $2}' | awk -F '"' '{print $1}')"
    if [ -n "$sha2name" ]; then
       if [ -n "$sha2xzname" ]; then
         echo $basename $sha2name $sha2xzname >> src/versions.map
       else
         echo $basename $sha2name >> src/versions.map
       fi
    fi
  fi
done
