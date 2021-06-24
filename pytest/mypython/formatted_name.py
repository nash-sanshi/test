def formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    print(full_name.title())


formatted_name('chen', 'jie')
formatted_name('wang', 'tian', 'feng')