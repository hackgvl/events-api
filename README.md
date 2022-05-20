# Upstate / Greenville, SC Tech Organization Events API Service

This Python + Pipenv + Flask application provides an endpoint to return event data for all [organizations](https://data.openupstate.org/organizations) listed in the [organizations API](https://github.com/codeforgreenville/OpenData/blob/master/ORGANIZATIONS_API.md) if they host events on:

* Meetup.com - [example API call](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/3#issuecomment-802219986)
* Eventbrite.com - [example API call](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/4#issuecomment-802212633)

Meeting services currently not supported: [Facebook](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/5), [Nvite](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/6), [Open Collective](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/2), and [custom websites](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/7).

If your organization is not included, then connect with us by commenting on [one of the issues](https://github.com/codeforgreenville/upstate_tech_cal_service/issues).

## Examples Applications

* [HackGreenville.com](https://hackgreenville.com/events)
* [OpenWorks' Dashboard](https://joinopenworks.com/dashboard/meetups.php)

The events listed on supported evebt services are pulled, combined, and re-published in [JSON format](https://www.json.org/json-en.html) or [JSON+LD](https://json-ld.org/) every hour at our [Events API](https://events.openupstate.org/api/gtc) endpoint.  Additional filtering options are described below.

# Contributing to and Running the Application

There are three ways to run the appliation (locally, locally with Docker, and web server), but start by reading our [CONTRIBUTING.md](https://github.com/codeforgreenville/upstate_tech_cal_service/blob/master/deploy_notes_docker.md).

# Interacting with the API
By default, results are returned in JSON format.  If an `Accept: application/json+ld` header is sent to the API, then it will reply with [Schema.org Event markup](https://schema.org/Event) in JSON+LD format.

* [Get all upcoming events](https://events.openupstate.org/api/gtc) by calling _/api/gtc_
* [Get events within a date range](https://events.openupstate.org/api/gtc?start_date=2018-01-01&end_date=2018-02-01) by calling _/api/gtc?start__date=2018-01-01&end__date=2018-02-01_
    * the API defaults to providing only upcoming meetings, unless a `start_date` and `end_date` are specified
    * "past events" are limited by the `[past_events] max_days_in_the_past` set in the config.ini file
    * "US/Eastern" is assumed as the timezone when a date filter is provided
* [Get events with a specific organizations tag](https://events.openupstate.org/api/gtc?tags=1) by calling _/api/gtc?tags=1_ - "tags" are applied to an organization in the [organizations API](https://github.com/codeforgreenville/OpenData/issues/17).  Currently, the organizations API only provides integer tag IDs, such as with this tag #1, representing OpenWorks hosted events, https://events.openupstate.org/api/gtc?tags=1


The format of the JSON that returns is:

    [{
    "created_at": "2019-03-05T13:44:52Z", 
    "data_as_of": "2019-10-02T03:35:21Z", 
    "description": "Bring your laptop and join us for our monthly Hack Night - drop-ins welcome!", 
    "event_name": "WWCode Hack Night", 
    "group_name": "Women Who Code Greenville", 
    "nid": "40", 
    "rsvp_count": 10, 
    "service": "meetup", 
    "service_id": "cqthwryccfbdc", 
    "status": "upcoming", 
    "tags": "1", 
    "time": "2019-10-03T22:00:00Z", 
    "url": null, 
    "uuid": "788992ce-51f8-44e2-b300-d495303e0025", 
    "venue": null
    "event_name": "Code For Greenville Work Night",
    "group_name": "Code for Greenville",
    "venue": null,
    "url": "https://www.meetup.com/Code-for-Greenville/events/qwpbksyfchbdb/",
    "time": "2023-05-02T22:00:00Z",
    "tags": "1",
    "rsvp_count": 0,
    "created_at": "2021-05-27T02:26:52Z",
    "description": "Come and Design, Write Copy, Hack on the Code for Greenville Projects. If you are attending for the first time, we'll have an organizer to explain the active projects. ",
    "uuid": "9a1c536a-c0a8-4886-b327-435ec1382dd7",
    "nid": "7",
    "data_as_of": "2022-05-20T02:40:11Z",
    "status": "upcoming",
    "service_id": "qwpbksyfchbdb",
    "service": "meetup"
    }]

Note:
* Kudos to @Nunie123 for the initial development
* All timestamps are in UTC.  
* The event description fields may include HTML markup.  This application does not sanitize those fields and it's unclear if the upstream source should be trusted, so sanitize any output to avoid malicious XSS.
