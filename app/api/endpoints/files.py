from flask import request
from flask import jsonify
from flask.views import MethodView


class MyFiles(MethodView):
    decorators = [token_auth.login_required]
    
    def get(self):
        user = token_auth.current_user()
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM `file` WHERE `user`=%s;", (user,))
        res = []
        for r in cur.fetchall():
            res.append({
                "id": r[0],
                "name": r[1],
                "mime": r[2],
                "created": r[3].isoformat('T'),
                "modified": r[4].isoformat('T')
            })
        return res
        
    def post(self):
        pass