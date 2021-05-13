from flask_restful import Resource, reqparse
from db import query
import pymysql
from flask_jwt_extended import jwt_required

# this resource is for the users to get papers for a subject yearwise
class UserBookmarks(Resource):

    #@jwt_required    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('uid', type=int, required=True, help="uid cannot be left blank!")
        data = parser.parse_args()
        #create query string
        qstr = f""" 
        select bookmarks.park_id, vehicle_type, detail, bookmarked
        from bookmarks join parking on (bookmarks.park_id = parking.park_id) 
        where uid = "{ data['uid'] }" order by bookmarked desc;"""
        try:
            return query(qstr)
        except Exception as e:
            return {
                "message" : "There was an error updating the database." + str(e)
            }, 500
