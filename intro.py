import bottle
from bottle import run, route

@route('/hello')
@route('/hello/<name>')
def function(name):
    return 'Hello ' + name

run(port=8080, reloader=True)