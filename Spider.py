import requests
import json


def scraper(vehicle='samand-lx'):
    url = 'https://bama.ir/cad/api/search'  # ?vehicle=samand%2Clx&pageIndex=1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    cars = list()
    print(f'"{vehicle}" vehicle data receving!')
    for page in range(10):
        payload = {'vehicle': vehicle, 'pageIndex': page}
        response = requests.get(url, headers=headers, params=payload)
        info = json.loads(response.text)
        cars.extend(info['data']['ads'])
        print(f'The number of cars received {len(cars)}')

    return cars