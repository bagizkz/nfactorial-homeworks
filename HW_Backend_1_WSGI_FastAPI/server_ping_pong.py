def application(environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')
    if path == 'ping':
        response_body = b"pong"
        status = '200 OK'
    else:
        response_body = b"Not Found"
        status = '404 Not Found'

    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [response_body]