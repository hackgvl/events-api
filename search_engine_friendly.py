

{
"@context": [
      "http://schema.org/",
  {"nid": null, "rsvp_count": null, "tags": null, "uuid": null}
],
"@type": "DataFeed",
"dataFeedElement": [
  {
    "@type": "DataFeedItem",
    "dateCreated": datetime.datetime.utcfromtimestamp(int(event.get('created'))/1000)
                                  .strftime('%Y-%m-%dT%H:%M:%SZ'), 
    "dateModified": "2019-01-27T05:43:14Z",
    "item": {
      "@type": "Event",
      "description": event.get('description'), 
      "name": event.get('name'), 
      "organizer": {
        "@type": "Organization",
        "name": event.get(group).get(name)
      }, 
      "nid": "7",
      "rsvp_count": 0, 
      "tags": "1", 
      "startDate": "2019-03-05T23:00:00Z", 
      "url": "https://www.meetup.com/Code-for-Greenville/events/mcrjcqyzfbhb/", 
      "identifier": "urn:uuid:47500439-5c63-45ba-9600-be41109bc291", 
      "location": {
        "@type": "Place",
        "name": "OpenWorks",
        "address": {
          "streetAddress": "101 N. Main St 3rd Floor", 
          "addressLocality": "Greenville",
          "addressRegion": "SC",
          "addressCountry": "USA",
          "postalCode": null
        },
        "geo": {
          "@type": "GeoCoordinates",
          "latitude": 34.851925, 
          "longitude": -82.399948
        }
      }
    }
  }
]}


#create dataFeedElement with date created, date modified, item{}, nid, rsvp_count, tags, startDate, url,
    #identifier, location{}, geo{}

data = {
    "@context": [
      "http://schema.org/",
  {"nid": None, "rsvp_count": None, "tags": null, "uuid": null}
], 
}

item = {}
location = {}
address = {}
geo = {}


def format_meetup_events(events_raw, group_list):
    
    events = []
    for event in events_raw:
        venue_dict = event.get('venue')
        group_item = [i for i in group_list if i.get('field_events_api_key') == str(event['group']['urlname'])][0]
        tags = group_item.get('field_org_tags')
        uuid = group_item.get('uuid')
        nid = group_item.get('nid')

        if venue_dict:

            location = {
                "@type": "Place",
                "name": venue_dict.get('name'),
                "address": {
                    "streetAddress": venue_dict.get('address_1'),
                    "addressLocality": venue_dict.get('city'),
                    "addressRegion": venue_dict.get('state'),
                    "addressCountry": venue_dict.get('country'),
                    "postalCode": venue_dict.get('zip')
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": venue_dict.get('lat'),
                    "longitude": venue_dict.get('lon')
                }
            }
        else:
            location = None
        if event.get('description'):
            description = event.get('description').replace('<p>', '').replace('</p>', '')
        else:
            description = None

        try:
            event_data = {
                "@type":"dataFeedItem",
                "date_created": datetime.datetime.utcfromtimestamp(int(event.get('created'))/1000).strftime('%Y-%m-%dT%H:%M:%SZ'),
                "date_modified": datetime.datetime.utcfromtimestamp(int(event.get('updated'))/1000).strftime('%Y-%m-%dT%H:%M:%SZ'),
                "item": {
                    "@type": "Event",
                    #update with regex to catch all html tags
                    "description": event.get('description').replace('<p>', '').replace('</p>', ''),
                    "name": event.get('name'), 
                    "organizer": {
                        "@type": "Organization",
                        "name": event.get('group').get('name')
                    },
                "nid": event.get('nid'),
                "rsvp_count": event.get('yes_rsvp_count'), 
                "tags": "1", 
                "startDate": datetime.datetime.utcfromtimestamp(int(event.get('time'))/1000).strftime('%Y-%m-%dT%H:%M:%SZ'), 
                "url": event.get('link'), 
                "identifier": "urn:uuid:{}".format(event.get('uuid')),  
                },
                "location": location,
            }
        except TypeError:
            pass

        events.append(event_data)
    return events


def format_eventbrite_events(events_list, venues_list, group_list):
    
    venues = {}
    events = []
    for venue in venues_list:
        venue_id = venue.get('id')
        venue_address = venue.get('address')
        venue_dict = {} 
        if venue_address:
            location = {
                "@type": "Place",
                "name": venue_address.get('name'),
                "address": {
                    "streetAddress": venue_address.get('address_1'),
                    "addressLocality": venue_address.get('city'),
                    "addressRegion": venue_address.get('state'),
                    "addressCountry": venue_address.get('country'),
                    "postalCode": venue_address.get('zip')
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": venue_address.get('lat'),
                    "longitude": venue_address.get('lon')
                }
            }
        venues[venue_id] = venue_dict

    for event in events_list:
        #If eventbrite event is not online and venue_id is not None: is venue_id a str or int?
        if type(event.get('venue_id')) == str or event.get('venue_id') is None:  # If venue id error
            group_item = [i for i in group_list if i['field_events_api_key'] == event.get('organizer_id')][0]
            group_name = group_item.get('title')
            if type(event.get('venue_id')) == str:
                event_data = {
                "@type":"dataFeedItem",
                "date_created": datetime.datetime.utcfromtimestamp(int(event.get('created'))/1000).strftime('%Y-%m-%dT%H:%M:%SZ'),
                "date_modified": datetime.datetime.utcfromtimestamp(int(event.get('changed'))/1000).strftime('%Y-%m-%dT%H:%M:%SZ'),
                "item": {
                    "@type": "Event",
                    #update with regex to catch all html tags
                    "description": event.get('description').get('text'),
                    "name": event.get('name').get('text'), 
                    "organizer": {
                        "@type": "Organization",
                        "name": group_name
                    },
                "nid": event.get('nid'),
                "rsvp_count": event.get('yes_rsvp_count'), 
                "tags": "1", 
                "startDate": datetime.datetime.utcfromtimestamp(int(event.get('start').get('utc'))/1000).strftime('%Y-%m-%dT%H:%M:%SZ'), 
                "url": event.get('url'), 
                "identifier": "urn:uuid:{}".format(event.get('uuid')),  
                },
                "location": location,
            }
                # event_dict = {
                #     'event_name': event.get('name').get('text'),
                #     'group_name': group_name,
                #     'venue': venues[event.get('venue_id')],
                #     'url': event.get('url'),
                #     'time': event.get('start').get("utc"),
                #     'tags': tags,
                #     'rsvp_count': None,
                #     'created_at': event.get('created'),
                #     'description': event.get('description').get('text'),
                #     'uuid': uuid,
                #     'nid': nid,
                #     'data_as_of': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
                #     'status': normalize_eventbrite_status_codes(event.get('status'))
                # }
            elif event.get('venue_id') == None: # if event venue is None, it is online/virtual
                event_dict = {
                    'event_name': event.get('name').get('text'),
                    'group_name': group_name,
                    'venue': event.get('venue_id'),
                    'url': event.get('url'),
                    'time': event.get('start').get("utc"),
                    'tags': tags,
                    'rsvp_count': None,
                    'created_at': event.get('created'),
                    'description': event.get('description').get('text'),
                    'uuid': uuid,
                    'nid': nid,
                    'data_as_of': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
                    'status': normalize_eventbrite_status_codes(event.get('status'))
                }
            events.append(event_dict)
    return events