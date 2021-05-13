from flask_restful import Resource, reqparse
from db import query
import pymysql
from flask_jwt_extended import jwt_required

# this resource is for the users to get papers for a subject yearwise
class UserHistory(Resource):

    #@jwt_required    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('uid', type=int, required=True, help="uid cannot be left blank!")
        data = parser.parse_args()
        #create query string
        qstr = f""" 
        select history.park_id, vehicle_type, detail, accessed
        from history join parking on (history.park_id = parking.park_id) 
        where uid = "{ data['uid'] }" order by accessed desc;
        """
        try:
            return query(qstr)
        except Exception as e:
            return {
                "message" : "There was an error updating the database." + str(e)
            }, 500
