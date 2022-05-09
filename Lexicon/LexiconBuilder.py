from Geez.convert2geez import Word2Geez
from Geez.alphabet import Fidel

class LexiBuilder():
    lexicon = {}
    text = ""

    def __init__(self, text):
        self.text = text
        
    def tokenize(self):
        content = ''
        fidel = Fidel()
        fidels = fidel.alpha()
        for char in self.text:
            if (char in fidels) and (char is not ''):
                content += char
            else:
                content += ' '

        
        tokens = [token for token in content.split(" ") if token is not ""]
        g2w = Word2Geez()
        for token in tokens:
            geez, token = g2w.toGeezWord(token)
            if token in self.lexicon:
                self.lexicon[token] += 1
            else:
                self.lexicon[token] = 1

    def listTokens(self):
        return self.lexicon