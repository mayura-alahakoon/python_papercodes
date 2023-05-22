List = ['a', 0, 2]
for entry in List:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Opps", sys.exc_info()[0],"occurred.")
        print("Next entry")
        print()
print("The reciprocal of", entry, "is", r)