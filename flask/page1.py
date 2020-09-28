from flask import Flask, request, render_template, make_response, redirect, g, abort
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return render_template('index.html', name=request.args['name'], lastname=request.args['lastname'])
# http://127.0.0.1:5000/?name=Andruxa&lastname=Xpen


@app.after_request
def after_request(response):
    print("after_request() called")
    return response

@app.errorhandler(404)
def http_404_handler(error):
    return "<p>Оёёшеньки, что-то пошло не так. такой странички мы не можем найти :(</p>", 404

@app.route("/")
def helloWorld():
    return "Hello World"

@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)

@app.route('/books/<genre>/')
def books(genre):
    return f"All Books in {genre} category"


@app.route('/transfer')
def transfer():
    return "", 302, {'location': 'http://localhost:5000/user/50'}

if __name__ == "__main__":
    app.run(debug=True)