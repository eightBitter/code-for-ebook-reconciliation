#The ultimate purpose of this script is to a text file, extract the URLs, redirect the URLs, and replace the original URLs with the redirected URLs

#Python library for HTTP requests
import requests

#Retrieve a single URL redirect
r = requests.get('https://link.springer.com/openurl?genre=book&isbn=978-1-4939-3677-9')
print(r.url)

### open/read text file, supply delimiter, print each row
import csv
with open('Sirsi_eBooks.txt', 'rb') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|', quoting=csv.QUOTE_NONE)
    for row in reader:
        print row

### open/read text file, supply delimiter, print each row of the column URL
import csv
with open('Sirsi_eBooks.txt', 'rb') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row['URL'])

### open/read text file, grab the URL from URL column. Redirect each URL and retrieve the redirected URL
import csv
import requests
with open('springer-ebook-url-cleaned.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(requests.get(row['URL']).url)
