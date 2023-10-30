#!/usr/bin/python3
"""
route for handling Place
"""
from flask import jsonify, abort, request
from api.v1.views import app_views, storage
from models.place import Place


@app_views.route("/cities/<city_id>/places", methods=["GET"],
                 strict_slashes=False)
def places_by_city(city_id):
    """
    retrieves all Place objects by city
    """
    place_list = []
    city_obj = storage.get("City", str(city_id))
    for obj in city_obj.places:
        place_list.append(obj.to_json())

    return jsonify(place_list)


@app_views.route("/cities/<city_id>/places", methods=["POST"],
                 strict_slashes=False)
def place_create(city_id):
    """
    create place route
    """
    place_json = request.get_json(silent=True)
    if place_json is None:
        abort(400, 'Not a JSON')
    if not storage.get("User", place_json["user_id"]):
        abort(404)
    if not storage.get("City", city_id):
        abort(404)
    if "user_id" not in place_json:
        abort(400, 'Missing user_id')
    if "name" not in place_json:
        abort(400, 'Missing name')

    place_json["city_id"] = city_id

    new_place = Place(**place_json)
    new_place.save()
    result = jsonify(new_place.to_json())
    result.status_code = 201

    return result


@app_views.route("/places/<place_id>",  methods=["GET"],
                 strict_slashes=False)
def place_by_id(place_id):
    """
    gets a specific Place object by ID
    """

    place = storage.get("Place", str(place_id))

    if place is None:
        abort(404)

    return jsonify(place.to_json())


@app_views.route("/places/<place_id>",  methods=["PUT"],
                 strict_slashes=False)
def place_put(place_id):
    """
    updates specific Place object by ID
    :param place_id: Place object ID
    :return: Place object and 200 on success, or 400 or 404 on failure
    """
    place_json = request.get_json(silent=True)

    if place_json is None:
        abort(400, 'Not a JSON')

    place = storage.get("Place", str(place_id))

    if place is None:
        abort(404)

    for key, val in place_json.items():
        if key not in ["id", "created_at", "updated_at", "user_id", "city_id"]:
            setattr(place, key, val)

    place.save()

    return jsonify(place.to_json())


@app_views.route("/places/<place_id>",  methods=["DELETE"],
                 strict_slashes=False)
def place_delete_by_id(place_id):
    """
    deletes Place by id
    """

    place = storage.get("Place", str(place_id))

    if place is None:
        abort(404)

    storage.delete(place)
    storage.save()

    return jsonify({})
