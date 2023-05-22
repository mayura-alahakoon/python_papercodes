print("####break");

for i in range(1, 11):
    if i == 5:
        break
    print(i)

print("####continue");


for i in range(1, 11):
    if i == 5:
        continue
    print(i)


print("####pass");

for i in range(1, 11):
    if i == 5:
        pass
    print(i)



print("####continue");

for i in range(1, 10):
  if i % 2 == 0:
    continue
  print(i)
