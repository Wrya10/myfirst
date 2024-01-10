#25 Nested Dictionary

nested_dict = {'dictA' : {'name':'Ali' , 'lname' : 'samadi'},
               'dictB' : {'name' : 'wrya', 'lname' : 'Javaheri'}}

#print(nested_dict['dictB']['name'])

nested_dict['dictC'] = {'name':'Omar', 'lname':'Javaheri'}
nested_dict['dictC']['age'] = 24
print(nested_dict['dictC']['lname'])
del nested_dict['dictA']['name']
print(nested_dict['dictA'])