"""Flask tutorial 102

Write your code below.
Details in the readme.md file.
"""


from flask import Flask, request

app = Flask(__name__)

WEIGHT_RANGE = (0.0, 1000.0)
HEIGHT_RANGE = (0.0, 3.0)


def bmi(height, weight):
    if not HEIGHT_RANGE[0] < height <= HEIGHT_RANGE[1]:
        raise ValueError(f'Height should be in range'
                         f' ({HEIGHT_RANGE[0]}, {HEIGHT_RANGE[1]}>')
    if not WEIGHT_RANGE[0] <= weight <= WEIGHT_RANGE[1]:
        raise ValueError(f'Weight should be in range'
                         f' ({WEIGHT_RANGE[0]}, {WEIGHT_RANGE[1]}>')
    return round(weight / height ** 2, 2)


def compute_bmi(height, weight):
    try:
        height = float(height)
        weight = float(weight)
        return dict(bmi=bmi(height, weight))
    except (ValueError, TypeError) as error:
        return str(error), 400


@app.route("/bmi/")
def calculate_bmi():

    height = request.args.get('height')
    weight = request.args.get('weight')

    if not height:
        return "Missing 'height' parameter", 400
    if not weight:
        return "Missing 'weight' parameter", 400
    return compute_bmi(height, weight)


@app.route('/bmi2/height/<string:height>/weight/<string:weight>/')
def calculate_bmi2(height, weight):
    return compute_bmi(height, weight)


@app.route("/")
def status():
    return dict(status="ok")


if __name__ == '__main__':
    app.run(debug=True)
