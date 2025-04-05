from flask import Blueprint

user_bp = Blueprint('user', __name__)

auth_bp = Blueprint('auth', __name__)

admin_bp = Blueprint('admin', __name__)

jobs_bp = Blueprint('jobs', __name__)

from . import auth_routes, user_routes, admin_routes, jobs_routes 

# Don't import routes here to avoid circular imports 

# This file is intentionally left empty to mark this directory as a Python package 