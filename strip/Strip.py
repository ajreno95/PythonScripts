import re

def StringStrip(PassedString, **kwargs):
    ReturnString = ''
    if 'arg' in kwargs: 
        StringArgs = re.compile(kwargs['arg'])
        ReturnString = StringArgs.sub('',PassedString)
        return ReturnString
    else:
        NoArgs = re.compile(r'\s+')
        ReturnString = NoArgs.sub('', PassedString)
        return ReturnString
   
      
TestString1 = 'Alexander Reno test test Alexander Reno is testing this test'
TestString2  = '    test    '
test1 = StringStrip(TestString1, arg='test')
test2 = StringStrip(TestString2)
print('before:\t{}'.format(TestString1))
print('strip:\ttest')
print('after:\t{}\n'.format(test1))
print('before: {}'.format(TestString2))
print('after:\t{}'.format(test2))
