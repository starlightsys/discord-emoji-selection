#!/usr/bin/env nix-shell
#! nix-shell -p inotify-tools -i bash
inotifywait -m -e modify ./csv-reparse/ |
  while read -r filename event; do
    clear
    poetry run python -m csv-reparse
  done
