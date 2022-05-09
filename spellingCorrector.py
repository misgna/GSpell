import UI as ui

#ui.corrector('ሰማይ')
#ui.corrector('ክደማ') #ክደይ
#ui.corrector('ጨለማይ') #ጨለማን

#import misspelt data: geez
filepath = 'outputs/misspelt.txt'

result = 'outputs/tr_result.txt'
tr_result = ""
with open(filepath, encoding = "utf8") as f:
    for line in f:
        words = line.split(' : ')
        tr_result += str(ui.corrector(words[0])) + '\n'

f_result = open(result, 'w', encoding = "utf8")
f_result.write(tr_result)
f_result.close()
