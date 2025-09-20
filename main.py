from pickletools import uint8

import requests
from SendEmail import send_email

api_key="5ff047a2013b4148b21307bb978b39f3"
url=("https://newsapi.org/v2/everything?q=tesla&"
     "from=2025-08-20&sortBy=publishedAt&apiKey="
     "5ff047a2013b4148b21307bb978b39f3")

#Make request
request=requests.get(url)

#Get a dictionary with data
content=request.json()

#Access the article's titles and description
body=""
for article in content["articles"]:
     if article["title"] is not None:
          body=body+article["title"]+"\n"+article["description"]+2*"\n"

body=body.encode("utf-8")
send_email(message=body)

