from bottle import Bottle,redirect, response
from bottle.ext.mongo import MongoPlugin
from bson.json_util import dumps

app = Bottle()

plugin = MongoPlugin(uri="mongodb://127.0.0.1/27017", db="mydb", json_mongo=True)

@app.route('/get', method='GET')
def index(mongodb):
    return dumps(mongodb['collection'].find())

@app.route('/post/<name>/<place>') #Optional parameters<param:int>
def create(mongodb, name, place):
    mongodb['collection'].insert({'name': name, 'b': 2})
    redirect("/get")

@app.post('/post1')
def post1():

app.install(plugin) #will be applied to all routes of this application

app.run(reloader=True, port=8080)