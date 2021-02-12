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
    judul = top_seller.findAll('span', attrs={'class':'title'})
    count = 0
    for juduls in judul:
        count += 1
        saring = juduls.text
        print(f"{count}.{saring}")
    gambar = top_seller.findAll('div', attrs={'class':'col search_capsule'})
    for gambars in gambar:
        count += 1
        saring = gambars.find('img')
        print(f"{count}.{saring}")
    tanggal = top_seller.findAll('div', attrs={'class':'col search_released responsive_secondrow'})
    for tanggals in tanggal:
        count += 1
        saring = tanggals.text
        saringgan = ""
        if saring == "":
            saringgan = "Tanggal Kosong"
        print(f"{count}.{saringgan}{saring}")