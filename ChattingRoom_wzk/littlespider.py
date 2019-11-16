"""
spider to get pratices of china.cssc.org
"""

import requests
from bs4 import BeautifulSoup


# 获取html文档
def get_html(url):
    """get the content of the url"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text


# 获取笑话
def get_certain_joke(html):
    """get the joke of the html"""
    soup = BeautifulSoup(html, 'lxml')
    joke_content = soup.select('div.content')[0].get_text()

    return joke_content


def write_in(path, content):
    """
    write 'content' to file of 'path'
    """
    with open(path, 'a', encoding='utf-8') as f:
        f.write(content)


pre_url = "http://www.wendangku.net/doc/d4851b7d00f69e3143323968011ca300a6c3f6de"
for i in range(1, 10):
    print(i)
    full_url = pre_url + "-{}.html".format(i)
    html = get_html(full_url)
    content = get_certain_joke(html)
    write_in('C:/Users/zhikangwang/Desktop/4.txt', content)

# joke_content = get_certain_joke(html)
# print(joke_content)


