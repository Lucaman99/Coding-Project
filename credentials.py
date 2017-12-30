from passlib.hash import pbkdf2_sha256
import pandas as pd


def verify(username, password):
    username = username.lower()
    df = pd.read_csv('private.csv')
    usernames = df['USERNAME'].tolist()
    hashes = df['HASH'].tolist()
    return pbkdf2_sha256.verify(password, hashes[usernames.index(username)])


def new_user(username, password):
    username = username.lower()
    hashed = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
    df = pd.read_csv('private.csv')
    usernames = df['USERNAME'].tolist()
    if username in usernames: return 'A user with that username already exists!'
    last_row = len(usernames)
    df.loc[last_row] = username, hashed
    df.to_csv('private.csv', index=None)
    return 'User has been created.'


def change_password(username, new_password):
    # todo: add parameter old_password
    username = username.lower()
    hashed = pbkdf2_sha256.encrypt(new_password, rounds=200000, salt_size=16)
    df = pd.read_csv('private.csv')
    usernames = df['USERNAME'].tolist()
    if username not in usernames: return 'ERROR CONTACT SUPPORT'
    df.loc[usernames.index(username)]['HASH'] = hashed
    df.to_csv('private.csv', index=None)
    return 'Your password has been changed.'


if __name__ == '__main__':
    # print(new_user('elijah', 'asdas'))
    change_password('elijah', 'test')
    # print(verify('elijah', 'test'))
    # hash = pbkdf2_sha256.encrypt('PASSWORD', rounds=200000, salt_size=16)
