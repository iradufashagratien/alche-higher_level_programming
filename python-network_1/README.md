# python-network_1

Python scripts using urllib (tasks 0-3) and requests (tasks 4-10) to interact
with HTTP servers: fetching status, reading response headers, sending POST
data, handling HTTP errors, parsing JSON responses, and using GitHub Basic
Authentication.

## Requirements
- Python 3.4.3 style compatible
- PEP 8 (pycodestyle 1.7)
- Every file starts with #!/usr/bin/python3
- Every file is executable
- Every module is documented

## Files
- 0-hbtn_status.py   : fetches intranet status using urllib
- 1-hbtn_header.py   : displays X-Request-Id header using urllib
- 2-post_email.py    : sends a POST with an email using urllib
- 3-error_code.py    : handles HTTPError and prints error code, urllib
- 4-hbtn_status.py   : fetches intranet status using requests
- 5-hbtn_header.py   : displays X-Request-Id header using requests
- 6-post_email.py    : sends a POST with an email using requests
- 7-error_code.py    : prints error code for status >= 400, requests
- 8-json_api.py      : POSTs a letter, parses JSON search results
- 10-my_github.py    : fetches GitHub user id via Basic Authentication
