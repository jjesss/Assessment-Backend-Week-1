"""This file defines the API routes."""

# pylint: disable = no-name-in-module

from datetime import datetime, date

from flask import Flask, Response, request, jsonify

from date_functions import (convert_to_datetime, get_day_of_week_on,
                            get_days_between, get_current_age, is_datetime_string)

app_history = []

app = Flask(__name__)


def add_to_history(current_request):
    """Adds a route to the app history."""
    app_history.append({
        "method": current_request.method,
        "at": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "route": current_request.endpoint
    })


def clear_history():
    """Clears the app history."""
    app_history.clear()


@app.get("/")
def index():
    """Returns an API welcome messsage."""
    return jsonify({"message": "Welcome to the Days API."})


@app.route("/between", methods=["POST"])
def date_difference():
    """Returns the number of days between two dates"""
    # validate
    if "first" not in request.json or "last" not in request.json:
        return {"error": "Missing required data."}, 400
    if not isinstance(request.json["first"], str) or not isinstance(request.json["last"], str):
        return {"error": "Unable to convert value to datetime."}, 400
    if (not is_datetime_string(request.json["first"], "%d.%m.%Y") or
            not is_datetime_string(request.json["last"], "%d.%m.%Y")):
        return {"error": "Unable to convert value to datetime."}, 400

    first = convert_to_datetime(request.json["first"])
    last = convert_to_datetime(request.json["last"])
    days = get_days_between(first, last)
    add_to_history(request)
    return jsonify({"days": days})


@app.route("/weekday", methods=["POST"])
def get_day_of_week():
    """Returns the day of the week a specific date is"""
    # validate
    if "date" not in request.json:
        return {"error": "Missing required data."}, 400
    if not isinstance(request.json["date"], str):
        return {"error": "Unable to convert value to datetime."}, 400
    if not is_datetime_string(request.json["date"], "%d.%m.%Y"):
        return {"error": "Unable to convert value to datetime."}, 400

    chosen_date = convert_to_datetime(request.json["date"])
    weekday = get_day_of_week_on(chosen_date)
    add_to_history(request)
    return jsonify({"weekday": weekday})


if __name__ == "__main__":
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    app.run(port=8080, debug=True)
