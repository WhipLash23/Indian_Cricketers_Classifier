from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import util

app = Flask(__name__)


@cross_origin()
@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')

    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Indian Cricketers Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)
