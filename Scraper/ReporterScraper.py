import json
import os

class etReporter:
    content = ""
    path = 'etReporter'

    def readFile(self):
        files = os.listdir(self.path)
        for file in files:
            newPath = self.path + '/' + file
            with open(newPath, encoding = 'utf8') as data:
                contents = json.load(data)
                for content in contents['news']:
                    self.content += ' ' + content['title'] + ' ' + content['text']

    def readFileArticle(self):
        with open('etReporterArt/reporter.json', encoding = 'utf8') as article:
            contents = json.load(article)
            for content in contents['news']:
                self.content += content['text'] + ' '

    def reporterContent(self):
        return self.content



