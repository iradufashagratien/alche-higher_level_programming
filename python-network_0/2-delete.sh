#!/bin/bash
# sends a DELETE request and displays the body of the response, retries if server isn't ready yet
curl -s --retry 5 --retry-delay 1 -X DELETE "$1"
