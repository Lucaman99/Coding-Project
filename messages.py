import requests


def send_message(username, password, recipient, message):
    post_data = {'username': username, 'password': password, 'recipient': recipient, 'message': recipient}
    r = requests.post('http://localhost:99/sendmsg', data=post_data)
    return r