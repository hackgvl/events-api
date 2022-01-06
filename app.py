from flask import Flask, jsonify, request
from flask_cors import CORS
import simplejson as json
from configparser import ConfigParser
# import requests
import datetime
import pytz
from dateutil.parser import parse

# import config file to global object
config = ConfigParser()
config_file = 'config.ini'
config.read(config_file)

import logging
from logging.config import fileConfig

# instantiate flask app
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
CORS(app)
app.config['SECRET_KEY'] = config.get('flask', 'secret_key')

fileConfig('logging_config.ini')
logger = logging.getLogger()

# Method used for parsing dates throughout functions
def parse_date(d):
    if isinstance(d, datetime.datetime):
        parsed_date = d
    elif isinstance(d, str):
        try:
            eastern = pytz.timezone('US/Eastern')
            date_no_tz = parse(d)
            parsed_date = eastern.localize(date_no_tz, is_dst=None)
        except ValueError:
            return 'Start date {} is in unknown format. '.format(d)
    else:
        return 'Start date {} is in unknown format. '.format(d)
    return parsed_date

# Takes list of events and returns list of events occuring in specified date range
def filter_events_by_date(events, start_date_str=datetime.datetime.now(datetime.timezone.utc), end_date_str=None):
    
    # days_in_the_past = config.get('past_events', 'days_in_the_past')
    # current_time = (datetime.datetime.utcnow())
    # if start_date_str:
    #     start_date = (current_time - datetime.timedelta(int(days_in_the_past))).strftime('%Y-%m-%dT%H:%M:%SZ')
    # else:
    #     start_date = None
    start_date = parse_date(start_date_str) if start_date_str else None
    end_date = parse_date(end_date_str) if end_date_str else None

    if isinstance(start_date, str) or isinstance(end_date, str):
        return '{}{}'.format(start_date, end_date).replace('None', '')

    if start_date and end_date:
        return [event for event in events if start_date <= parse(event['time']) <= end_date]
    elif start_date:
        return [event for event in events if parse(event['time']) >= start_date]
    elif end_date:
        return [event for event in events if parse(event['time']) <= end_date]
    else:
        
        return events

# Takes list of events and string of tags to return list of events with specified tags
def filter_events_by_tag(events, tags):
    if tags:
        tags_list = tags.replace(' ', '').split(',')
        filtered_events = []
        for tag in tags_list:
            filtered_events += [event for event in events if tag in event['tags']]
        return filtered_events
    else:
        return events

def normalize_eventbrite_status_codes(status):
    # takes current status from eventbrite, and matches it to meetup's vernacular
    status_dict = {
        'canceled': 'cancelled',
        'live': 'upcoming',
        'ended': 'past'
    }
    return status_dict.get(status)

@app.route('/api/gtc', methods=['GET', 'POST'])
def get_dates():
    if request.args.get('start_date'):
        start_date = request.args.get('start_date', datetime.datetime.now(datetime.timezone.utc))
    else: 
        default_days_in_the_past = config.get('past_events', 'default_days_in_the_past')
        current_time = (datetime.datetime.utcnow())
        start_date = (current_time - datetime.timedelta(int(default_days_in_the_past))).strftime('%Y-%m-%d')

    end_date = request.args.get('end_date', None)
    tags = request.args.get('tags', None)
    with open('all_meetings.json') as json_data:
        events_json = json.load(json_data)
        events_date_filter = filter_events_by_date(start_date_str=start_date, end_date_str=end_date, events=events_json)
        events = filter_events_by_tag(events_date_filter, tags)

        # Sort events by time
        events_json.sort(key=lambda s: s['time'])
        return jsonify(events)


if __name__ == '__main__':
    app.run()
