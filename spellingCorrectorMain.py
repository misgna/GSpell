
import sys
from Scraper.BibleScraper import KJVAmScraper
from Scraper.ReporterScraper import etReporter
from Lexicon.LexiconBuilder import LexiBuilder
from Geez.convert2geez import Word2Geez
import json

#Lexicon
lexicon = {}
#Data From The Holy Bible
#scraper = KJVAmScraper("am")
#scraper.path2text()
#scraper.readText()
#text = scraper.scrapedText()

#Data from GitHub
f_amharic = open('E:/Research/SpellingCorrector/dataset/amharic.txt', 'r', encoding = 'utf8')
f_new_am = open('E:/Research/SpellingCorrector/dataset/new-am.txt', 'r', encoding = 'utf8')
f_training = open('E:/Research/SpellingCorrector/dataset/training.txt', 'r', encoding = 'utf8')

text = f_amharic.read() + ' ' + f_new_am.read() + ' ' + f_training.read()


#Data from the Ethiopian Reporter
reporter = etReporter()
reporter.readFile()
content = reporter.reporterContent()

#Data from the Ethiopian Reporter (article)
articles = ''
article = etReporter()
article.readFileArticle()
articles = article.reporterContent()

#Data integration
text += ' ' + content + ' ' + articles

#Lexicon Builder
lexicalBuilder = LexiBuilder(text)
lexicalBuilder.tokenize()
tokens = lexicalBuilder.listTokens()

#print(tokens)

#TextToGeezConverter
l2g = Word2Geez()
#geez = l2g.toGeezWords(tokens)

#print(geez)
#sorted_tokens = sorted(tokens.items(), key = lambda x:x[1])
for key, value in tokens.items():
        if key is not '':
                geez, word = l2g.toGeezWord(key)
                if geez not in lexicon:
                        lexicon[geez] = [(key, value)]
                else:
                        pair = (key, value)
                        lexicon[geez].append(pair)

#print(lexicon)
#file = open('output.txt', 'w', encoding = 'utf8')
data = {}
data['kalat'] = []
for key, value in lexicon.items():
        data['kalat'].append({
                'geez' : key,
                'words' : value
        })
        #file.write(key + ' : ' + str(value) + '\n')
#file.close()
with open('allwords.json', 'w', encoding = "utf8") as output:
        json.dump(data, output, ensure_ascii= False)
