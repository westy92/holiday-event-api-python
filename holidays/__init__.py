from http.client import responses
import marshmallow_dataclass
import requests
from holidays.types import GetEventInfoResponse, GetEventsResponse, SearchResponse


class client:
    """The API Client"""
    def __init__(self, apiKey: str):
        """Initializes an API client"""
        if not apiKey:
            raise ValueError('Please provide a valid API key. Get one at https://apilayer.com/marketplace/checkiday-api#pricing.')
        self.apiKey = apiKey

    def getEvents(self, date: str = None, adult: bool = False, timezone: str = None) -> GetEventsResponse:
        """Gets the Events for the provided Date"""
        params = {
            'adult': str(adult).lower(),
        }
        if date:
            params['date'] = date
        if timezone:
            params['timezone'] = timezone

        return self.__request('events', params, GetEventsResponse)

    def getEventInfo(self, id: str, start: int = None, end: int = None) -> GetEventInfoResponse:
        """Gets the Event Info for the provided Event"""
        if not id:
            raise ValueError('Event id is required.')
        params = {
            'id': id,
        }
        if start is not None:
            params['start'] = str(start)
        if end is not None:
            params['end'] = str(end)

        return self.__request('event', params, GetEventInfoResponse)

    def search(self, query: str, adult: bool = False) -> SearchResponse:
        """Searches for Events with the given criteria"""
        if not query:
            raise ValueError('Search query is required.')
        params = {
            'query': query,
            'adult': str(adult).lower(),
        }

        return self.__request('search', params, SearchResponse)

    def __request(self, path, parameters, resultClass):
        baseUrl = 'https://api.apilayer.com/checkiday/'  # TODO class const
        headers = {
            'apikey': self.apiKey,
            # TODO class const, build from version somewhere?
            'User-Agent': 'HolidayApiPython/1.0.0',
        }
        url = baseUrl + path

        data = {}
        response = None
        result = None
        try:
            response = requests.get(url, params=parameters, headers=headers)
            data = response.json()
            data['rateLimit'] = {
                'limitMonth': int(response.headers.get('X-RateLimit-Limit-Month', '0')),
                'remainingMonth': int(response.headers.get('X-RateLimit-Remaining-Month', '0')),
            }
            schema = marshmallow_dataclass.class_schema(resultClass)()
            result = schema.load(data)
        except Exception:
            if response is None:
                raise RuntimeError('Unable to process request.')
            elif response.ok:
                raise RuntimeError('Unable to parse response.')

        if not response.ok:
            raise RuntimeError(data.get('error', responses.get(response.status_code, response.status_code)))

        return result
