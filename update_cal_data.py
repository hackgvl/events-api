##!/home/ubuntu/miniconda2/envs/cal_service/bin/python
# encoding: utf-8
import app
import simplejson as json


# Gets lists of meetings, concatenates meeting lists from all sources, then saves json locally.
def refresh_all_meetings():
    group_lists = app.get_group_lists()
    meetup_events = app.get_meetup_events(group_lists['Meetup.com'])
    eventbrite_events = app.get_eventbrite_events(group_lists['Eventbrite.com'])
    eventbrite_venues = app.get_eventbrite_venues(eventbrite_events)
    events = (
        app.format_meetup_events(meetup_events, group_lists['Meetup.com'])
        + app.format_eventbrite_events(events_list=eventbrite_events,
                                       venues_list=eventbrite_venues,
                                       group_list=group_lists['Eventbrite.com'])
        )
    with open('all_meetings.json', 'w') as outfile:
        json.dump(events, outfile)
   
    return events


if __name__ == '__main__':
    refresh_all_meetings()
