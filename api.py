import bottle
from bottle import get, route, request, run

people = [{'name':'Shashank', 'place':'Bengaluru'},
{'name':'Mohammed', 'place':'Chennai'},
{'name':'Rahul', 'place':'Delhi'}]

@get('/person')
def function():
    return {'person': people}

@get('/person/<name>')
def function(name):
    for person in people:
        if person['name'] == name:
            place = person['place']

            return {'place': place}




run(port=8081, reloader=True)