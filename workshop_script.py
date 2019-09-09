# ALT + ENTER
# CTRL + SHIFT + F10
import requests
import bs4

page = requests.get("https://reaktor.pwn.pl/kurs/analityk-danych/")
html = bs4.BeautifulSoup(page.content, 'html.parser')

print(html)
