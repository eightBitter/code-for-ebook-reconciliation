#The ultimate purpose of this script is to a text file, extract the URLs, redirect the URLs, and replace the original URLs with the redirected URLs

#Python library for HTTP requests
import requests

#Retrieve a single URL redirect
r = requests.get('https://link.springer.com/openurl?genre=book&isbn=978-1-4939-3677-9')
print(r.url)
