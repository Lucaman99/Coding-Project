import requests
import rethinkdb as r


user_info_conn = r.connect(db='userinfo', user='apogee', password='93+GhEbWQXW9vfDY').repl()
# conn = r.connect(db='userinfo', user='apogee', password='93+GhEbWQXW9vfDY').repl()
# r.table('heroes').run()


def send_message(username, password, recipient, message):  # how client side should work, make it for server side tho
    post_data = {'username': username, 'password': password, 'recipient': recipient, 'message': recipient}
    resp = requests.post('http://localhost:99/sendmsg', data=post_data)
    return resp


def check_for_new_messages(username):

    return 'Message sent'
    # return 'Message not sent'

# on client-side add a backup to google drive option
