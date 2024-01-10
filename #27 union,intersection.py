#27 union,intersection

a = {23 , 24 , 25 , 26}
b = {25 , 26 , 27 , 28}

print(a.union(b))         # or (a | b)
print(a.intersection(b))  # or (a & b)
print(a.difference(b)) # or (a - b) # shows items in a that are not in b
print(a.symmetric_difference(b)) # or (a ^ b) shows non-intersections of a and b