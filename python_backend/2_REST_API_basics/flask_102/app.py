"""Flask tutorial 102

Write your code below.
Details in the readme.md file.
"""
from typing import Tuple

from flask import abort, Flask, jsonify, request

from errorhandling import BadRequestError, bad_request


app = Flask(__name__)


@app.route("/")
def status():
    return {"status": "ok"}


@app.route("/bmi/")
def bmi():
    return {"bmi": calculate_bmi(request.args['weight'],
                                 request.args['height'])}


@app.route("/bmi2/height/<height>/weight/<weight>/")
def bmi2(weight: str, height: str):
    return {"BMI": calculate_bmi(weight, height)}


def calculate_bmi(weight: str, height: str) -> float:
    weight, height = convert_params2float_and_check(weight, height)
    return round(weight / height ** 2, 2)


def convert_params2float_and_check(weight: str, height: str) -> \
        Tuple[float, float]:
    try:
        weight = float(weight)
        height = float(height)
    except (ValueError, KeyError):
        raise abort(400)
    if not (0 < height <= 3.0):
        raise BadRequestError("Height should be in range (0.0, 3.0>")
    if not (0 < weight <= 1000):
        raise BadRequestError("Weight should be in range (0.0, 1000.0>")
    return weight, height


@app.errorhandler(BadRequestError)
def bad_request_handler(error):
    return bad_request(str(error))


if __name__ == '__main__':
    app.run(debug=False)
