## Greenville Tech Meetup Events / Calendar API Service

This application provides an endpoint to return event data for all [meetup groups](https://data.openupstate.org/organizations) listed in the [meetups API](https://github.com/codeforgreenville/OpenData/issues/17) if they host meetings on:
* Meetup.com - [example API call](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/3#issuecomment-802219986)
* Eventbrite.com - [example API call](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/4#issuecomment-802212633)

Meeting services currently not supported: [Facebook](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/5), [Nvite](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/6), [Open Collective](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/2), and [custom websites](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/7).

To be added or provided updates to this list, make a comment on [one of the issues](https://github.com/codeforgreenville/upstate_tech_cal_service/issues).

The exposed JSON includes past and future meetings, but defaults to providing only future meetings unless a `start_date` is specified. The data comes from the associated event hosting website APIs and is updated every five minutes.

You can access this data by going here: https://events.openupstate.org/api/gtc

### Examples
* [HackGreenville.com](https://hackgreenville.com/events)
* [OpenWorks' Dashboard](https://joinopenworks.com/dashboard/meetups.php)


### Documentation

#### Setup
If you're new here, then initial setup of test or production environment with Python + Miniconda + Flask app can be found in the [deploy_notes_initial.md](https://github.com/codeforgreenville/upstate_tech_cal_service/blob/master/deploy_notes_initial.md)

Other [general application notes are included in the issue from before the app was migrated](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/14) off Heroku onto a dedicated server.

#### Interacting with a Running Application

You may filter by any tags applied to the organization on the openupstate.org api.  Currently the openupstate.org api only provides Tag IDs (i.e. an integer) instead of descriptive tags. (e.g. https://events.openupstate.org/api/gtc?tags=1)

You may also filter the return result by providing a `start_date` and `end_date` like so: https://events.openupstate.org/api/gtc?start_date=2018-01-01&end_date=2018-02-01 (the application currently assumes "US/Eastern" as the timezone when a date filter is provided)

The format of the JSON that returns is:

    [{
    "created_at": "2019-03-05T13:44:52Z", 
    "data_as_of": "2019-10-02T03:35:21Z", 
    "description": "Bring your laptop and join us for our monthly Hack Night - drop-ins welcome! You are invited to work on any coding project you have, learn to code while enjoying a hacking atmosphere and network with other women developers. You will have the opportunity to announce your project or ask for help and mingle with other women in tech. If you're just starting off with coding, come, and we'll help you choose tutorials and learn further. Some of our members are working on freeCodeCamp (<a href=\"https://www.freecodecamp.com/\" class=\"linkified\">https://www.freecodecamp.com/</a>). Just checking out what everyone else is doing is OK, too! If you have skills to share, please come to help mentor and answer questions. THANKS to our host OpenWorks (<a href=\"https://joinopenworks.com/\" class=\"linkified\">https://joinopenworks.com/</a>)! Schedule: 6:00pm Arrive/Network/Food<br/>6:30pm Welcome &amp; Announcements<br/>6:45pm Freestyle Hack Night ", 
    "event_name": "WWCode Hack Night", 
    "group_name": "Women Who Code Greenville", 
    "nid": "40", 
    "rsvp_count": 10, 
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
* Some of the description fields include html markup from the host sites.  This application does not verify that there is nothing malicious in the included markup.
