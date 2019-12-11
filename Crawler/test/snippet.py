import requests

start_url = 'http://www.qiushibaike.com'
response = requests.get(start_url)
print (response.status_code)
print (response.text[:5000])

