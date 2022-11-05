from flask import Flask, render_template

#Creating flask instance

app = Flask(__name__)

# create a route decorator
@app.route('/')

def index():
    first_name = "Oba"
    stuff = "This is bold text"
    favorite_daw = ['Ableton', 'Logic', 'ProTools', 'Reason', 'Serato', 20]

    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,favorite_daw=favorite_daw)


@app.route('/user/<name>')

def user(name):
    return render_template("user.html" ,name=name)

#invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
