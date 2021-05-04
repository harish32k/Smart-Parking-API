from flask_restful import Resource, reqparse
from db import query
import pymysql
from flask_jwt_extended import jwt_required

# this resource is for the users to get papers for a subject yearwise
class GetPostalZones(Resource):

    #@jwt_required    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('did', type=int, required=True, help="did cannot be left blank!")
        data = parser.parse_args()
        #create query string
        qstr = f""" 
        select * from postal_zones where did = "{ data['did'] }";
        """
        try:
            return query(qstr)
        except Exception as e:
            return {
                "message" : "There was an error updating the database." + str(e)
            }, 500