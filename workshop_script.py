# ALT + ENTER           - podpowiedź
# CTRL + SHIFT + F10    - uruchomienie
# CTRL + D              - duplikowanie lini kodu
import requests
import bs4

page = requests.get("https://reaktor.pwn.pl/kurs/analityk-danych/")
html = bs4.BeautifulSoup(page.content, 'html.parser')

print(html)
terms = html.findAll(class_ = "column small-12 large-5")
editions = html.findAll(class_ = "column small-12 large-3 text-center")

print(terms)
print(editions)