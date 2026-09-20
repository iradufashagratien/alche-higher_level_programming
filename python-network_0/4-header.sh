#!/bin/bash
# sends a GET request with a custom header, displays the body, retries if server isn't ready yet
curl -s --retry 5 --retry-delay 1 -H "X-HolbertonSchool-User-Id: 98" "$1"
