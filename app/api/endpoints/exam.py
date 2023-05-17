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

class AllExams(MethodView):
    decorators = [token_auth.login_required]
    
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM `board_ay` ORDER BY `exam_yr` DESC, `std` ASC;")
        
        res = []
        for i in cur.fetchall():
            res.append({
                "id": i[0],
                "year": int(i[1]),
                "std": i[2],
                "parse_engine": i[3]
            })
            
        return jsonify(res)