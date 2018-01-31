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

def get_counter_list(token):
    headers = {
        'Authorization': 'OAuth {}'.format(token),
        'Content-Type': 'application/json'
    }
    response = request.get('https://api-metrika.yandex.ru/management/v1/counters',
                           headers=headers, params={'pretty': 1})

    return response.json()

counters = get_counter_list(TOKEN)
print(counters)

