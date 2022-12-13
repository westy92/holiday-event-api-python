import pytest
import holidays
from holidays.types import Occurrence


with open('test/responses/getEventInfo.json', 'r') as f:
    default = f.read()
with open('test/responses/getEventInfo-parameters.json', 'r') as f:
    parameters = f.read()


def test_get_event_info_with_default_parameters(requests_mock):
    client = holidays.client('abc123')
    requests_mock.get(
        'https://api.apilayer.com/checkiday/event?id=f90b893ea04939d7456f30c54f68d7b4',
        text=default,
    )
    result = client.getEventInfo(id='f90b893ea04939d7456f30c54f68d7b4')
    assert requests_mock.called
    assert result.event.id == 'f90b893ea04939d7456f30c54f68d7b4'
    assert len(result.event.hashtags) == 2


def test_get_event_info_with_set_parameters(requests_mock):
    client = holidays.client('abc123')
    requests_mock.get(
        'https://api.apilayer.com/checkiday/event?id=f90b893ea04939d7456f30c54f68d7b4&start=2002&end=2003',
        text=parameters,
    )
    result = client.getEventInfo(id='f90b893ea04939d7456f30c54f68d7b4', start=2002, end=2003)
    assert requests_mock.called
    assert len(result.event.occurrences) == 2
    assert result.event.occurrences[0] == Occurrence(
        date='08/08/2002',
        length=1,
    )


def test_get_event_info_invalid_event(requests_mock):
    client = holidays.client('abc123')
    requests_mock.get(
        'https://api.apilayer.com/checkiday/event?id=hi',
        status_code=404,
        json={'error': 'Event not found.'},
    )
    with pytest.raises(RuntimeError) as e:
        client.getEventInfo(id='hi')
    assert 'Event not found.' == str(e.value)
    assert requests_mock.called


def test_get_event_info_missing_id():
    client = holidays.client('abc123')
    with pytest.raises(ValueError) as e:
        client.getEventInfo(id=None)
    assert 'Event id is required.' == str(e.value)
