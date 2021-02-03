from flask import Flask, jsonify, request 
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__) 
auth = HTTPBasicAuth()

USER_DATA = {
    "admin": "Pritam"
}

@auth.verify_password
def verify(username,password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password
    
Movies = [{'name' : 'The Prestige'}, {'name' : 'Shutter Island'}, {'name' : 'Intestellar'}, {'name' : 'Tenet'}, {'name' : 'Inception'}, {'name' : 'The Shawshank Redemption'}]

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'The RESTful_api is working properly!'})

@app.route('/Film', methods=['GET'])
@auth.login_required
def returnAll():
	return jsonify({'Movies' : Movies})

@app.route('/Film/<string:name>', methods=['GET'])
@auth.login_required
def returnOne(name):
	Film = [Movie for Movie in Movies if Movie['name'] == name]
	return jsonify({'Movie' : Films[0]})

@app.route('/Film', methods=['POST'])
@auth.login_required
def addOne():
	Movie = {'name' : request.json['name']}

	Movies.append(Movie)
	return jsonify({'Movies' : Movies})

@app.route('/Film/<string:name>', methods=['PUT'])
@auth.login_required
def editOne(name):
	Films = [Movie for Movie in Movies if Movie['name'] == name]
	Films[0]['name'] = request.json['name']
	return jsonify({'Movie' : Films[0]})

@app.route('/Film/<string:name>', methods=['DELETE'])
@auth.login_required
def removeOne(name):
	Film = [Movie for Movie in Movies if Movie['name'] == name]
	Movies.remove(lang[0])
	return jsonify({'Movies' : Movies})

if __name__ == '__main__':
	app.run(debug=True)