from datetime import datetime

from flask import jsonify


def response_error(message, status_code=400, data=None):
    return {
        'message': message,
        "time_stamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'data': data if data else None
    }, status_code


def response_success(data, message, status_code=200):
    return jsonify(
        {'data': data, 'message': message, "time_stamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}), status_code


def response_obj(data, message, status_code=200):
    return jsonify(
        {
            'data': data,
            'message': message,
            "time_stamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    ), status_code
