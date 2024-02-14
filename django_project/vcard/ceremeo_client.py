import requests


url = 'https://url_systemu/api/v1/lead/'
auth_token = 'your_auth_token'
campaign_token = "campaign_token"
headers = {'Authorization': 'Token ' + auth_token, 'Content-Type': 'application/json'}


def post_lead(phone, email=None, name=None, surname=None, comments: list = None):
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
        payload['comments'] = [{f'comment{i}': comment} for i, comment in enumerate(comments)]

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print("API call successful")
        print("Response:", response.json())
    else:
        print("API call failed with status code:", response.status_code)
        print("Response:", response.text)
