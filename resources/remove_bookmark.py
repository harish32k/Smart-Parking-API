from flask.json import jsonify
from flask_restful import Resource, reqparse
from db import query
from flask_jwt_extended import jwt_required

# this resource is for the users to get papers for a subject yearwise
class RemoveBookmark(Resource):

    #@jwt_required    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('park_id', type=int, required=True, help="park_id cannot be left blank!")
        parser.add_argument('uid', type=int, required=True, help="uid cannot be left blank!")
        data = parser.parse_args()

        qstr = f"""
        delete from bookmarks where uid = '{data["uid"]}' and park_id = '{data["park_id"]}';
        """


        try:
            query(qstr)
            return jsonify({
                "message" : "Success removing bookmark!"
            })
        except Exception as e:
            print(str(e))
            return {
                "message" : "There was an error accessing the database." + str(e)
            }, 500