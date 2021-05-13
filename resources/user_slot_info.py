from flask.json import jsonify
from flask_restful import Resource, reqparse
from db import connectToHost, query, encode
import pymysql
from flask_jwt_extended import jwt_required
from datetime import datetime
import pytz;

# this resource is for the users to get papers for a subject yearwise
class UserSlotInfo(Resource):

    #@jwt_required    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('park_id', type=int, required=True, help="park_id cannot be left blank!")
        parser.add_argument('uid', type=int, required=True, help="uid cannot be left blank!")
        data = parser.parse_args()


        # transaction begins
        conn = connectToHost()
        conn.begin()

        #create query string
        #print(data)

        qstr = f"""
        select park_id, latitude, longitude, vehicle_type, detail, available, last_updated, 
        localities.locality, 
        postal_zones.pincode, zone, 
        dname, 
        (select count(uid) from 
        (select * from bookmarks where park_id = '{ data["park_id"] }' and uid = '{ data["uid"] }') 
        bookmarks) is_bookmarked
        from parking join localities join postal_zones join districts
        on 
        parking.locality = localities.lid and 
        localities.pincode = postal_zones.pincode and
        postal_zones.did = districts.did
        where park_id = '{ data["park_id"] }'
        LIMIT 1;
        """


        
        cursor = conn.cursor()
        cursor.execute(qstr)
        result = encode(cursor.fetchall())

        dt = datetime.now(pytz.timezone('Asia/Kolkata'))
        timestamp = dt.strftime('%Y-%m-%d %H:%M:%S')
        qstr = f"""
        INSERT INTO history (uid, park_id, accessed) VALUES('{data["uid"]}', '{data["park_id"]}',
        '{timestamp}') ON DUPLICATE KEY UPDATE    
        accessed = '{timestamp}';"""
        cursor.execute(qstr)

        conn.commit()
        conn.close()
        cursor.close()

        try:
            return jsonify(result[0])
        except Exception as e:
            print(str(e))
            return {
                "message" : "There was an error accessing the database." + str(e)
            }, 500

old_qstr = """ 
SELECT park_id, latitude, longitude, vehicle_type, detail, available, last_updated, 
localities.locality, 
postal_zones.pincode pincode, zone, 
dname
FROM parking JOIN localities JOIN postal_zones JOIN districts
ON 
(parking.locality = localities.lid AND 
localities.pincode = postal_zones.pincode AND
postal_zones.did = districts.did)
WHERE park_id = '{ data["park_id"] }'
LIMIT 1;
"""