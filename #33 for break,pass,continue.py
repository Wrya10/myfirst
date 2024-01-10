#33 for  break,pass,continue

numbers = [11,22,33,44,55,66]

for num in numbers:
    if num % 4 ==0:
        print(f'At least one of the numbers provided in the list is divided by 4 !\n Here it is: {num}')
        break
    
else:
    print('None of the provided list is divided by 4 !')