import json
import time
def app(environ, start_response):
    d = {'time' : time.strftime("%H:%M:%S", time.localtime()), 'url' : environ['PATH_INFO']}
    data = bytes(json.dumps(d), 'utf-8') #getting bytes string
    status = '200 OK'
    response_headers = [
        ('Content-type', 'application/json'),
        ('Content-Length', str(len(data)))
    ]
#    print(environ['PATH_INFO'])
    start_response(status, response_headers)
    return [data]

