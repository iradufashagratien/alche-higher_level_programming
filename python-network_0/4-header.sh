#!/bin/bash
# sends a GET request with a custom header, displays the body of the response
curl -H "X-HolbertonSchool-User-Id: 98" "$1" -s
