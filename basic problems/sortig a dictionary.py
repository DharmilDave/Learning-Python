x = {}
l = [1, 25, 45, 71, 2, 21, 36, 57, 41, 65]
t = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
c = 0

for i in t:
    print(i, c)
    x[i] = l[c]
    c += 1


print(x)
# * to sort the full dictionary by values

sorted_dict = {}
sorted_keys = sorted(x, key=x.get)
for j in sorted_keys:
    sorted_dict[j] = x[j]
print("Sorted dict: ", sorted_dict)

# * to get keys of sorted dictionary
o = [k for k, v in sorted(x.items(), key=lambda item: item[1])]
print(o)

# * to get values of sorted dictionary
o = [v for k, v in sorted(x.items(), key=lambda item: item[1])]
print(o)
