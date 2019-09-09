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
print(len(terms))
print(editions)
print(len(editions))

for index, term in enumerate(terms):
    terms[index] = str(terms[index]).replace('<div class="column small-12 large-5">', '').replace(' </div>', '')
    editions[index] = str(editions[index]).replace('<div class="column small-12 large-3 text-center">','')\
        .replace('</div>','')
print(terms)
print(editions)

file = open("kursy_reaktor.txt", "w")
file.write("KURS ANALITYK DANYCH\n\n")

for index, term in enumerate(terms):
    file.write(str(terms[index])+'\n')
    file.write(str(editions[index])+'\n')
    file.write((40*"-")+'\n')
file.close()

# hint -> input() zwaraca typ napisowy string
user_data = input("podaj dane: ")
print(user_data)


