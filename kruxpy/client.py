import requests

BASE_URI = 'https://console.krux.com/api/v1'


class Client:
    def __init__(self, username, password, api_key):
        self.auth = (username, password)
        self.api_key = api_key

    @property
    def audiences(self):
        return self._get('audience')

    @property
    def sites(self):
        return self._get('sites')

    @property
    def events(self):
        return self._get('event')

    def get_audience_distribution(self, segment_id):
        return self._get('audience/audience_distribution',
                         segment_id=segment_id)

    def _get(self, path, **params):
        url = "%s/%s" % (BASE_URI, path)
        params['api_key'] = self.api_key
        request = requests.get(url, auth=self.auth, params=params)
        request.raise_for_status()
        return request.json()
