counts = dict()
names = ['csev', 'cwen', 'csev', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name]
print(counts)