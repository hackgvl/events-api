# This Project is Archived with a Replacement

**This project is no longer used or developed by HackGreenville Labs.**

However, an replacement [Events API](https://github.com/hackgvl/hackgreenville-com/blob/develop/EVENTS_API.md) has been integrated into our [HackGreenville.com application](https://github.com/hackgvl/hackgreenville-com).

## Kudos to Past Contributors
* Thanks to @Nunie123 for the initial development, and to @ramona-spence for sustaining the [previous Python implementation](https://github.com/hackgvl/events-api).
* Thanks to @bogdankharchenko and [HackGreenville Labs](https://hackgreenville.com/labs) for migrating the Python implementation to [PHP / Laravel](https://github.com/hackgvl/hackgreenville-com/blob/develop/EVENTS_API.md)

## Upstate / Greenville, SC Tech Organization Events API Service
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-8-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

This Python + Pipenv + Flask application previously provided an endpoint to return event data for all [organizations](https://data.openupstate.org/organizations) listed in the [organizations API](https://github.com/hackgvl/OpenData/blob/master/ORGANIZATIONS_API.md) if they host events on:

* Meetup.com - [example API call](https://github.com/hackgvl/events-api/issues/3#issuecomment-802219986)
* Eventbrite.com - [example API call](https://github.com/hackgvl/events-api/issues/4#issuecomment-802212633)

Meeting services currently not supported: [Facebook](https://github.com/hackgvl/events-api/issues/5), [Nvite](https://github.com/hackgvl/events-api/issues/6), [Open Collective](https://github.com/hackgvl/events-api/issues/2), and [custom websites](https://github.com/hackgvl/events-api/issues/7).

## Examples of Previous Consuming Applications

* [HackGreenville.com](https://hackgreenville.com/events)
* [OpenWorks' Dashboard](https://joinopenworks.com/dashboard/meetups.php)

The events listed on supported event services are pulled, combined, and re-published in [JSON format](https://www.json.org/json-en.html) or [JSON+LD](https://json-ld.org/) every hour at our [Events API](https://events.openupstate.org/api/gtc) endpoint.  Additional filtering options are described below.

# Contributing to and Running the Application

This project has been replaced, so join us at [Events API](https://github.com/hackgvl/hackgreenville-com/blob/develop/EVENTS_API.md) for get involved in the PHP / Laravel implementation.

There were three ways to run the appliation (locally, locally with Docker, and web server), but start by reading our [CONTRIBUTING.md](https://github.com/hackgvl/events-api/blob/master/deploy_notes_docker.md).

# Interacting with the API
By default, results were returned in JSON format.  If an `Accept: application/json+ld` header is sent to the API, then it will reply with [Schema.org Event markup](https://schema.org/Event) in JSON+LD format.

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

## Kudos to Past Contributors
* Thanks to @Nunie123 for the initial development, and to @ramona-spence for sustaining the [previous Python implementation](https://github.com/hackgvl/events-api).
* Thanks to @bogdankharchenko for migrating the Python implementation to PHP / Laravel

## Notes
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
      <td align="center" valign="top" width="14.28%"><a href="https://olivia.sculley.dev"><img src="https://avatars.githubusercontent.com/u/88074048?v=4?s=100" width="100px;" alt="Olivia Sculley"/><br /><sub><b>Olivia Sculley</b></sub></a><br /><a href="https://github.com/hackgvl/events-api/commits?author=oliviasculley" title="Code">💻</a> <a href="#infra-oliviasculley" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/hackgvl/events-api/commits?author=oliviasculley" title="Documentation">📖</a> <a href="#ideas-oliviasculley" title="Ideas, Planning, & Feedback">🤔</a> <a href="#platform-oliviasculley" title="Packaging/porting to new platform">📦</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://bigbluehat.com/"><img src="https://avatars.githubusercontent.com/u/43209?v=4?s=100" width="100px;" alt="BigBlueHat"/><br /><sub><b>BigBlueHat</b></sub></a><br /><a href="#ideas-BigBlueHat" title="Ideas, Planning, & Feedback">🤔</a> <a href="#question-BigBlueHat" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.linkedin.com/in/jeremywight/"><img src="https://avatars.githubusercontent.com/u/8245600?v=4?s=100" width="100px;" alt="Jeremy Wight"/><br /><sub><b>Jeremy Wight</b></sub></a><br /><a href="https://github.com/hackgvl/events-api/issues?q=author%3Ajeremywight" title="Bug reports">🐛</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ThorntonMatthewD"><img src="https://avatars.githubusercontent.com/u/44626690?v=4?s=100" width="100px;" alt="Matthew Thornton"/><br /><sub><b>Matthew Thornton</b></sub></a><br /><a href="https://github.com/hackgvl/events-api/commits?author=ThorntonMatthewD" title="Tests">⚠️</a> <a href="#infra-ThorntonMatthewD" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#research-ThorntonMatthewD" title="Research">🔬</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
