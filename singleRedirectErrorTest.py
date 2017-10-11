#The ultimate purpose of this script is to a text file, extract the URLs, redirect the URLs, and replace the original URLs with the redirected URLs

#Import libraries
import csv
import requests

#Open file with cleaned URLs. Also open a new file where you'll write the redirected URLs
with open('springer-ebook-url-cleaned-20170929.csv', 'rb') as originalFile, open('springer-ebook-url-redirected-2.csv', 'wb') as redirectedFile:
    #Set column names for springer-ebook-url-redirected.csv
    fieldnames = ['title', 'URL', 'errorMessage']
    #Set variables for the two datasets
    reader = csv.DictReader(originalFile)
    writer = csv.DictWriter(redirectedFile, fieldnames=fieldnames)
    #Let the user know the script is running
    print "Redirecting URLs. Hold on to your butts! This might take a while"
    writer.writeheader()
    #Read each row in the first file; add the title to the new file; redirect each URL and add the redirected URL to the new file
    for row in reader:
        # Try to redirect the URLs
        try:
            redirectedURL = requests.get(row['URL']).url
            # for line in writer:
            writer.writerow({'title': row['title'], 'URL': redirectedURL})
                #print(requests.get(row['URL']).url)
        # If redirecting the URL results in an erro (e.g. the URL times out), then add the error message to the csv and keep running through the rest of the URLs (keeps the script from stopping based on the error)
        except Exception, message:
            writer.writerow({'title': row['title']})
            writer.writerow({'errorMessage': str(message)})

print "ALL DONE!"

### TODO
#  Field limit problem:
#  File "singleRedirectErrorTest.py", line 18, in <module>
#     for row in reader:
#   File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/csv.py", line 108, in next
#     row = self.reader.next()
# _csv.Error: field larger than field limit (131072)
# Problem was created, because OpenRefine messed up some of the column values
# Need to start with a file that doesn't have messed up column values
