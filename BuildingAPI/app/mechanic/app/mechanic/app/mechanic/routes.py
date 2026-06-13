from flask import request, jsonify
from app.models import Mechanic
from app.extensions import db
from . import mechanic_bp
from .schemas import mechanic_schema, mechanics_schema