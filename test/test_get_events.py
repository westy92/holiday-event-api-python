import holidays


with open('test/responses/getEvents-default.json', 'r') as f:
    default = f.read()
with open('test/responses/getEvents-parameters.json', 'r') as f:
    parameters = f.read()


def test_get_events_with_default_parameters(requests_mock):
    client = holidays.client('abc123')
    requests_mock.get(
        'https://api.apilayer.com/checkiday/events',
        text=default,
    )
    result = client.getEvents()
    assert requests_mock.called
    assert result['adult'] is False
    assert result['timezone'] == 'America/Chicago'
    assert len(result['events']) == 2
    assert len(result['multiday_starting']) == 1
    assert len(result['multiday_ongoing']) == 2
    assert result['events'][0] == {
        'id': 'b80630ae75c35f34c0526173dd999cfc',
        'name': 'Cinco de Mayo',
        'url': 'https://www.checkiday.com/b80630ae75c35f34c0526173dd999cfc/cinco-de-mayo',
    }


def test_get_events_with_set_parameters(requests_mock):
    client = holidays.client('abc123')
    requests_mock.get(
        'https://api.apilayer.com/checkiday/events'
        + '?adult=true&timezone=America/New_York&date=7/16/1992',
        text=parameters,
    )
    result = client.getEvents(
        date='7/16/1992', adult=True, timezone='America/New_York')
    assert requests_mock.called
    assert result['adult'] is True
    assert result['timezone'] == 'America/New_York'
    assert len(result['events']) == 2
    assert len(result['multiday_starting']) == 0
    assert len(result['multiday_ongoing']) == 1
    assert result['events'][0] == {
        'id': '6ebb6fd5e483de2fde33969a6c398472',
        'name': 'Get to Know Your Customers Day',
        'url': 'https://www.checkiday.com/6ebb6fd5e483de2fde33969a6c398472/get-to-know-your-customers-day',
    }
