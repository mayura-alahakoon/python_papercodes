numbers = []

for i in range(12, 25):  
    if i in [13, 17, 23]:
        continue
       
    numbers.append(i)
    
print(numbers)