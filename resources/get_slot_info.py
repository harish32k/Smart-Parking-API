from flask_restful import Resource, reqparse
from db import query
import pymysql
from flask_jwt_extended import jwt_required

# this resource is for the users to get papers for a subject yearwise
class GetSlotInfo(Resource):

    #@jwt_required    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('park_id', type=int, required=True, help="park_id cannot be left blank!")
        data = parser.parse_args()
        #create query string
        print(data)
        qstr = f""" 
        SELECT * FROM parking
        WHERE park_id = '{ data["park_id"] }'
        LIMIT 1;
        """
        print(qstr)
        try:
            return query(qstr, json_array=False)
        except Exception as e:
            print(str(e))
            return {
                "message" : "There was an error accessing the database." + str(e)
            }, 500

    #@jwt_required    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('park_id', type=int, required=True, help="park_id cannot be left blank!")
        data = parser.parse_args()
        #create query string
        print(data)
        qstr = f""" 
        SELECT * FROM parking
        WHERE park_id = '{ data["park_id"] }'
        LIMIT 1;
        """
        print(qstr)
        try:
            return query(qstr, json_array=False)
        except Exception as e:
            print(str(e))
            return {
                "message" : "There was an error accessing the database." + str(e)
            }, 500