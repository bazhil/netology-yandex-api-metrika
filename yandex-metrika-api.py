import requests

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


    def get_counter_list(token):
        headers = {
            'Authorization': 'OAuth {}'.format(self.token),
            'Content-Type': 'application/json'
        }
        response = requests.get('https://api-metrika.yandex.ru/management/v1/counters',
                               headers=headers, params={'pretty': 1})

        return response.json()

# counters = get_counter_list(TOKEN)
# print(counters)

def get_counter_visits(counter_id, token):

    headers = {
        'Authorization': 'OAuth {}'.format(token),
        'Content-Type': 'application/json'
    }

    params={
        'id': counter_id,
        'metrics': 'ya:s:visits'
    }

    response = requests.get('https://api-metrika.yandex.ru/management/v1/data', params,
                             headers=headers)
    return response.json()

visits = get_counter_visits('47502862', TOKEN)
print(visits)