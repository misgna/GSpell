import os
from bs4 import BeautifulSoup


class KJVAmScraper:
    text = ""
    paths = []

    def __init__(self, filename):
        self.filename = filename

    def path2text(self):
        books = [book for book in os.listdir(self.filename) if book.isdigit()]
        for book in books:
            book = 'am/'+ book
            chapters = [chapter for chapter in os.listdir(book)]
            for chapter in chapters:
                path = book + "/" + chapter
                self.paths.append(path)
    

    def readText(self):
        textContent = ""
        for path in self.paths:
            file = open(path, 'r', encoding = "utf8") 
            pageContent = file.read()
            page2soup = BeautifulSoup(pageContent)
            textContent += page2soup.get_text()

        self.text = textContent
    
    def scrapedText(self):
        return self.text
