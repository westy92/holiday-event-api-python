import requests

class client:
    def __init__(self, apiKey: str):
        if not apiKey:
            raise ValueError('Please provide a valid API key. Get one at https://apilayer.com/marketplace/checkiday-api#pricing.')
        self.apiKey = apiKey

    def getEvents(self, date: str = None, adult: bool = False, timezone: str = None):
        params = {
            'adult': str(adult).lower(),
        }
        if date:
            params['date'] = date
        if timezone:
            params['timezone'] = timezone

        return self.__request('events', params)

    def getEventInfo(self, id: str, start: int = None, end: int = None):
        if not id:
            raise ValueError('Event id is required.')
        params = {
            'id': id,
        }
        if start != None:
            params['start'] = str(start)
        if end != None:
            params['end'] = str(end)

        return self.__request('event', params)

    def search(self, query: str, adult: bool = False):
        if not query:
            raise ValueError('Search query is required.')
        params = {
            'query': query,
            'adult': str(adult).lower(),
        }

        return self.__request('search', params)

    def __request(self, path, parameters):
        baseUrl = "https://api.apilayer.com/checkiday/" # TODO class const
        headers = {
            'apikey': self.apiKey,
            'User-Agent': "HolidayApiPython/0.0.1" # TODO class const, build from version somewhere?
        }
        url = baseUrl + path

        data = {}
        response = None
        try:
            response = requests.get(url, params=parameters, headers=headers)
            data = response.json()
            data['rateLimit'] = {
                'limitMonth': int(response.headers.get('X-RateLimit-Limit-Month', '0')),
                'remainingMonth': int(response.headers.get('X-RateLimit-Remaining-Month', '0')),
            }
        except Exception:
            if response is None:
                raise RuntimeError('Unable to process request.')
            elif response.ok:
                raise RuntimeError('Unable to parse response.')

        if not response.ok:
            # TODO response.reason https://github.com/psf/requests/issues/6303
            raise RuntimeError(data.get('error', response.status_code))

        return data
