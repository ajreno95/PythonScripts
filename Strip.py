import re

def StringStrip(PassedString, *args):
    ReturnString = ''
    if(args == ()):
        NoArgs = re.compile(r'\S+')
        for string in(NoArgs.findall(PassedString)):
            ReturnString += string
        return ReturnString
    else:
        print(PassedString)
        StringArgs = re.compile(args[0])
        test = StringArgs.sub('',PassedString)
        return ReturnString
      


StringStrip('Alexander Reno test test Alexander Reno is testing this test', 'test')
StringStrip('test2')
