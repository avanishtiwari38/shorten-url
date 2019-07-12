import logging

from flask_restful import Resource
from flask import request, jsonify

logger = logging.getLogger(__name__)

class Hello(Resource):
	"""docstring for Hello"""
	def get(self):
		return jsonify(msg="It is working", status=200)
