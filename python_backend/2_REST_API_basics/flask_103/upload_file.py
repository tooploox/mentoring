import requests


if __name__ == '__main__':
    url = 'http://localhost:5000/upload'
    files = {'file': open('data/dog-image.jpg', 'rb')}
    values = {'action': 'scale', 'value': '0.5'}

    r = requests.post(url, files=files, data=values)
    r.raise_for_status()
    print(r)
    print(r.text)
    print(r.content)
