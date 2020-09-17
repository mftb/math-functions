from flask import Flask, request
from functions.math_functions import math

app = Flask(__name__)


@app.route('/', methods=['POST'])
def simulate_endpoint():
    return math(request)


if __name__ == '__main__':
    app.run(debug=True)
