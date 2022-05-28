import datetime
from flask import request
from configparser import ConfigParser
import pytz
from dateutil.parser import parse

# import config file to global object
config = ConfigParser()
config_file = 'config.ini'
config.read(config_file)

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

def get_dates():
    #  retrieves date parameters if given
    #  if no date parameters have been given,
    #  will use current time - default days in the past (see config) for start_date
    if request.args.get('start_date'):
        start_date = request.args.get('start_date', datetime.datetime.now(datetime.timezone.utc))
    else: 
        default_days_in_the_past = config.get('past_events', 'default_days_in_the_past')
        current_time = (datetime.datetime.utcnow())
        start_date = (current_time - datetime.timedelta(int(default_days_in_the_past))).strftime('%Y-%m-%d')
    end_date = request.args.get('end_date', None)
    return start_date, end_date
 

def format_json_ld(events_json):
    # reformats all_meetings.json to JSON+LD 
    data_feed_elements = []
    for event in events_json:
        # if event is online:
        if event['venue'] is None or event['venue']['name'] == "Online event":
            location = {
                "@type": "VirtualLocation",
                "url": event.get('url')
            }
        else:
            location = {
                "@type": "Place",
                "name": event.get('venue').get('name'),
                "address": {
                "streetAddress": event.get('venue').get('address'), 
                "addressLocality": event.get('venue').get('city'),
                "addressRegion": event.get('venue').get('state'),
                "addressCountry": event.get('venue').get('country'),
                "postalCode": event.get('venue').get('zip')
                    },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": event.get('venue').get('lat'),
                    "longitude": event.get('venue').get('lon'),
                    }
                }
            
        element = {
            "@type": "DataFeedItem",
            "dateCreated": event.get("created_at"), 
            "dateModified": event.get('data_as_of'),
            "item": {
                "@type": "Event",
                "description": event.get('description'), 
                "name": event.get('event_name'), 
                "organizer": {
                    "@type": "Organization",
                    "name": event.get('group_name')
                        }, 
                "nid": event.get('nid'),
                "rsvp_count": event.get('rsvp_count'),
                "tags": event.get('tags'), 
                "startDate": event.get('time'), 
                "url": event.get('url'), 
                "identifier": event.get('uuid'), 
                "location": location
                }
            }
        data_feed_elements.append(element)
            
            
    ld_json = {
        "@context": [
                "http://schema.org/",
                {"nid": None, "rsvp_count": None, "tags": None, "uuid": None}
                ],
            "@type": "DataFeed",
            "dataFeedElement": data_feed_elements
            
            }
    return ld_json
