import re
import requests


def lets_find_links(url):
    response = requests.get(url)
    re_pattern = r'a href=\"(https?://.+?)"'
    list_of_links = re.findall(re_pattern, str(response.content), flags=re.MULTILINE)
    for item in list_of_links:
        print(item)
    return list_of_links


if __name__ == '__main__':
    url = 'https://habrahabr.ru/'
    lets_find_links(url)
