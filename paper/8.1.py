import sys

A = ['L', 0, 6]

for entry1 in A:
    try:
        print("The entry is", entry1)
        c = 1 / int(entry1)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry1, "is", c)