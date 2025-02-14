# This file is part of MyPHP.

# MyPHP is free software: you can redistribute it and/or modify it under 
# the terms of the GNU General Public License as published by the Free 
# Software Foundation, either version 3 of the License, or (at your 
# option) any later version.

# MyPHP is distributed in the hope that it will be useful, but WITHOUT 
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License 
# for more details.

# You should have received a copy of the GNU General Public License along
# with MyPHP. If not, see <https://www.gnu.org/licenses/>. 

from flask import jsonify, request, \
    render_template
from werkzeug.exceptions import HTTPException

from app import mysql
from app.errors import bp

@bp.app_errorhandler(HTTPException)
def http_error(e):
    mysql.connection.rollback()
    return jsonify({"type": "HTTPException",
                    "message": e.description}), e.code

