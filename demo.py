import requests
import json
import os.path
from time import sleep

url = 'https://bg.annapurnapost.com/api/search?title=%E0%A4%96%E0%A5%87%E0%A4%B2%E0%A4%95%E0%A5%81%E0%A4%A6&page='


ul = []
page_num = 1

while page_num <= 5:

    res = requests.get(url+str(page_num))

    # Check the url link text file exist or not

    if not os.path.exists('url-link.txt'):

        # Write json file for first link or page 1
        with open('data.json', 'w', encoding='utf-8') as fp:
            json.dump(res.json()['data']['items'], fp,
                      ensure_ascii=False, indent=4)

    # Write the url link on url text file
        with open('url-link.txt', 'w') as fp:
            fp.write(f'{url+str(page_num)}\n')

        # Used to test on terminal

        # print(res.json()['data']['items'])
        # sleep(10)

    # If file already exists
    else:

        # Extract url link in order to check new url exist or not
        with open('url-link.txt', 'r+') as fp:

            for line in fp:
                # remove linebreak from a current name
                # linebreak is the last character of each line
                x = line[:-1]

                # add current item to the list
                ul.append(x)

        # Checked
            if (url+str(page_num)) not in ul:
                fp.write(f'{url+str(page_num)}\n')

                with open('data.json', 'r+', encoding='utf-8') as fp:
                    json.dump(res.json()['data']['items'],
                              fp, ensure_ascii=False, indent=4)

                # print(res.json()['data']['items'])
                # sleep

            else:
                print("Process Broked So Scraping Continuing....")

    page_num += 1
