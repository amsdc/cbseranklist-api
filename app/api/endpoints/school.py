import re
import time
import builtins

from flask import current_app, request
from flask import abort, jsonify
from flask.views import MethodView

from app import mysql
from app.api.auth import basic_auth, token_auth, admin_required
from app.api.helpers.auth import User
from app.api.errors.exceptions import NoSchoolAssociated, SchoolAlreadyAssociated, SchoolAlreadyExists
from app.api.helpers.validation import EMAIL_REGEX, VALID_PREFTYPES


class MeSchool(MethodView):
    decorators = [token_auth.login_required]
    
    def get(self):
        user = token_auth.current_user()
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM `school` WHERE `principal`=%s LIMIT 1;", (user,))
        res = cur.fetchone()
        cur.close()
        if res:
            return {
                "id": res[0],
                "name": res[1],
                "affiliation_number": res[2],
                "school_code": res[3],
                "address": res[4],
                "phone": res[5],
                "principal": res[6]
            }
        else:
            raise NoSchoolAssociated
        
    def put(self):
        user = token_auth.current_user()
        cur = mysql.connection.cursor()
        data = request.get_json()
        
        cur.execute("SELECT * FROM `school` WHERE `principal`=%s;", (user,))
        if cur.fetchone():
            raise SchoolAlreadyAssociated
        
        cur.execute("SELECT * FROM `school` WHERE `aff_no`=%s OR `schoolcode`=%s LIMIT 1;", (data["affiliation_number"], data["school_code"]))

        if cur.fetchone():
            raise SchoolAlreadyExists
            
        cur.execute("INSERT INTO `school` (`name`, `aff_no`, `schoolcode`, `address`, `phone`, `principal`) VALUES (%s, %s, %s, %s, %s, %s);", (data["name"], data["affiliation_number"], data["school_code"], data["address"], data["phone"], user))
        mysql.connection.commit()
        
        return "", 201