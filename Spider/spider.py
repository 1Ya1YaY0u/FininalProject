"""
spider to get pratices of china.cssc.org
"""

import requests
from bs4 import BeautifulSoup
from flask import Flask, request

app = Flask(__name__)
global href_list
href_list = []
global base_url
base_url = ""


def get_raw_html(url):
    """get raw html from url"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text


def reconstruct_html(html):
    """reconstruct html, add base url to href"""
    soup = BeautifulSoup(html, 'lxml')
    head = soup.select('head')[0]
    chapter_list_html = soup.find(class_='listmain')
    global href_list
    href_list = [i.get('href') for i in chapter_list_html.find_all('a')]
    chapter_name_list = [i.get_text() for i in chapter_list_html.find_all('a')]
    # print(chapter_name_list)
    new_html = ""
    for i in range(len(chapter_name_list)):
        # href_tag = "<dd><a href=\"" + base_url.rstrip("index.html") + str(href_list[i]) + "\">"
        href_tag = "<dd><a href=\"\{}\">".format(i)
        new_html += href_tag + chapter_name_list[i] + "</a></dd>"
    return str(head) + new_html


def get_content_html(html):
    """select content html from html"""
    soup = BeautifulSoup(html, 'lxml')
    content_html = soup.find(class_='showtxt')
    print(type(content_html))
    return content_html


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
    global base_url
    base_url = url.rstrip('index.html')
    html = get_raw_html(url)
    new_html = reconstruct_html(html)
    # print(new_html)
    return new_html


@app.route('/<int:chapter_index>')
def link2chapter(chapter_index):
    # base_url = "http://www.shuquge.com/txt/8400/"
    global base_url
    url = base_url + href_list[chapter_index]
    print(url)
    html = get_raw_html(url)
    content_html = get_content_html(html)
    return str(content_html)


if __name__ == "__main__":
    # pre_url = "http://www.shuquge.com/txt/63542/"
    # for i in range(1, 3):
    #     print(i)
    #     full_url = pre_url + "-{}.html".format(i)
    #     html = get_html(full_url)
    #     content = get_certain_joke(html)

    # url = "http://www.shuquge.com/txt/63542/index.html"
    # html = get_html(url)
    # content = get_chapter_list(html)

    app.run()
