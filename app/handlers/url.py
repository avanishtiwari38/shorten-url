import logging

from flask_restful import Resource
from flask import request

logger = logging.getLogger(__name__)

class Url(Resource):
	"""docstring for Url"""
	def post(self):
		try:
			request_data = request.get_json()
			token = self.randomString()
			request_data['token'] = token
			dataSchema = UrlSchema().load(request_data).data
			db.session.add(dataSchema)
			db.session.commit()
			db.session.close()
			return jsonify(data=token_pool, status=200)
		except DataError as e:
			logger.exception(str(e))
			return jsonify(status=400, msg="Data error")
		except NoResultFound as e:
			logger.exception(str(e))
			return jsonify(status=400, msg=str(e))
		except Exception as e:
			logger.exception(str(e))
			return jsonify(status=400, msg=str(e))

	def randomString(self, stringlength=10):
		"""Generate a random string of fixed length """
		letters = string.ascii_lowercase
		return ''.join(random.sample(letters,stringlength))