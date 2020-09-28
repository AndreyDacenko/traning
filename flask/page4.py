from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    name, lastname, age, profession = "Andruxa", "Xpen", 22, 'Programmer'
    template_context = dict(name=name, lastname=lastname, age=age, profession=profession)
    return render_template('index3.html', **template_context)


@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    username = ''
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')

    if username == 'root' and password == 'pass':
        message = "Correct username and password"
    else:
        message = "Wrong username or password"

    return render_template('login.html', message=message)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.10", port=9000)
