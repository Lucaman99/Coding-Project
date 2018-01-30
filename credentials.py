from passlib.hash import pbkdf2_sha256
import rethinkdb as r
# from apogee import bcrypt
# todo maybe use flask-bcrypt instead of pbkdf2_sha256
conn = r.connect(db='apogee').repl()


def verify(username, password):
    username = username.lower()
    try:
        return pbkdf2_sha256.verify(password, r.table('users').get(username).run()['hash'])
    except TypeError: return False


def new_user(username, password):
    username = username.lower()
    hashed = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
    if r.table('users').insert({'username': username, 'hash': hashed}).run()['errors'] > 0:
        return 'That username already exists'
    return 'User has been created.'


def change_password(username, old_password, new_password):
    try:
        if not pbkdf2_sha256.verify(old_password, r.table('users').get(username).run()['hash']):
            return 'ERROR: Incorrect old password'
    except TypeError: return 'ERROR: USERNAME DOES NOT EXIST'
    hashed = pbkdf2_sha256.encrypt(new_password, rounds=200000, salt_size=16)
    r.table('users').get(username).update({'hash': hashed}).run()
    return 'Your password has been changed.'


if __name__ == '__main__':
    # THIS IS ALL TESTING
    print(new_user('elijah', 'testing123'))
    print(new_user('jack', 'aftermath'))
    print(change_password('eli', 'aftermath', 'testing123'))
    print(change_password('elijah', 'aftermath', 'testing123'))
    # print(change_password('elijah', 'testing123', 'aftermath'))
    print(verify('elijah', 'aftermath'))
    # hash = pbkdf2_sha256.encrypt('PASSWORD', rounds=200000, salt_size=16)
