import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/"

get_response = requests.get(endpoint, json={'query': 'Hello World'}) #HTTP requests
print(get_response.text) #print raw text response
print(get_response.status_code)

# HTTP Request -> HTML
# REST API HTTP Requests - > JSON
# Javascript Object Notation -> Python Dict
# print(get_response.json())
# print(get_response.status_code)