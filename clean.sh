#!/bin/sh
if find /var/tmp/pdfcache/ -mindepth 1 -print -quit 2>/dev/null | grep -q .;then
  for f in /var/tmp/pdfcache/*; do
    fuser -s "$f" || rm "$f"
  done
fi