import requests
from pprint import pprint

from urllib.parse import urlencode

APP_ID = 'b2b47346041546fab15e847b645d3fe9'
AUTH_URL = 'https://oauth.yandex.ru/authorize'

auth_url_data = {
    'response_type': 'token',
    'client_id': APP_ID
}

print('?'.join((AUTH_URL, urlencode(auth_url_data))))

TOKEN = 'AQAAAAAcVNslAATIrN2nnub4HktyujxM8jwrzuk'

class YandexMetrikaUser:
    def __init__(self, token):
        self.token = token
        self.counter_id = 0

    def get_counter(self):
        headers = {
            'oauth_token': self.token,
            'Authorization': 'OAuth {}'.format(self.token),
            'Content-Type': 'application/json'
        }
        response = requests.get('https://api-metrika.yandex.ru/management/v1/counters',
                               headers=headers)
        if response.status_code == 200:
            resp_dict = response.json()
            self.counter_id = resp_dict['counters'][0]['id']
            # pprint(response.json())
        # return response.json()

    def get_counter_visits(self):
        headers = {
            'oauth_token': self.token,
            'Authorization': 'OAuth {}'.format(self.token),
            'Content-Type': 'application/json'
        }

        params = {
            'oauth_token': self.token,
            'id': self.counter_id,
            'metrics': 'ym:s:visits'
        }

        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data',
                                params=params)
        print(response.status_code)
        print(response.text)
        print(response.headers)

        if response.status_code == 200:
            pprint(response.json())
        # return response.json()

metrika = YandexMetrikaUser(TOKEN)
metrika.get_counter()
metrika.get_counter_visits()

# counters = get_counter_list(TOKEN)
# print(counters)



    # visits = get_counter_visits('47502862', TOKEN)
    # print(visits)

