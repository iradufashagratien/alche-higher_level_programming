#!/bin/bash
# follows redirects and displays the body only if the final status is 200
[ "$(curl -sL --retry 5 --retry-delay 1 -o /dev/null -w '%{http_code}' "$1")" = "200" ] && curl -sL --retry 5 --retry-delay 1 "$1"
