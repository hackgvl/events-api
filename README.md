# Upstate / Greenville, SC Tech Organization Events API Service
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

This Python + Pipenv + Flask application provides an endpoint to return event data for all [organizations](https://data.openupstate.org/organizations) listed in the [organizations API](https://github.com/hackgvl/OpenData/blob/master/ORGANIZATIONS_API.md) if they host events on:

* Meetup.com - [example API call](https://github.com/hackgvl/events-api/issues/3#issuecomment-802219986)
* Eventbrite.com - [example API call](https://github.com/hackgvl/events-api/issues/4#issuecomment-802212633)

Meeting services currently not supported: [Facebook](https://github.com/hackgvl/events-api/issues/5), [Nvite](https://github.com/hackgvl/events-api/issues/6), [Open Collective](https://github.com/hackgvl/events-api/issues/2), and [custom websites](https://github.com/hackgvl/events-api/issues/7).

If your organization is not included, then connect with us by commenting on [one of the issues](https://github.com/hackgvl/events-api/issues).

## Examples Applications

* [HackGreenville.com](https://hackgreenville.com/events)
* [OpenWorks' Dashboard](https://joinopenworks.com/dashboard/meetups.php)

The events listed on supported evebt services are pulled, combined, and re-published in [JSON format](https://www.json.org/json-en.html) or [JSON+LD](https://json-ld.org/) every hour at our [Events API](https://events.openupstate.org/api/gtc) endpoint.  Additional filtering options are described below.

# Contributing to and Running the Application

There are three ways to run the appliation (locally, locally with Docker, and web server), but start by reading our [CONTRIBUTING.md](https://github.com/hackgvl/events-api/blob/master/deploy_notes_docker.md).

# Interacting with the API
By default, results are returned in JSON format.  If an `Accept: application/json+ld` header is sent to the API, then it will reply with [Schema.org Event markup](https://schema.org/Event) in JSON+LD format.

* [Get all upcoming events](https://events.openupstate.org/api/gtc) by calling _/api/gtc_
* [Get events within a date range](https://events.openupstate.org/api/gtc?start_date=2018-01-01&end_date=2018-02-01) by calling _/api/gtc?start__date=2018-01-01&end__date=2018-02-01_
    * the API defaults to providing only upcoming meetings, unless a `start_date` and `end_date` are specified
    * "past events" are limited by the `[past_events] max_days_in_the_past` set in the config.ini file
    * "US/Eastern" is assumed as the timezone when a date filter is provided
* [Get events with a specific organizations tag](https://events.openupstate.org/api/gtc?tags=1) by calling _/api/gtc?tags=1_ - "tags" are applied to an organization in the [organizations API](https://github.com/hackgvl/OpenData/issues/17).  Currently, the organizations API only provides integer tag IDs, such as with this tag #1, representing OpenWorks hosted events, https://events.openupstate.org/api/gtc?tags=1


The format of the JSON that returns is:

    [{
    "event_name": "Code For Greenville Work Night",
    "group_name": "Code for Greenville",
    "group_url": 'https://hackgvl.org',
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

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Nunie123"><img src="https://avatars.githubusercontent.com/u/15092236?v=4?s=100" width="100px;" alt="Ed Nunes"/><br /><sub><b>Ed Nunes</b></sub></a><br /><a href="#ideas-Nunie123" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/hackgvl/events-api/commits?author=Nunie123" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/allella"><img src="https://avatars.githubusercontent.com/u/1777776?v=4?s=100" width="100px;" alt="Jim Ciallella"/><br /><sub><b>Jim Ciallella</b></sub></a><br /><a href="https://github.com/hackgvl/events-api/commits?author=allella" title="Code">💻</a> <a href="#maintenance-allella" title="Maintenance">🚧</a> <a href="#infra-allella" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#projectManagement-allella" title="Project Management">📆</a> <a href="https://github.com/hackgvl/events-api/pulls?q=is%3Apr+reviewed-by%3Aallella" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/hackgvl/events-api/issues?q=author%3Aallella" title="Bug reports">🐛</a> <a href="https://github.com/hackgvl/events-api/commits?author=allella" title="Documentation">📖</a> <a href="#question-allella" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.linkedin.com/in/ramona-spence"><img src="https://avatars.githubusercontent.com/u/52936858?v=4?s=100" width="100px;" alt="Ramona"/><br /><sub><b>Ramona</b></sub></a><br /><a href="https://github.com/hackgvl/events-api/commits?author=ramonaspence" title="Code">💻</a> <a href="#ideas-ramonaspence" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/hackgvl/events-api/commits?author=ramonaspence" title="Documentation">📖</a> <a href="https://github.com/hackgvl/events-api/issues?q=author%3Aramonaspence" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/bcsnipes"><img src="https://avatars.githubusercontent.com/u/43290072?v=4?s=100" width="100px;" alt="Brett Snipes"/><br /><sub><b>Brett Snipes</b></sub></a><br /><a href="https://github.com/hackgvl/events-api/commits?author=bcsnipes" title="Code">💻</a> <a href="https://github.com/hackgvl/events-api/issues?q=author%3Abcsnipes" title="Bug reports">🐛</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!