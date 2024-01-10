#25 dictionary c

a = {'name':'Wrya' , 'last name':'Javaheri' , 'age':34}
b = {'job' : 'Cisco Developer'}
#dict = dict.fromkeys(a, 'Wrya')

a.update(b)
print(list(a.values()))
print(list(a.keys()))