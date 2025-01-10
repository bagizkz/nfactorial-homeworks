def application(environ, start_response):
    if environ.get('PATH_INFO', '').lstrip('/') == 'info':
        method = environ.get('REQUEST_METHOD')
        url = environ.get('PATH_INFO')
        protocol = environ.get('SERVER_PROTOCOL')

        response_body = f"Method: {method}\nURL: {url}\nProtocol: {protocol}".encode()
        status = '200 OK'
    else:
        response_body = b"Not Found"
        status = '404 Not Found'

    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [response_body]