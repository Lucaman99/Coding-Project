import requests

post_data = {'username': 'elijah', 'password': 'test', 'recipient': 'eli', 'message': 'asdapskdpoa'}
r = requests.post('http://localhost:99/sendmsg', data=post_data)
