from Geez.alphabet import Fidel

class Word2Geez:
    def __init__(self):
        pass
    
    def toGeezWord(self, token):
        fidel = Fidel()
        fidels = fidel.alpha()

        gzWord = "" #a word where all letters are transformed to geez form
        word = "" #original word form
        for char in token:
            if (char in fidels) and (char is not ''):
                gzWord += fidels[char]
                word += char
        return gzWord, word

    def toGeezWords(self, tokens):
        geezWords = {}
        tokens = tokens.keys()
        l2g = Word2Geez()

        for token in tokens:
            gzWord, word = l2g.toGeezWord(token)
            if (gzWord in geezWords):
                words = geezWords[gzWord]
                if word not in words:
                    geezWords[gzWord].append(word)
            elif word is not '':
                words = [word]
                geezWords[gzWord] = words
            else:
                pass
        return geezWords