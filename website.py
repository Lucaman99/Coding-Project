from flask import Flask, render_template, request
import credentials

app = Flask(__name__)

# {
#     msg: "asdkpoaskdpoaks"
#     sender: ""
#     receiver: ""
# }


@app.route('/')
def home():
    # return redirect(url_for('login'))
    return render_template('home.html')


@app.route('/weblogin', methods=['GET'])
def app_login():
    username = request.args.get('username')
    password = request.args.get('password')
    response = str(credentials.verify(username, password))
    return response
    # return render_template('test.html', display_text=response)


@app.route('/login')
def login():
    return render_template('test.html')


# todo: make a web login version

# @app.route('/success/<name>')
# def success(name):
#     return 'welcome %s' % name


app.run(host='localhost', port='99')
