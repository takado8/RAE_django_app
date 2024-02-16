import os

import requests


url = os.environ.get('API_URL') + '/api/v1/lead/'
auth_token = os.environ.get('AUTH_TOKEN')
campaign_token = os.environ.get('CAMPAIGN_TOKEN')
headers = {'Authorization': 'Token ' + auth_token, 'Content-Type': 'application/json'}


def post_lead(phone, name=None, surname=None, email=None, comments: list = None):
    payload = {
        'campaign_token': f'{campaign_token}',
        'phone': f'{phone}',
    }
    if email:
        payload['email'] = email
    if name:
        payload['name'] = name
    if surname:
        payload['surname'] = surname
    if comments:
        payload['comments'] = comments

    print("POST Lead: ")
    print(f'URL: {url}')
    print(f'Headers: {headers}')
    print(f'payload: {payload}')
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("API call successful")
        print("Response:", response.json())
    else:
        print("API call failed with status code:", response.status_code)
        print("Response:", response.text)
