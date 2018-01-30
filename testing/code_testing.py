# import requests
# import rethinkdb as r

# conn = r.connect(db='apogee').repl()
# r.db_drop('apogee').run()
# r.table_drop('users').run()
# r.table_create('users', primary_key='username').run()
# print('Tables in apogee:', r.table_list().run())
# y = r.table('users').insert({'username': 'eli', 'hash': '$pbkdf2-sha256$200000$eg9hbK0VgtCaM0YIwdhbKw$6yuGejPDA3j02rVCfG2pOJJgGq/7FTsfM1s3.Vc3bA0'}).run()
# x = r.table('users').get('asdaposdoasijs').update({'hash': 'asdasd'}).run()
# x = r.table('users').insert({'username': 'eli', 'hash': 'test'}).run()
# cursor = r.table('users').run()
# print(cursor)
# print(x)
# r.db_create('apogee')
# conn.use('messages')
# r.db('apogee').table_create('users').run()


# post_data = {'username': 'elijah', 'password': 'test', 'recipient': 'eli', 'message': 'asdapskdpoa'}
# r = requests.post('http://localhost:99/sendmsg', data=post_data)
