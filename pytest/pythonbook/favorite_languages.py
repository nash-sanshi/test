#from chardet.metadata import languages
favorite_languages = {
    'jen' : ['python' , 'ruby'],
    'sarch' : ['c'],
    'edwar' : ['ruby' , 'go'],
    'phil' : ['python' , 'haskell'],
    }
for name,languages in favorite_languages.items():
    print('\n' + name.title() + "'s favorite languages are:")   #\n表示换行
    for languages in languages:
        print('\t' + languages.title())  #\t表示缩进tab