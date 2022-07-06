import requests
import json
import os.path
from time import sleep

url = 'https://bg.annapurnapost.com/api/search?title=%E0%A4%96%E0%A5%87%E0%A4%B2%E0%A4%95%E0%A5%81%E0%A4%A6&page='


ul = []
scraped = []
page_num = 0

while page_num <= 3:

    try:
        res = requests.get(url+str(page_num))

    # Check the url link text file exist or not

        if not os.path.exists('url-link.txt'):

            # Write the url link on url text file
            with open('url-link.txt', 'w') as fp:
                fp.write(f'{url+str(page_num)}\n')

    # <-------------------------------------------->

        else:
            with open('url-link.txt', 'r+') as fp:
                for line in fp:
                    x = line[:-1]
                    ul.append(x)

            # Checked
                if (url+str(page_num)) not in ul:
                    fp.write(f'{url+str(page_num)}\n')

                    with open('data.json', 'w', encoding='utf-8') as fp:
                        for data in res.json()['data']['items']:
                            entry_dict = {
                                'title': data['title'],
                                'author': data['author'],
                                'content': data['content'],
                                'publishDate': data['publishOn']
                            }
                            scraped.append(entry_dict)
                        json.dump(scraped, fp, ensure_ascii=False, indent=4)

                    # print(res.json()['data']['items'])
                    # sleep

                else:
                    print("Process Broked So Scraping Continuing....")

    except requests.ConnectionError:
        print('....Starting')

    page_num += 1
