#!/bin/bash
# displays all HTTP methods the server accepts, retries if server isn't ready yet
curl -s --retry 5 --retry-delay 1 -X OPTIONS -I "$1" | grep -i "^Allow:" | cut -d' ' -f2- | tr -d '\r'
