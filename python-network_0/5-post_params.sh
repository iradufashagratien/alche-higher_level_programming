#!/bin/bash
# sends a POST request with email and subject params, retries if server isn't ready yet
curl -s --retry 5 --retry-delay 1 --retry-connrefused -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
