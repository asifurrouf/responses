import responses
import requests


responses.add(responses.GET,'http://www.dropbox.com/asif'
                ,body='{"error":"not found"}',status=404)

NewResponse =requests.get('http://www.dropbox.com/asif' )

print NewResponse.text
print NewResponse.status_code
