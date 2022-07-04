import requests
import json

url = 'https://bg.annapurnapost.com/api/search?title=%E0%A4%96%E0%A5%87%E0%A4%B2%E0%A4%95%E0%A5%81%E0%A4%A6&page='

page_num = 1
scraped = []
try:
    while page_num <= 5:
        res = requests.get(url+str(page_num))
        page_num += 1
        for json_data in res.json()['data']['items']:
            entry_data = {'title': json_data['title'], 'author': json_data['author'],
                          'content': json_data['content'], 'publish': json_data['publishOn']}
            # print(json_data['title'])
            # print(json_data['author'])
            # print(json_data['content'])
            # print(json_data['publishOn'])
            scraped.append(entry_data)

except:
    pass

# print(scraped)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(scraped, f, ensure_ascii=False, indent=4)
