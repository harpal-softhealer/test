dict_1 = {'a': 2, 'b': 4, 'c': 6}

square_dict = dict(map(lambda val : (val[0],val[1]**2),dict_1.items()))

print(square_dict)