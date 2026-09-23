#!/bin/bash
# follows redirects and displays the body only if the final status is 200
[ "$(curl -sL --retry 5 --retry-delay 1 --retry-connrefused -o /dev/null -w '%{http_code}' "$1")" = "200" ] && curl -sL --retry 5 --retry-delay 1 --retry-connrefused "$1"
