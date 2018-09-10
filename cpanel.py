import requests

class cPanel():
	"""
		cPanel is a class that allows you to manage servers with cPanel JSON-API v2
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

	def __init__(self, init = None, api = None, auth = None):
		if (init != None):
			for k in init.keys():
				self.init[k] = init[k]
		if (api != None):
			for k in api.keys():
				self.api[k] = api[k]
		if (auth != None):
			for k in auth.keys():
				self.auth[k] = auth[k]

	def set_api(self, api):
		for k in api.keys():
			self.api[k] = api[k]

	def set_api_module(self, module):
		self.api['cpanel_api_module'] = module

	def set_api_func(self, func):
		self.api['cpanel_api_func'] = func

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
		self.res = requests.get(self.query_string, auth=(self.auth['user'], self.auth['password'])).json()

	def response(self):
		return self.res

	def get_response(self):
		return self.res['cpanelresult']

	def get_preevent(self):
		return self.res['cpanelresult']['preevent']

	def get_preevent_result(self):
		return self.res['cpanelresult']['preevent']['result']

	def get_event(self):
		return self.res['cpanelresult']['event']

	def get_event_result(self):
		return self.res['cpanelresult']['event']['result']

	def get_postevent(self):
		return self.res['cpanelresult']['postevent']

	def get_postevent_result(self):
		return self.res['cpanelresult']['postevent']['result']

	def get_data(self):
		return self.res['cpanelresult']['data']

	def get_errors(self):
		data = self.get_data()
		errors = []
		for d in data:
			if (not 'result' in d):
				break
			if (d['result'] == 0):
				errors.append(d['reason'])
		return errors

	def get_status(self):
		return self.get_errors() == []