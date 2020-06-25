from flask import jsonify


class BadRequestError(ValueError):
    pass


def bad_request(message):
    if message is None:
        response = jsonify({'message': message})
        response.status_code = 400
    return response
