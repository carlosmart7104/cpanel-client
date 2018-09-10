import requests

class cPanel():
	"""
		cPanel es una clase que permite gestionar servidores con cPanel API v2
	"""
	init = {
		'protocol': 'https',
		'host': 'cpanel.example.com',
		'port': '2083',
		'token': 'cpsess##########',
		'api_url': 'json-api/cpanel'
	}

	api = {
		'cpanel_api_user': 'username',
		'cpanel_api_version': '2',
		'cpanel_api_module': 'Module',
		'cpanel_api_func': 'function',
		'params_string': '&key=value&another_key=another_value'
	}

	auth = {
		'user': 'username',
		'password': 'password'
	}

	query_string = ''
	res = None

	def __init__(self, args, api = None, auth = None):
		for k in args.keys():
			self.init[k] = args[k]
		if (api != None):
			for k in api.keys():
				self.api[k] = api[k]
		if (auth != None):
			for k in auth.keys():
				self.auth[k] = auth[k]

	def set_api_func(self, args):
		for k in args.keys():
			self.api[k] = args[k]

	def set_auth(self, user = 'root', password = ''):
		self.auth['user'] = user
		self.auth['password'] = password

	def set_query(self, query_string = None):
		if (query_string == None):
			host = '{}://{}:{}/{}/{}'.format(self.init['protocol'], self.init['host'], self.init['port'], self.init['token'], self.init['api_url'])
			api = 'cpanel_jsonapi_user={}&cpanel_jsonapi_apiversion={}&cpanel_jsonapi_module={}&cpanel_jsonapi_func={}'.format(self.api['cpanel_api_user'], self.api['cpanel_api_version'], self.api['cpanel_api_module'], self.api['cpanel_api_func'])
			params = self.api['params_string']
			self.query_string = '{}?{}{}'.format(host, api, params)
		elif (type(query_string) == str):
			self.query_string = query_string
		else:
			self.query_string = ''

	def request(self, params_string = None):
		if (params_string != None):
			self.api['params_string'] = params_string

		self.set_query()
		res = requests.get(self.query_string, auth=(self.auth['user'], self.auth['password'])).json()
		self.res = res['cpanelresult']

	def response(self):
		return self.res

	def get_errors(self):
		return self.res['error']

	def get_event(self):
		return self.res['event']

	def get_result(self):
		return self.res['event']['result']

	def get_data(self):
		return self.res['data']