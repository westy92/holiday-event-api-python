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
