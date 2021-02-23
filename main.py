import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}

url = 'https://store.steampowered.com/search/?filter=topsellers'
respon = requests.get(url, headers)
soup = BeautifulSoup(respon.text, "html.parser")
top_sellers = soup.findAll('div', attrs={'class':'search_results'})

for top_seller in top_sellers:
    title = top_seller.findAll('span', attrs={'class':'title'})
    count = 0
    for titles in title:
        count += 1
        filter = titles.text
        print(f"{count}.{filter}")
    pic = top_seller.findAll('div', attrs={'class':'col search_capsule'})
    for pics in pic:
        count += 1
        filter = pics.find('img')
        print(f"{count}.{filter}")
    date = top_seller.findAll('div', attrs={'class':'col search_released responsive_secondrow'})
    for dates in date:
        count += 1
        filter = dates.text
        filters = ""
        if filter == "":
            filters = "Empty date"
        print(f"{count}.{filters}{filter}")
