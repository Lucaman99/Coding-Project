from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home(): return render_template('test.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    print(text)
    processed_text = f'You sent {text}'
    return render_template('test.html', display_text=processed_text)


app.run(host='localhost', port='99')
