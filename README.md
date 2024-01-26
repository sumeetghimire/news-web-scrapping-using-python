# news-web-scrapping-using-python



Python News Scraper with Flask
This Python web application leverages Flask, BeautifulSoup, and Requests to scrape news articles from various sources. The project provides a simple web interface to view the latest news headlines, summaries, and additional details.

Features
Scrapes news articles from BBC and CNN websites.
Displays headlines, summaries, images, and links to full articles.
Uses Flask for the web application framework.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/sumeetghimire/news-web-scrapping-using-python
cd Python-News-Scraper
Install dependencies:

bash
Copy code
pip install Flask requests beautifulsoup4
Run the application:

bash
Copy code
python app.py
Open your web browser and navigate to http://127.0.0.1:5000/ to see the latest news in json format.

Usage
Visit the web interface to view the latest news from BBC and CNN.
Click on a news article to see details, including the full article text and image.
How it Works
The application scrapes news articles by sending requests to specified news websites. It extracts relevant information such as headlines, summaries, and article details using BeautifulSoup for HTML parsing.

Dependencies
Flask: Web application framework.
Requests: HTTP library for sending requests.
BeautifulSoup: HTML parsing library.
Disclaimer
This project is for educational purposes only. Be aware of the terms of service of the websites you are scraping, and ensure compliance with ethical considerations and legal regulations.

Contributing
Feel free to contribute to the project by opening issues or submitting pull requests.


