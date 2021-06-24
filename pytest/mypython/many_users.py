users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einsten',
        'location' : 'princeton',
        },    
    'mcurie' : {
        'first' : 'maria',
        'last' : 'curie',
        'location' : 'paries',
        },
    }
for key,value in users.items():
    print("\nUsername:" + key)
    full_name = value['first'] + ' ' + value['last']
    location = value['location']

# for username,user_info in users.items():
#     print("\nUsername:" + username)
#     full_name = user_info['first'] + ' ' + user_info['last']
#     location = user_info['location']
    
    print(full_name.title())
    print(location.title())