from .cpanel import cPanel
class Email(cPanel):
	'''
		cPanel is a class that allows you to manage Email accounts with cPanel JSON-API v2
	'''
	# addpop variables
	domain = 'example.com'
	quota = 250
	sent_welcome_email = False

	def __init__(self, init = None, api = None, auth = None):
		super(Email, self).__init__(init, api, auth)
		self.set_api_module('Email')

	# auxiliary addpop methods 
	def set_domain(self, domain):
		self.domain = domain

	def get_domain(self):
		return self.domain

	def set_quota(self, quota):
		self.quota = quota

	def get_quota(self):
		return self.quota

	def set_sent_welcome_email(self, value):
		self.sent_welcome_email = value

	def get_sent_welcome_email(self):
		return self.sent_welcome_email

	# addpop interface definition
	def addpop(self, email, password, domain = None, quota = None, sent_welcome_email = None):
		self.set_api_func('addpop')
		if (domain != None):
			self.domain = domain
		if (quota != None):
			self.quota = quota
		if (sent_welcome_email != None):
			self.sent_welcome_email = sent_welcome_email
		d, e, p, q, s = self.domain, email, password, self.quota, self.sent_welcome_email
		self.api['params_string'] = '&domain={0}&email={1}&password={2}&quota={3}&sent_welcome_email={4}'.format(d, e, p, q, s)
		self.request()

	# delpop interface definition
	def delpop(self, email, domain = None):
		self.set_api_func('delpop')
		if (domain != None):
			self.domain = domain
		e, d = email, self.domain
		self.api['params_string'] = '&domain={0}&email={1}'.format(d, e)
		self.request()

	# listpops interface definition
	def listpops(self, regex = None):
		self.set_api_func('listpops')
		if (regex != None):
			self.api['params_string'] = '&regex={0}'
		else:
			self.api['params_string'] = ''
		self.request()
		