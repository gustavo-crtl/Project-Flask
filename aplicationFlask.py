from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/services")
def services():
    return render_template("services.html")

# @app.route("/portfolio")
# def portfolio():
#     return render_template("portfolio.html")

@app.route("/contacts")
def contatos():
    return render_template("contacts.html")

@app.route("/users/<name_user>")
def users(name_user):
    return render_template("users.html", name_user=name_user)

if __name__ == "__main__":
    app.run(debug=True)