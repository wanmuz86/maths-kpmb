scores = [30,10,20,70];
print(scores)

#retrieve the first item from the lists
#the first item in the list start with index 0
print(scores[0])

# Untuk setiap isi/item di dalam list,
# Tunjukkan item tersebut
for i in scores:
	print(i)

# Append untuk tambah di hujung dan di dlama list
scores.append(80)
print(scores)

# Tambah di posisi 1 , nombor 100
scores.insert(1,100)
print(scores)

# Remove item from the end of the list
scores.pop()
print(scores)

#If you want to remove an item at the specfic
# index, you specify the index to be removed
# inside the parameter

scores.pop(1)
print(scores)