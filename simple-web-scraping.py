import requests
import bs4

page = requests.get("https://en.wikipedia.org/wiki/List_of_authors_by_name:_M")
soup = bs4.BeautifulSoup(page.content, features="html.parser")

def findOneBook(name):
    baseUrl = "https://www.goodreads.com" 
    goodreads = requests.get(baseUrl+"/search?utf8=%E2%9C%93&query="+name)
    soup = bs4.BeautifulSoup(goodreads.content)
    findFirstBook = soup.find("a", "bookTitle")['href']
    print(baseUrl+findFirstBook)

names = soup.findAll("a")

for name in names:
    if name.string != None and name.string[0] == "J":
        findOneBook(str(name.string))