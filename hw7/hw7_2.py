import json
import requests


def get_info_from_site(site):
    with open('first.txt', 'w') as file:
        response = requests.get(site)
        first_json = json.dumps(dict(response.headers), sort_keys=True, indent=4)

        # sort_keys - для сортировки по алфавиту,
        # indent - отступы (без указания параметра (даже indent=0) нет разделения по строкам)

        print(first_json)
        file.write(first_json)
        file.close()


if __name__ == '__main__':
    get_info_from_site('https://jsonplaceholder.typicode.com/')
