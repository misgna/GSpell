from Transliteration.transliterate import transliteration

filepath_allwords = 'outputs/allwords.txt'
filepath_misspelt = 'outputs/misspelt.txt'
trans = transliteration()
tr_allwords = trans.transliterate_document(filepath_allwords)
tr_misspelt = trans.transliterate_document(filepath_misspelt)

#write transliterated files into another document

f_allwords = open('outputs/tr_allwords.txt', 'w', encoding = 'utf8')
f_allwords.write(tr_allwords)
f_allwords.close()

f_misspelt = open('outputs/tr_misspelt.txt', 'w', encoding = 'utf8')
f_misspelt.write(tr_misspelt)
f_misspelt.close()