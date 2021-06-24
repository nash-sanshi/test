#from chardet.metadata import languages
'''
favorite_languages = {
    'jen' : ['python' , 'ruby'],
    'sarch' : ['c'],
    'edwar' : ['ruby' , 'go'],
    'phil' : ['python' , 'haskell'],
    }
'''


from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = ['python' , 'ruby']
favorite_languages['sarch'] = ['c']
favorite_languages['edwar'] = ['ruby' , 'go']
favorite_languages['phil'] = ['python' , 'haskell']

for name,languages in favorite_languages.items():
    print('\n' + name.title() + "'s favorite languages are:")   #\n表示换行
    for languages in languages:
        print('\t' + languages.title())  #\t表示缩进tab