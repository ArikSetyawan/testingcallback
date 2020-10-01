from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class resource_index(Resource):
	def get(self):
		return jsonify({"message":"helloworld"})

	def post(self):
		try:
			data = request.json
			print(data)
			return jsonify(data)
		except:
			return jsonify({"message":"error"})

api.add_resource(resource_index, "/callback/")

if __name__ == "__main__":
	app.run(debug=True, port=5001)