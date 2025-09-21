import requests
from SendEmail import send_email

topic="tesla"

api_key="5ff047a2013b4148b21307bb978b39f3"
url="https://newsapi.org/v2/everything?"\
     f"q={topic}&"\
     "sortBy=publishedAt&"\
     "apiKey=5ff047a2013b4148b21307bb978b39f3&"\
     "language=en"

#Make request
request=requests.get(url)

#Get a dictionary with data
content=request.json()

#Access the article's titles and description
body=""
for article in content["articles"][:20]:
     if article["title"] is not None:
          body="Subject:Today's News"\
                +"\n"+body+article["title"]+"\n"\
                +article["description"]\
                +"\n"+article["url"]+2*"\n"

body=body.encode("utf-8")
send_email(message=body)

