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











 # allow CORS for all domains on all routes.

#@flask_app.route("/") # root or index route

#def index():
    #return "Hello Flask ! this is a sample flask app !"

#@flask_app.route("/add/<num1>/<num2>") # adding 2 numbers
#def add_numbers(num1, num2):
    #sumNum = int(num1) + int(num2)
    #return f"this method will add numbers {num1} and {num2} ==> {sumNum}"

#@flask_app.route("/generate") 

 # tweet_a_vs_b = tweeet_creation_data['tweet_a_vs_tweet_b']
    # prediction = tweeet_creation_data['prediction']
    # explanation = tweeet_creation_data['explanation']
    # return f"Prompt is ==> {prompt}\nTweet A VS B ==>{tweet_a_vs_b}\nPrediction is ==> {prediction}\nExplanation is ==> {explanation}"


    
#@flask_app.route(rule: "/tweet")