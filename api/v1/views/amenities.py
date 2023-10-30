#!/usr/bin/python3
"""
route for handling Amenity
"""
from flask import jsonify, abort, request
from api.v1.views import app_views, storage
from models.amenity import Amenity


@app_views.route("/amenities", methods=["GET"], strict_slashes=False)
def amenity_get_all():
    """
    retrieves all Amenity objects
    """
    am_list = []
    am_obj = storage.all("Amenity")
    for obj in am_obj.values():
        am_list.append(obj.to_json())

    return jsonify(am_list)


@app_views.route("/amenities", methods=["POST"], strict_slashes=False)
def amenity_create():
    """
    create amenity route
    """
    am_json = request.get_json(silent=True)
    if am_json is None:
        abort(400, 'Not a JSON')
    if "name" not in am_json:
        abort(400, 'Missing name')

    new_am = Amenity(**am_json)
    new_am.save()
    result = jsonify(new_am.to_json())
    result.status_code = 201

    return result


@app_views.route("/amenities/<amenity_id>",  methods=["GET"],
                 strict_slashes=False)
def amenity_by_id(amenity_id):
    """
    gets a specific Amenity object by ID
    :param amenity_id: amenity object id
    :return: state obj with the specified id or error
    """

    amenity = storage.get("Amenity", str(amenity_id))

    if amenity is None:
        abort(404)

    return jsonify(amenity.to_json())


@app_views.route("/amenities/<amenity_id>",  methods=["PUT"],
                 strict_slashes=False)
def amenity_put(amenity_id):
    """
    updates specific Amenity object by ID
    """
    am_json = request.get_json(silent=True)
    if am_json is None:
        abort(400, 'Not a JSON')
    amenity = storage.get("Amenity", str(amenity_id))
    if amenity is None:
        abort(404)
    for key, val in am_json.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(amenity, key, val)
    amenity.save()
    return jsonify(amenity.to_json())


@app_views.route("/amenities/<amenity_id>",  methods=["DELETE"],
                 strict_slashes=False)
def amenity_delete_by_id(amenity_id):
    """
    deletes Amenity by id
    """

    amenity = storage.get("Amenity", str(amenity_id))

    if amenity is None:
        abort(404)

    storage.delete(amenity)
    storage.save()

    return jsonify({})
