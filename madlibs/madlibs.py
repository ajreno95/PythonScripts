import re, sys

textFile = open('test.txt')
Text = textFile.read()
findWord = re.compile('ADJECTIVE|NOUN|ADVERB|VERB')
for UserInput in findWord.findall(Text):
    replaceString = ''
    if UserInput == 'ADJCECTIVE':
        replaceString = input('Enter an {}:\t'.format(UserInput.lower()))
    else:
        replaceString = input('Enter a {}:\t'.format(UserInput.lower()))
    Text = re.sub(UserInput, replaceString, Text, 1)
print(Text)
writeFile = open('output.txt', 'w')
writeFile.write(Text)
