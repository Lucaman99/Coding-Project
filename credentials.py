from passlib.hash import pbkdf2_sha256
import pandas as pd
# from apogee import bcrypt

# todo use flask-bcrypt instead of pbkdf2_sha256


def verify(username, password):
    username = username.lower()
    df = pd.read_csv('credentials.csv')
    usernames = df['USERNAME'].tolist()
    if username not in usernames: return False
    hashes = df['HASH'].tolist()
    # return bcrypt.check_password_hash(hashes[usernames.index(username)], password)
    return pbkdf2_sha256.verify(password, hashes[usernames.index(username)])


def new_user(username, password):
    username = username.lower()
    hashed = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
    # hashed = bcrypt.generate_password_hash(password)
    df = pd.read_csv('credentials.csv')
    usernames = df['USERNAME'].tolist()
    if username in usernames: return 'A user with that username already exists!'
    last_row = len(usernames)
    df.loc[last_row] = username, hashed
    df.to_csv('credentials.csv', index=None)
    return 'User has been created.'


def change_password(username, new_password):
    # todo: add parameter old_password
    username = username.lower()
    # hashed = bcrypt.generate_password_hash(new_password)
    hashed = pbkdf2_sha256.encrypt(new_password, rounds=200000, salt_size=16)
    df = pd.read_csv('credentials.csv')
    usernames = df['USERNAME'].tolist()
    if username not in usernames: return 'ERROR CONTACT SUPPORT'
    df.loc[usernames.index(username)]['HASH'] = hashed
    df.to_csv('credentials.csv', index=None)
    return 'Your password has been changed.'


def user_exists(username):
    username = username.lower()
    df = pd.read_csv('credentials.csv')
    return username in df['USERNAME'].tolist()


if __name__ == '__main__':
    # print(new_user('elijah', 'asdas'))
    change_password('elijah', 'test')
    # print(verify('elijah', 'test'))
    # hash = pbkdf2_sha256.encrypt('PASSWORD', rounds=200000, salt_size=16)
