# python-network_0

Bash scripts using curl to interact with a web server: checking response
size, retrieving response bodies conditionally on status code, sending
DELETE and POST requests, sending custom headers, and listing allowed
HTTP methods.

## Requirements
- Each script is exactly 3 lines (shebang, comment, curl command)
- All scripts are executable
- Tested against a local web server on port 5000

## Files
- 0-body_size.sh    : prints the response body size in bytes
- 1-body.sh         : prints the body only for a 200 status response
- 2-delete.sh       : sends a DELETE request and prints the body
- 3-methods.sh      : lists all HTTP methods the server accepts
- 4-header.sh       : sends a GET with a custom header, prints the body
- 5-post_params.sh  : sends a POST with email and subject, prints the body
