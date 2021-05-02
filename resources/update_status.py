from flask_restful import Resource, reqparse
from db import query
import pymysql
from flask_jwt_extended import jwt_required
from datetime import datetime
import pytz;


# this resource is for the users to get papers for a subject yearwise
class UpdateStatus(Resource):

    #@jwt_required    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('park_id', type=int, required=True, help="park_id cannot be left blank!")
        parser.add_argument('availability', type=str, required=True, help="availability cannot be left blank!")
        data = parser.parse_args()
        #create query string
        dt = datetime.now(pytz.timezone('Asia/Kolkata'))
        timestamp = dt.strftime('%Y-%m-%d %H:%M:%S')
        #print(timestamp)
        qstr = f""" 
        update parking
        set available = "{ data['availability'] }", 
        last_updated = "{ timestamp }" 
        where park_id = "{ data['park_id'] }";
        """
        #print(qstr)
        try:
            query(qstr)
            return {
            "message" : "Succesfully updated."
            }, 200
        except Exception as e:
            return {
                "message" : "There was an error updating the database." + str(e)
            }, 500

    #@jwt_required    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('park_id', type=int, required=True, help="park_id cannot be left blank!")
        parser.add_argument('availability', type=str, required=True, help="availability cannot be left blank!")
        data = parser.parse_args()
        #create query string
        dt = datetime.now(pytz.timezone('Asia/Kolkata'))
        timestamp = dt.strftime('%Y-%m-%d %H:%M:%S')
        #print(timestamp)
        qstr = f""" 
        update parking
        set available = "{ data['availability'] }", 
        last_updated = "{ timestamp }" 
        where park_id = "{ data['park_id'] }";
        """
        #print(qstr)
        try:
            query(qstr)
            return {
            "message" : "Succesfully updated."
            }, 200
        except Exception as e:
            return {
                "message" : "There was an error updating the database." + str(e)
            }, 500
