original = {'c1': 'Red', 'c2': 'Green', 'c3': None}
new = {key: value for key, value in original.items() if value is not None}
print(new)