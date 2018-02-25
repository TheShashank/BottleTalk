import bottle
from bottle import route, run, static_file

@route('/files/<filename>')
def staticfiles(filename):
    return static_file(filename, root='static')

run(port=8080, reloader=True)