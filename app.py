from urllib import response
from flask import Flask, Response
from flask_cors import CORS
import simplejson as json
from configparser import ConfigParser
import app_functions as func
from flask_restful import Api, Resource

# import config file to global object
config = ConfigParser()
config_file = 'config.ini'
config.read(config_file)


import logging
from logging.config import fileConfig

# instantiate flask app
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = config.get('flask', 'secret_key')

fileConfig('logging_config.ini')
logger = logging.getLogger()

api = Api(app)

# representation decorator tells the app to route request to this method
# when the request Content-Type is application/json
# See https://flask-restful.readthedocs.io/en/latest/extending.html#content-negotiation
# for description of this decorator. 
@api.representation('application/json')
def output_json(data, code, headers={"Content-Type": "application/json"}):
    events_data = json.dumps(data)
    resp = Response(events_data, status=code, headers=headers)
    return resp
    
@api.representation('application/json+ld')
def output_json_ld(data, code, headers={"Content-Type": "application/json+ld"}):
    events_data = func.format_ld_json(data)
    events_data = json.dumps(events_data)
    resp = Response(events_data, status=code, headers=headers)
    return resp

class Event(Resource):
    def get(self):
        with open('all_meetings.json') as json_data:
            events= json.load(json_data)
        return events

# binds the resource Event, to the endpoint `/api/gtc`
api.add_resource(Event, '/api/gtc')

if __name__ == '__main__':
    app.run()
