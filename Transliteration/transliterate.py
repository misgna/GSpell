from Geez.alphabet import Fidel

class transliteration:
    
    def __init__(self):
        pass
    
    def transliterate_word(self, word):
        trans = Fidel().trans_g2en()

        trans_output = ""
        for char in word:
            if char in trans:
                trans_output += trans[char]
            else:
                trans_output += char

        return trans_output

    def transliterate_document(self, filepath):
        trans_output = ""
        with open(filepath, encoding = 'utf8') as f:
            for line in f:
                trans_output += transliteration().transliterate_word(line)
        return trans_output

