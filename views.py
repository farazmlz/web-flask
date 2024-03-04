from flask import Blueprint , render_template, jsonify

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return "this is main view page"
    # return render_template("index.html", name="faraz")

@views.route("/json")
def get_json():
    return jsonify({'name' : 'faraz',
                    'coolness' : 10 })