#The ultimate purpose of this script is to a text file, extract the URLs, redirect the URLs, and replace the original URLs with the redirected URLs

#Import libraries
import csv
import requests

#Open file with cleaned URLs. Also open a new file where you'll write the redirected URLs
with open('springer-ebook-url-cleaned.csv', 'rb') as originalFile, open('springer-ebook-url-redirected.csv', 'wb') as redirectedFile:
    #Set column names for springer-ebook-url-redirected.csv
    fieldnames = ['title', 'URL']
    #Set variables for the two datasets
    reader = csv.DictReader(originalFile)
    writer = csv.DictWriter(redirectedFile, fieldnames=fieldnames)
    #Let the user know the script is running
    print "Redirecting URLs. Hold on to your butts! This might take a while"
    writer.writeheader()
    #Read each row in the first file; add the title to the new file; redirect each URL and add the redirected URL to the new file
    for row in reader:
        redirectedURL = requests.get(row['URL']).url
        # for line in writer:
        writer.writerow({'title': row['title'], 'URL': redirectedURL})
            #print(requests.get(row['URL']).url)
print "ALL DONE!"

### TODO
# Figure out how to bypass connection issues for single URL problems
# requests.exceptions.ConnectionError: HTTPSConnectionPool(host='link.springer.com', port=443): Max retries exceeded with url: /openurl?genre=book&isbn=978-3-319-46184-7 (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x105dc3f10>: Failed to establish a new connection: [Errno 60] Operation timed out',))
# Insert an error message in the new file to indicate there was a problem with the particular URL
# Using the code block from Trello and test it against the open URL
