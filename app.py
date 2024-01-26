from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

app = Flask(__name__)

def get_article_details(article_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    }

    response = requests.get(article_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        article_text = " ".join([p.text.strip() for p in soup.find_all('p')])

        image_tag = soup.find('img')
        image_url = urljoin(article_url, image_tag['src']) if image_tag else "N/A"

        return {"article_text": article_text, "image_url": image_url}
    else:
        print(f"Failed to fetch the article. Status code: {response.status_code}")
        return {"article_text": None, "image_url": None}

@app.route('/')
def index():
    sources = [
        {"name": "BBC", "url": "https://www.bbc.com/news"},
        {"name": "CNN", "url": "https://edition.cnn.com/world"},
    ]

    news_list = []

    for source in sources:
        URL = source["url"]

        HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
        }

        for page in range(1, 3):  
            params = {'page': page}
            response = requests.get(URL, headers=HEADERS, params=params)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")

                articles = soup.find_all("div", class_="gs-c-promo") 

                for index, article in enumerate(articles[:20], 1):
                    title = article.find("h3", class_="gs-c-promo-heading__title")
                    title_text = title.text.strip() if title else "N/A"

                    summary = article.find("p", class_="gs-c-promo-summary")
                    summary_text = summary.text.strip() if summary else "N/A"

                    image = article.find("img", class_="qa-lazyload-image")
                    image_url = image['src'] if image else "N/A"

                    link = article.find("a", class_="gs-c-promo-heading")
                    article_url = urljoin(URL, link['href']) if link else "N/A"

                    if article_url != "N/A":
                        details = get_article_details(article_url)
                        aritcle_details = details["article_text"]

                        news_item = {
                            "Source": source["name"],
                            "Title": title_text,
                            "Summary": summary_text,
                            "Image URL": image_url,
                            "Article URL": aritcle_details,
                            "Article Text": details["article_text"],
                            "Article Image URL": details["image_url"]
                        }

                        news_list.append(news_item)

            else:
                return f"Failed to fetch the website. Status code: {response.status_code}"

    return news_list

if __name__ == '__main__':
    app.run(debug=True)
