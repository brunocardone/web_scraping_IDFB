import requests
from bs4 import BeautifulSoup
import pandas as pd

from csv import writer


def correr_API(url_API):
    from Correndo_Lista import nomedaplanilha
    headers = {
        'authority': 'lookup-id.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'origin': 'https://lookup-id.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://lookup-id.com/',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': '__cfduid=d3fad46eb41aa9e619ca5cc984a81ee2d1619273628; _ga=GA1.2.1577581479.1619273630; _gid=GA1.2.332210037.1619273630; __atssc=google%3B1; __atuvc=13%7C16; _gat=1',
    }

    url = url_API
    #url = 'https://www.facebook.com/bruno.cardone'
    data = {
      'fburl': url,
      'check': 'Lookup'
    }

    response = requests.post('https://lookup-id.com/', headers=headers, data=data)
    content = response.content

    site = BeautifulSoup(content, 'html.parser')
    try:
        User_ID = site.find("span", {"id": "code"}).text
        User_Name = site.find("em").text

        List = [User_ID, User_Name]
        # Open our existing CSV file in append mode
        # Create a file object for this file
        with open(f"{nomedaplanilha}.csv", 'a') as f_object:
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f_object)

            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(List)

            # Close the file object
            f_object.close()

        print(User_ID, User_Name)
    except:
        pass
