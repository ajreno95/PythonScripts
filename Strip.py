import re

def StringStrip(PassedString, **kwargs):
    ReturnString = ''
    if 'arg' in kwargs: 
        StringArgs = re.compile(kwargs['arg'])
        ReturnString = StringArgs.sub('',PassedString)
        return ReturnString
    else:
        NoArgs = re.compile(r'\S+')
        for string in(NoArgs.findall(PassedString)):
            ReturnString += string
        return ReturnString
   
      


StringStrip('Alexander Reno test test Alexander Reno is testing this test', arg='test')
StringStrip('test2')
