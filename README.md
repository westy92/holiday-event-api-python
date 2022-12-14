# The Official Holiday and Event API for Python

[![PyPI](https://img.shields.io/pypi/v/holiday-event-api)](https://pypi.org/project/holiday-event-api)
[![Supported Versions](https://img.shields.io/pypi/westy92/holiday-event-api.svg)](https://pypi.org/project/holiday-event-api)
[![Build Status](https://github.com/westy92/holiday-event-api-python/actions/workflows/github-actions.yml/badge.svg)](https://github.com/westy92/holiday-event-api-python/actions)
[![Code Coverage](https://codecov.io/gh/westy92/holiday-event-api-python/branch/main/graph/badge.svg)](https://codecov.io/gh/westy92/holiday-event-api-python)
[![Known Vulnerabilities](https://snyk.io/test/github/westy92/holiday-event-api-python/badge.svg)](https://snyk.io/test/github/westy92/holiday-event-api-python)
[![Funding Status](https://img.shields.io/github/sponsors/westy92)](https://github.com/sponsors/westy92)

Industry-leading Holiday and Event API for Python. Over 5,000 holidays and thousands of descriptions. Trusted by the World’s leading companies. Built by developers for developers since 2011.

## Supported Python Versions
Latest version of the the Holiday and Event API supports all actively-maintained Python [releases](https://devguide.python.org/versions/) and might work with older versions. It also supports PyPy versions `3.7`, `3.8`, and `3.9`.

## Authentication

Access to the Holiday and Event API requires an API Key. You can get for one for FREE [here](https://apilayer.com/marketplace/checkiday-api#pricing), no credit card required! Note that free plans are limited. To access more data and have more requests, a paid plan is required.

## Installation

The Holiday and Event API is available on PyPI:
```console
$ python -m pip install holiday-event-api
```

## Example

```python
import holidays


try:
    # Get a FREE API key from https://apilayer.com/marketplace/checkiday-api#pricing
    client = holidays.client('<Your API Key Here>')

    # Get Events for a given Date
    events = client.getEvents(
        # These parameters are the defaults but can be specified:
        # date='today',
        # timezone='America/Chicago',
        # adult=False,
    )

    event = events.events[0]
    print(f"Today is {event.name}! Find more information at: {event.url}.")
    print(f"Rate limits remaining: {events.rateLimit.remainingMonth}/{events.rateLimit.limitMonth} (month).")

    # Get Event Information
    eventInfo = client.getEventInfo(
        id=event.id,
        # These parameters can be specified to calculate the range of eventInfo.Event.Occurrences
        # start=2020,
        # end=2030,
    )

    print(f"The Event's hashtags are {eventInfo.event.hashtags}.")

    # Search for Events
    query = "pizza day"
    search = client.search(
        query=query,
        # These parameters are the defaults but can be specified:
        # adult=False,
    )

    print(f"Found {len(search.events)} events, including {search.events[0].name}, that match the query '{query}'.")
except Exception as e:
    print(f"There was an error: {e}")
```