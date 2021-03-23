## Upstate / Greenville, SC Tech Organization Events / Calendar API Service

This application provides an endpoint to return event data for all [organizations](https://data.openupstate.org/organizations) listed in the [organizations API](https://github.com/codeforgreenville/OpenData/blob/master/ORGANIZATIONS_API.md) if they host events on:
* Meetup.com - [example API call](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/3#issuecomment-802219986)
* Eventbrite.com - [example API call](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/4#issuecomment-802212633)

Meeting services currently not supported: [Facebook](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/5), [Nvite](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/6), [Open Collective](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/2), and [custom websites](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/7).

To be added or provided updates to this list, make a comment on [one of the issues](https://github.com/codeforgreenville/upstate_tech_cal_service/issues).

### Examples
* [HackGreenville.com](https://hackgreenville.com/events)
* [OpenWorks' Dashboard](https://joinopenworks.com/dashboard/meetups.php)

The events from supported serivces are pulled, combined, and re-published in [JSON format](https://www.json.org/json-en.html) once an hour at https://events.openupstate.org/api/gtc  See below for additional filtering options.

### Documentation

#### Setup
If you're new here, then initial setup of test or production environment with Python + Miniconda + Flask app can be found in the [deploy_notes_initial.md](https://github.com/codeforgreenville/upstate_tech_cal_service/blob/master/deploy_notes_initial.md)

Other [general application notes are included in the issue from before the app was migrated](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/14) off Heroku onto a dedicated server.

#### Interacting with a Running Application

The exposed JSON includes past and future meetings as they are provided by the event services. The API defaults to providing only upcoming meetings, unless a `start_date` and `end_date` are specified, like https://events.openupstate.org/api/gtc?start_date=2018-01-01&end_date=2018-02-01.

The application currently assumes "US/Eastern" as the timezone when a date filter is provided.

You may ALSO filter by any "tags" applied to an organization in the [organizations API](https://github.com/codeforgreenville/OpenData/issues/17).  Currently, the organizations API only provides integer tag IDs, such as with this tag #1, representing OpenWorks hosted events, https://events.openupstate.org/api/gtc?tags=1

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
    }]

Note:
* Kudos to @Nunie123 for the initial development
* All timestamps are in UTC.  
* The event description fields may include HTML markup.  This application does not sanitize those fields and it's unclear if the upstream source should be trusted, so sanitize any output to avoid malicious XSS.
