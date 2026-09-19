#!/bin/bash
# displays the body of the response only when the status code is 200, retries if server isn't ready yet
[ "$(curl -s --retry 5 --retry-delay 1 --retry-connrefused -o /dev/null -w '%{http_code}' "$1")" = "200" ] && curl -s "$1"
