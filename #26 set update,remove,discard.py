#26 set update
a = {1,2,3,4}
print(a)
b = {7}
#b = {55} this doesn't show any errors!
#in update(), we allowed to add anything! [(tupl,list,dict) of things!]
a.update([0],[5,6,7,'a'])
a.discard(11) #for discarding without errors.
a.remove(2)   #for removing, if not existed show me an error!
print(a)
print(type(b))
