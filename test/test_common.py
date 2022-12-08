import requests
import holidays
import pytest

def test_sends_api_key(requests_mock):
    client = holidays.client('abc123')
    requests_mock.get(
        'https://api.apilayer.com/checkiday/events',
        request_headers={'apikey': 'abc123'},
        json={},
    )
    client.getEvents()
    assert requests_mock.called

def test_sends_user_agent(requests_mock):
    client = holidays.client('abc123')
    requests_mock.get(
        'https://api.apilayer.com/checkiday/events',
        request_headers={'user-agent': 'HolidayApiPython/0.0.1'},
        json={},
    )
    client.getEvents()
    assert requests_mock.called

def test_passes_along_error(requests_mock):
    requests_mock.get(
        'https://api.apilayer.com/checkiday/events',
        json={'error': 'MyError!'},
        status_code=401
    )
    client = holidays.client('abc123')
    with pytest.raises(RuntimeError) as e:
        client.getEvents()
    assert 'MyError!' == str(e.value)
    assert requests_mock.called

def test_server_error_500(requests_mock):
    requests_mock.get(
        'https://api.apilayer.com/checkiday/events',
        json={},
        status_code=500
    )
    client = holidays.client('abc123')
    with pytest.raises(RuntimeError) as e:
        client.getEvents()
    assert '500' == str(e.value)
    assert requests_mock.called

def test_server_error(requests_mock):
    requests_mock.get(
        'https://api.apilayer.com/checkiday/events',
        exc=requests.exceptions.ConnectTimeout,
    )
    client = holidays.client('abc123')
    with pytest.raises(RuntimeError) as e:
        client.getEvents()
    assert 'Unable to process request.' == str(e.value)
    assert requests_mock.called

def test_server_error_malformed_response(requests_mock):
    requests_mock.get(
        'https://api.apilayer.com/checkiday/events',
        text='{'
    )
    client = holidays.client('abc123')
    with pytest.raises(RuntimeError) as e:
        client.getEvents()
    assert 'Unable to parse response.' == str(e.value)
    assert requests_mock.called

def test_follows_redirects(requests_mock):
    client = holidays.client('abc123')
    requests_mock.get(
        'https://api.apilayer.com/checkiday/events',
        headers={'Location': 'https://api.apilayer.com/checkiday/redirected'},
        status_code=302,
    )
    requests_mock.get(
        'https://api.apilayer.com/checkiday/redirected',
        status_code=200,
        json={},
    )
    client.getEvents()
    assert requests_mock.called

def test_reports_rate_limits(requests_mock):
    client = holidays.client('abc123')
    requests_mock.get(
        'https://api.apilayer.com/checkiday/events',
        headers={
            'X-RateLimit-Remaining-Month': '123',
            'X-RateLimit-Limit-Month': '456',
        },
        json={},
    )
    response = client.getEvents()
    assert requests_mock.called
    assert response['rateLimit']['limitMonth'] == 456
    assert response['rateLimit']['remainingMonth'] == 123
