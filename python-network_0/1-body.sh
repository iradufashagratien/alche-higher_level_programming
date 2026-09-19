#!/bin/bash
# displays the body of the response only when the status code is 200
[ "$(curl -s -o /dev/null -w '%{http_code}' "$1")" = "200" ] && curl -s "$1"
