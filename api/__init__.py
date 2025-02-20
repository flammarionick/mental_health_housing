#!/usr/bin/python3
"""Initialize the API package."""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.users import *
from api.v1.views.housing import *
from api.v1.views.bookings import *
from api.v1.views.reviews import *