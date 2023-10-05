import requests
import json

def main():
    key = "5d8b1341b10c417094f3ec24d148888f"
    search = "construction"
    url = f"https://newsapi.org/v2/everything?q={search}&from=2023-09-05&sortBy=publishedAt&apiKey={key}"

    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        articles = json_data["articles"]
        for article in articles:
            "article is json"
            source = article["source"]
            author = article["author"]
            title = article["title"]
            description = article["description"]
            url = article["url"]
            url_to_image = article["urlToImage"]
            publised_at = article["publishedAt"]
            content = article["content"]
            parse_title(article)
    else:
        print(response.status_code)



def parse_title(title):
    #find rating of the title
    print(title)
    return 0

main()


