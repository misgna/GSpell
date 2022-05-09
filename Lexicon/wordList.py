filepath = 'outputs/output.txt'

def createTokens():
    allWords = ""
    with open(filepath, encoding = 'utf8') as f:
        for line in f:
            tokens = line.split(':')[1].replace('[(', '').replace(')]', '').replace('(','')
            if '),' in tokens:
                words = tokens.split('),')
                for word in words:
                    w = word.split(', ')
                    allWords += w[0] + '\n'
                    print("Writing from compound entry")
            else:
               allWords  += tokens.split(', ')[0] + '\n'
               print("Writing from one entry")

    return allWords

f = open('outputs/allwords.txt', 'w', encoding = 'utf8')
f.write(createTokens())
f.close()