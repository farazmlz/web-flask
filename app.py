from flask import Flask 
from views import views, render_template

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

#  main home page
@app.route("/")
def HOME():
    # return "this is home page"
    return render_template("index.html", name="faraz")


if __name__ == '__main__':
    app.run(debug=False, port='0.0.0.0')