


office = {
    
    'Jim' : ['pranks', 'sales', 'basketball'],
    'Dwight' : ['beets', 'sales', 'bears', 'battlestar galactica'],
    'Michael' : ['basketball', 'sales', 'pranks'],
    'Pam' : ['pranks', 'beets', 'art'],
    'Angela': ['accounting', 'beets', 'cats']

    }


# I want to know what activities people share
# How would I do that?

reverse_office = {}

for name, activities in office.items():
    for activity in activities:
        if activity not in reverse_office.keys():
            reverse_office[activity] = [name]
        else:
            reverse_office[activity].append(name)
            
print(reverse_office)
            



