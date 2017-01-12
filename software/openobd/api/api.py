import requests
import requests.auth
import json

class Api():
	def __init__(self):
		self.user = 'kaiboma7'
		self.password = 'Kaiboma12!'
		self.CLIENT_ID = '2e11dd1f-5c1d-4fd5-9b71-d50a3c6734d1'
		self.CLIENT_SECRET = 'daec554c-337b-486b-9681-47b71b76e0c8'
		self.REDIRECT_URI = 'myfirstmojio://'
		self.access_token = None
		self.refresh_token = None
		self.token_type = None
		self.expires_in = None

	def get_auth(self):	
		data = {"userName": self.user, "password": self.password, "grant_type": "password", "client_id" : self.CLIENT_ID, "client_secret" : self.CLIENT_SECRET}
		headers = {'Content-Type': 'x-www-form-urlencoded'}
		response = requests.post("https://accounts.moj.io/oauth2/token", data=data, headers=headers)

		if(response.status_code == 200):
			resp = response.json()
			self.access_token = resp['access_token']
			self.refresh_token = resp['refresh_token']
			self.token_type = resp['token_type']
			self.expires_in = resp['expires_in']
			print(resp)
		else:
			print("Bad Request...")

	def get_me(self):

		headers = {'Content-Type': 'x-www-form-urlencoded', 'Accept-Language': 'en', 'Authorization': self.token_type + ' ' + self.access_token}

		response = requests.get("https://api.moj.io/v2/me", headers = headers)

		print(response.json())

	def get_refresh_token(self):
		data = {"refresh_token": self.refresh_token, "grant_type": "refresh_token", "client_id" : self.CLIENT_ID, "client_secret" : self.CLIENT_SECRET}
		headers = {'Content-Type': 'x-www-form-urlencoded'}
		response = requests.post("https://accounts.moj.io/oauth2/token", data=data, headers=headers)

		if(response.status_code == 200):
			resp = response.json()
			self.access_token = resp['access_token']
			self.refresh_token = resp['refresh_token']
			self.token_type = resp['token_type']
			self.expires_in = resp['expires_in']
			print(resp)
		else:
			print("Bad Request...")

	def get(self, *args, **kargs):
		return

	def post(self, path, data, header):
		response = requests.post(path, data=data, headers=headers)
		return response.json()

	def put(self, path, data, header):
		response = requests.put(path, data=data, headers=headers)
		return response.json()
	def delete(self, path, data, header):
		response = requests.delete(path, data=data, headers=headers)
		return response.json()
