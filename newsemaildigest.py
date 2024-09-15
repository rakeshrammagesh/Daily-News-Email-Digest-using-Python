import requests
from send_email import send_email

topic = "tesla"

api_key = "907f13246ea44e968edd8ea18b338000"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&from=2024-08-15&" \
      "sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      "language=en"

request = requests.get(url)

content = request.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" + (article["description"] or "") + "\n" + article["url"] + "\n\n"

body = body.encode("utf-8")

send_email(message=body)