#!/usr/bin/python3
"""Define the app_views Blueprint."""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')