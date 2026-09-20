#!/bin/bash
# sends a GET request with a custom header, follows redirects, displays the body
curl -sL --retry 5 --retry-delay 1 --header "X-HolbertonSchool-User-Id: 98" "$1"
