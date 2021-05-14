from flask_restful import Resource, reqparse
from db import query
import pymysql
from flask_jwt_extended import jwt_required

# this resource is for the users to get papers for a subject yearwise
class GetNearestSlots(Resource):

    #@jwt_required    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('latitude', type=float, required=True, help="latitude cannot be left blank!")
        parser.add_argument('longitude', type=float, required=True, help="longitude cannot be left blank!")
        parser.add_argument('vehicle', type=int, required=True, help="did cannot be left blank!")
        parser.add_argument('locality', type=int, required=True, help="did cannot be left blank!")
        data = parser.parse_args()
        #create query string
        qstr = f""" 
        SELECT
        park_id, detail, available, (
            6371 * acos (
            cos ( radians({ data["latitude"] }) )
            * cos( radians( latitude ) )
            * cos( radians(longitude) - radians({ data["longitude"] }) )
            + sin ( radians({ data["latitude"] }) )
            * sin( radians( latitude ) )
            )
        ) AS distance
        FROM parking
        WHERE locality = '{ data["locality"] }' AND vehicle_type = '{ data["vehicle"] }'
        AND available = 1
        ORDER BY distance;
        """

        print(qstr)
        
        try:
            return query(qstr)
        except Exception as e:
            return {
                "message" : "There was an error accessing the database." + str(e)
            }, 500


    #@jwt_required    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('latitude', type=float, required=True, help="latitude cannot be left blank!")
        parser.add_argument('longitude', type=float, required=True, help="longitude cannot be left blank!")
        parser.add_argument('vehicle', type=int, required=True, help="did cannot be left blank!")
        parser.add_argument('locality', type=int, required=True, help="did cannot be left blank!")
        
        data = parser.parse_args()
        #create query string
        qstr = f""" 
        SELECT
        park_id, detail, available, (
            6371 * acos (
            cos ( radians({ data["latitude"] }) )
            * cos( radians( latitude ) )
            * cos( radians(longitude) - radians({ data["longitude"] }) )
            + sin ( radians({ data["latitude"] }) )
            * sin( radians( latitude ) )
            )
        ) AS distance
        FROM parking
        WHERE locality = '{ data["locality"] }' AND vehicle_type = '{ data["vehicle"] }'
        AND available = 1
        ORDER BY distance;
        """
        try:
            return query(qstr)
        except Exception as e:
            return {
                "message" : "There was an error accessing the database." + str(e)
            }, 500