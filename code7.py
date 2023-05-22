total = 0
count = 0
while True:
    inp = input("Enter a number: ")
    if inp == "done" : break
    value = float(inp)
    tot = tot + value
    count = count + 1
average = tot / count
print("Average", average)