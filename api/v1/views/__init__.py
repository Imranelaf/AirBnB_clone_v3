#!/usr/bin/python3
<<<<<<< HEAD
"""create blueprint"""
=======
'''
Creates a Blueprint.
'''


>>>>>>> fc0d1f829812e06cdc55ac1cb92bc5a2a6003f08
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

<<<<<<< HEAD
if app_views is not None:
    from api.v1.views.index import *
    from api.v1.views.states import *
    from api.v1.views.cities import *
    from api.v1.views.amenities import *
    from api.v1.views.users import *
    from api.v1.views.places import *
    from api.v1.views.places_reviews import *
    from api.v1.views.places_amenities import *
=======
>>>>>>> fc0d1f829812e06cdc55ac1cb92bc5a2a6003f08
