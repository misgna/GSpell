import nltk
import json
from Geez.convert2geez import Word2Geez

filename = 'outputs/output.json'
lexicon = {}
def readFile():
    global lexicon
    with open(filename, encoding = 'utf8') as file:
        data = json.load(file)
        for record in data['kalat']:
            lexicon[record['geez']] = record['words']
        
def detectError(word):
    w2g = Word2Geez()
    geez, word = w2g.toGeezWord(word)
    if geez in lexicon:
        lexicon_words = lexicon[geez]
        for words in lexicon_words:
            if word in words:
                return False
    return True

def sortByValue(dictForSort):
    return sorted(dictForSort.items(), key = lambda x:x[1])

def corrector(word):
    readFile()
    if detectError(word) is True:
        w2g = Word2Geez()
        geez, word = w2g.toGeezWord(word)
        measureOfWord = {}
        suggestion = {}
        for key, value in lexicon.items():
            distance = nltk.edit_distance(key, geez)
            measureOfWord[key] = distance
        measureOfWordSorted = sortByValue(measureOfWord)

        top5WordsWithLeastDistance = measureOfWordSorted[0:5]

        print('Spelling suggestion for ' + word)
        print('.............')
        for geezForm in top5WordsWithLeastDistance:
            words = lexicon[geezForm[0]]
            for wrd in words:
                suggestion[wrd[0]] = wrd[1]
        
        secSuggestion = {}
        for key, value in suggestion.items():
            secSuggestion[key] = nltk.edit_distance(word, key)

        sortedSecSuggestion = sortByValue(secSuggestion)

        for secSug in sortedSecSuggestion:
            print(secSug[0], suggestion[secSug[0]])
        
        '''
        #sortedSuggestion = sortByValue(suggestion)
        for key, value in suggestion.items():
            print(key + ' : ' + str(value))
        '''

    else:
        print("word is in correct form")
    