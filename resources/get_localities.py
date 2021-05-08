from flask_restful import Resource, reqparse
from db import query
import pymysql
from flask_jwt_extended import jwt_required

# this resource is for the users to get papers for a subject yearwise
class GetLocalities(Resource):

    #@jwt_required    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('pincode', type=int, required=True, help="pincode cannot be left blank!")
        data = parser.parse_args()
        #create query string
        qstr = f""" 
        select * from localities where pincode = "{ data['pincode'] }";
        """
        try:
            return query(qstr)
        except Exception as e:
            return {
                "message" : "There was an error accessing the database." + str(e)
            }, 500

    #@jwt_required    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('pincode', type=int, required=True, help="pincode cannot be left blank!")
        data = parser.parse_args()
        #create query string
        qstr = f""" 
        select * from localities where pincode = "{ data['pincode'] }";
        """
        try:
            return query(qstr)
        except Exception as e:
            return {
                "message" : "There was an error accessing the database." + str(e)
            }, 500