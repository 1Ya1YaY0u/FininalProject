from flask import Flask, request
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)


@app.route('/')
def index():
    # html = """
    # <form>
    # 姓名：
    # <input type="text" name="myName">
    # <br/>
    # 密码：
    # <input type="password" name="pass">
    # </form>"""
    html = """
    <!DOCTYPE html>
    <html>
    <body>

    <form action="/url" method="post">
    URL:<br>
    <input type="text" name="url" value="input url">
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
    # print(url)
    return url


def get_html(url):
    """get the content of the url"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text


# get content
def get_chapter_list(html):
    """get the joke of the html"""
    print(html)
    soup = BeautifulSoup(html, 'lxml')
    # joke_content = soup.select('#contents')[0].get_text()
    # head = soup.select('head')[0]
    # print("head:  \n", head)
    # chapter_list = soup.find(class_='listmain')
    # chapter_list = soup.find_all('a').get_text()
    # href = [i.get('href') for i in chapter_list.find_all('a')]
    # print(str(chapter_list))
    # print(chapter_list)
    # print("href", href)
    # chapter_list = soup.select('.wrap')[0]
    # print("chapter_list.name:", chapter_list.name)
    content = soup.select('.showtxt')
    print(content)

    # return chapter_list
    return content


if __name__ == '__main__':
    # app.run(debug=True)
    # url = "http://www.shuquge.com/txt/63542/index.html"
    url = "http://www.shuquge.com/txt/8400/28344165.html"
    html = get_html(url)
    content = get_chapter_list(html)
