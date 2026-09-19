#!/bin/bash
# displays the size in bytes of the body of the response, retries if server isn't ready yet
curl -s --retry 5 --retry-delay 1 --retry-connrefused -o /dev/null -w "%{size_download}\n" "$1"
