from flask import Flask, render_template_string
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

app = Flask(__name__)

BASE_URL = "https://shadowfox.in/"

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Scraped Links</title>
    <style>
        body { font-family: Arial; background: #f4f4f4; padding: 20px; }
        .card {
            width: 60%%; margin: auto; background: white;
            padding: 20px; border-radius: 10px;
            box-shadow: 0 0 10px gray;
        }
        a {
            font-size: 18px;
            color: blue;
            text-decoration: none;
        }
        a:hover { text-decoration: underline; }
        li { margin: 10px 0; }
    </style>
</head>
<body>
    <div class="card">
        <h2>ShadowFox Redirecting Links</h2>
        <ul>
            {% for title, href in scraped_data %}
            <li><a href="{{ href }}" target="_blank">{{ title }}</a></li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

def scrape_website():
    scraped_items = []

    try:
        response = requests.get(BASE_URL, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        links = soup.find_all("a")

        for link in links:
            title = link.get_text(strip=True)
            href = link.get("href")

            if title and href:
                # FIX: convert relative URL → FULL URL
                full_url = urljoin(BASE_URL, href)
                scraped_items.append((title, full_url))

    except Exception as e:
        scraped_items.append((f"Error: {e}", "#"))

    return scraped_items


@app.route("/")
def index():
    scraped_data = scrape_website()
    return render_template_string(HTML_PAGE, scraped_data=scraped_data)


if __name__ == "__main__":
    app.run(debug=True)
