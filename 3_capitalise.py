diction = {'apple': 2, 'banana': 4, 'cherry': 6}
capitalize = dict((map(lambda itm: (itm.capitalize(),diction[itm]), diction.keys())))

print(capitalize)
