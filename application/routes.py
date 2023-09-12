from flask import jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from application import app
from application import mongo



@app.route('/', methods=['GET'])
def home():
    response = jsonify("Home page")
    return response

@app.route('/users', methods=['GET','POST'])
def user():
    print("in users api")

    # ROUTE FOR ADDING A NEW USER
    if request.method == 'POST':
        json = request.json
        name = json['name']
        email = json['email']
        pwd = json['pwd']

        if name and email and pwd :

            # HASHING THE PASSWORD
            hashed_pwd = generate_password_hash(pwd)

            id = mongo.db.users.insert_one({
                'name': name,
                'email': email,
                'pwd': hashed_pwd
            })
            response = jsonify("User added successfully!")
            response.status_code = 200
            return response
        else:
            return not_found()
    
    # ROUTE FOR GETTING ALL USERS
    elif request.method == 'GET':
        users = mongo.db.users.find()
        response = dumps(users)
        return response

# *****************************************************************************************
@app.route('/users/<id>', methods=['GET','DELETE', 'PUT'])
def single_user(id):

    # ROUTE FOR GETTING A SPECIFIC USER
    if request.method == 'GET':
        user = mongo.db.users.find_one({'_id': ObjectId(id)})
        response = dumps(user)
        return response
    
    # ROUTE FOR DELETING A SPECIFIC USER 
    elif request.method == 'DELETE':
        mongo.db.users.delete_one({'_id': ObjectId(id)})
        response = jsonify("User has been deleted successfully")
        response.status_code = 200
        return response
    
    # ROUTE FOR CHANGING A SPECIFIC USER
    elif request.method == 'PUT':
        _id = id
        json = request.json
        name= json['name']
        email = json['email']
        pwd = json['pwd']

        if name and email and pwd:
            hashed_pwd = generate_password_hash(pwd)

            mongo.db.users.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},
                                      {
                                          '$set': {
                                              'name': name,
                                              'email': email,
                                              'pwd': hashed_pwd
                                          }
                                      })
            response = jsonify("User has been updated successfully")
            response.status_code = 200
            return response
        else:
            return not_found()

# ERROR HANDLING FUNCTION
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not FOund' + request.url
    }
    response = jsonify(message)
    response.status_code = 404

    return response