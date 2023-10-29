#!/usr/bin/python3
"""
API status
"""

from flask import jsonify
from api.v1.views import app_views

from models import storage


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """
    status route
    """
    data = {
        "status": "OK"
    }

    result = jsonify(data)
    result.status_code = 200

    return result
