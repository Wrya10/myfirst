#26 set add

a = {1,2,3,4}
print(a)
b = ('s')
#b = {55} this shows an error, since set by its own is mutable!
#in add(), we just allowed to add [an] immutables! (int,tupl,strings)
a.add(b)
print(a)
print(type(b))