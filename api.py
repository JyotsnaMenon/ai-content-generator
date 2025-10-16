from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

from create_tweet import create_tweet

flask_app = Flask(__name__,template_folder='ui')
cors = CORS(flask_app)

@flask_app.route("/") # root or index route
def index():
    return render_template("index.html")

@flask_app.route("/generate")
@cross_origin()
def generate_tweet():
    prompt = request.args.get('prompt')
    tweeet_creation_data =  create_tweet(prompt)
   
    return jsonify(tweeet_creation_data)

if __name__ == "__main__":
    flask_app.run()











 