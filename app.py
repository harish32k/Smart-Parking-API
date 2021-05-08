from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

#import resources
from resources.update_status import UpdateStatus
from resources.get_postal_zones import GetPostalZones
from resources.get_nearest_slots import GetNearestSlots
from resources.get_slot_info import GetSlotInfo
from resources.get_localities import GetLocalities

# create flask app instance
app = Flask(__name__)

"""
#set config for jwt
app.config['PROPAGATE_EXCEPTIONS']=True
app.config['JWT_SECRET_KEY'] = 'qp-cbit'
"""

#initialize api
api = Api(app)
api.add_resource(UpdateStatus, '/update-status') #for sensor to set status
api.add_resource(GetPostalZones, '/get-postal') #for postal zones
api.add_resource(GetNearestSlots, '/get-nearest-slots') #for nearest parking slots
api.add_resource(GetSlotInfo, '/get-slot-info')
api.add_resource(GetLocalities, '/get-localities')

"""
jwt=JWTManager(app)

#return an error response if JWT is missing
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'error': 'authorization_required',
        "description": "Request does not contain an access token."
    }), 401

#return an error response if JWT is invalid
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'error': 'invalid_token',
        'message': 'Signature verification failed.'
    }), 401
"""


#a welcome route to test if the flask app is working.
@app.route('/')
def home():
    return(f"""<h1 style="font-family: 'Palatino Linotype';">This is an API for the IoT Smart Parking System.</h1>
                <p style="font-size:2em">Developed by Harish, GDPR</p>""")

# set debug = False while deploying. debug = True is not safe in production environments
if __name__ == '__main__':
    app.run(debug=True)
