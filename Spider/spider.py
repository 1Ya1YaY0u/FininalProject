"""
spider to get pratices of china.cssc.org
"""

import requests
from bs4 import BeautifulSoup
from flask import Flask, request
app = Flask(__name__)


def get_raw_html(url):
    """get raw html from url"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text


def reconstruct_html(html, base_url):
    """reconstruct html, add base url to href"""
    soup = BeautifulSoup(html, 'lxml')
    head = soup.select('head')[0]
    chapter_list_html = soup.find(class_='listmain')
    href_list = [i.get('href') for i in chapter_list_html.find_all('a')]
    chapter_name_list = [i.get_text() for i in chapter_list_html.find_all('a')]
    print(chapter_name_list)
    new_html = ""
    for i in range(len(chapter_name_list)):
        href_tag = "<dd><a href=\"" + base_url.rstrip("index.html") + str(href_list[i]) + "\">"
        new_html += href_tag + chapter_name_list[i] + "</a></dd>"
    return str(head) + new_html


@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html>
    <body>

    <form action="/url" method="post">
    URL:<br>
    <input type="text" name="url" >
    <br>
    <input type="submit" value="Submit">
    </form>

    </body>
    </html>
    """
    return html


@app.route('/url', methods=["POST", "GET"])
def get_url():
    url = request.form.get('url')
    html = get_raw_html(url)
    new_html = reconstruct_html(html, url)
    print(new_html)
    return new_html


if __name__ == "__main__":
    # pre_url = "http://www.shuquge.com/txt/63542/index.html"
    # for i in range(1, 3):
    #     print(i)
    #     full_url = pre_url + "-{}.html".format(i)
    #     html = get_html(full_url)
    #     content = get_certain_joke(html)

    # url = "http://www.shuquge.com/txt/63542/index.html"
    # html = get_html(url)
    # content = get_chapter_list(html)

    app.run()
