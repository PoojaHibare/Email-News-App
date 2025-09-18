import requests

api_key="5ff047a2013b4148b21307bb978b39f3"
url="https://newsapi.org/v2/everything?q=tesla&"\
     "from=2025-08-18&sortBy=publishedAt&apiKey="\
     "5ff047a2013b4148b21307bb978b39f3"

#Make request
request=requests.get(url)

#Get a dictionary with data
content=request.json()

#Access the article's titles and description
for article in content["articles"]:
     print(article["title"])
     print(article["description"])