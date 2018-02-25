from bottle import run, request, get, post, Bottle, template

app = Bottle()

people = [{'name':'Shashank', 'place':'Bengaluru'},
{'name':'Mohammed', 'place':'Chennai'},
{'name':'Rahul', 'place':'Delhi'}]

@app.route('/person', method='GET')
def functionToRun():
    #return the list of people and places
    return {'people': people}

@app.get('/person/<name>') #passes the covered part of the URL as a keyword argument to the request callback
def specificPerson(name):
    place = 'a'
    for person in people:
        if person['name'] == name:
            place = person['place']

            return {'place': place}

@app.route('/test')
def needAConvention():
    id = request.query.id #query variables
    return template("The id is {{id}}")

@app.route('/hello')
def hello_again():
    if request.get_cookie("visited"):
        return "Welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you"

@app.route('/addperson', method='POST, OPTIONS')
def addPerson():
    #How do you add an element to a dictionary?
    people.append({'name': 2, 'place': 42})


'''
@get('/person')
def returnAll():
    return {'people':people}
    
@get('/person/<name>')
def returnOne(name):
 gender = [person for people in people if person['name'] == name]
 return {'name': name, 'gender': gender}
'''
run(reloader=True)