from flask import Flask, render_template, request
import credentials
# from flask_bcrypt import Bcrypt
# import flask_login


app = Flask(__name__)
# bcrypt = Bcrypt(app)
# {
#     msg: "asdkpoaskdpoaks"
#     sender: ""
#     receiver: ""
# }


@app.route('/')
def home():
    # return redirect(url_for('login'))
    return render_template('home.html', name='Apogee')


@app.route('/login/', methods=['GET'])
def app_login():
    # todo: make a css style sheet that hides the input data form
    # todo: make this a POST method
    username = request.args.get('username')
    password = request.args.get('password')
    response = str(credentials.verify(username, password))
    return response
    # return render_template('test.html', display_text=response)


@app.route('/weblogin/')
def login():
    # todo: do this "Enter username: INPUT BOX"
    return render_template('weblogin.html')


@app.route('/about/')
def about():
    return render_template('about.html')
# todo: make a web login version


@app.route('/sendmsg', methods=['POST'])
def sendmsg():
    # todo: make a User class
    username = request.form['username']
    password = request.form['password']
    message = request.form['message']
    recipient = request.form['recipient']
    if not credentials.verify(username, password): return 'message not sent'
    if not credentials.user_exists(username): return 'message not sent'
    # send_message(username, recipient, message)
    return 'message sent'
    # todo: make sendmsg.html with username, password, message, recipient fields


# @app.route('/success/<name>')
# def success(name):
#     return 'welcome %s' % name


app.run(host='localhost', port='99')
