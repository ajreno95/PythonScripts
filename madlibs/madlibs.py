import re

#Open text file and read it into Text
textFile = open('test.txt')
Text = textFile.read()
findWord = re.compile('ADJECTIVE|NOUN|ADVERB|VERB')

#read through Text and replace each word with user input
for UserInput in findWord.findall(Text):
    replaceString = None
    if UserInput == 'ADJCECTIVE':
        replaceString = input('Enter an {}:\t'.format(UserInput.lower()))
    else:
        replaceString = input('Enter a {}:\t'.format(UserInput.lower()))
    #sub only the first occurance
    Text = re.sub(UserInput, replaceString, Text, 1)

#print out edited Text string and then save that string into output.txt
print(Text)
writeFile = open('output.txt', 'w')
writeFile.write(Text)
