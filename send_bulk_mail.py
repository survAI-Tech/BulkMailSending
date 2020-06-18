# import the necessary packages
import requests
import json
import pandas as pd


emails = pd.read_csv("resources/Delhi NCR School list - Sheet2.csv")['Email']
# initialize the Keras REST API endpoint URL along with the input
# image path
KERAS_REST_API_URL = "https://b3ae5da223ba.ngrok.io/api/verifyEmail"
# submit the request
for email in emails:
	r = requests.post(KERAS_REST_API_URL,json={"email":str(email)})

	r = r.json()
	if r.success == True:
		print("Email sent successfully to {}".format(email))