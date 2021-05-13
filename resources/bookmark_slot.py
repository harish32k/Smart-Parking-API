from flask.json import jsonify
from flask_restful import Resource, reqparse
from db import connectToHost, query, encode
import pymysql
from flask_jwt_extended import jwt_required
from datetime import datetime
import pytz;

# this resource is for the users to get papers for a subject yearwise
class BookmarkSlot(Resource):

    #@jwt_required    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('park_id', type=int, required=True, help="park_id cannot be left blank!")
        parser.add_argument('uid', type=int, required=True, help="uid cannot be left blank!")
        data = parser.parse_args()

        dt = datetime.now(pytz.timezone('Asia/Kolkata'))
        timestamp = dt.strftime('%Y-%m-%d %H:%M:%S')
        qstr = f"""
        INSERT INTO bookmarks (uid, park_id, bookmarked) VALUES('{data["uid"]}', '{data["park_id"]}',
        '{timestamp}') ON DUPLICATE KEY UPDATE    
        bookmarked = '{timestamp}';"""


        try:
            query(qstr)
            return {
                "message" : "Success bookmarking!"
            }, 500
        except Exception as e:
            print(str(e))
            return {
                "message" : "There was an error accessing the database." + str(e)
            }, 500