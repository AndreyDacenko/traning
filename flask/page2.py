from flask import Flask, request, render_template
from jinja2 import Template

app = Flask(__name__)

@app.route('/')
def index():
    name, lastname, age, profession = "Andruxa", "Xpen", 22, 'Programmer'
    template_context = dict(name=name, lastname=lastname, age=age, profession=profession)
    return render_template('index2.html', **template_context)

@app.errorhandler(404)
def http_404_handler(error):
    return "<p>Оёёшеньки, что-то пошло не так. такой странички мы не можем найти :(</p>", 404

if __name__ == "__main__":
    app.run()