from flask import Flask, request, render_template
from jinja2 import Template
app = Flask(__name__)


@app.route('/')
def index():
    name, lastname, age, profession = "Andruxa", "Xpen", 22, 'Programmer'
    template_context = dict(name=name, lastname=lastname, age=age, profession=profession)
    return render_template('index3.html', **template_context)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.10", port=9000)