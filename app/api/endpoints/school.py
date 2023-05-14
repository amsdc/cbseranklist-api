import re
import time
import builtins

from flask import current_app, request
from flask import abort, jsonify
from flask.views import MethodView

from app import mysql
from app.api.auth import basic_auth, token_auth, admin_required
from app.api.helpers.auth import User
from app.api.errors.exceptions import InvalidEmailTokenError
from app.api.helpers.validation import EMAIL_REGEX, VALID_PREFTYPES


class School(MethodView):
    decorators = [token_auth.login_required]
    
    def get(self):
        user = token_auth.current_user()
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM `school` WHERE `principal`=%s LIMIT 1;", (user,))
        res = cur.fetchone()
        cur.close()
        return {
            "id": res[0],
            "name": res[1],
            "affiliation_no": res[2]
        }
