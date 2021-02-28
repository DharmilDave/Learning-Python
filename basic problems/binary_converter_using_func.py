n = int(input())
b = bin(n)
count = 0
s = str(b)[2:]
arr = s.split("0")
l = len(max(arr))
print(f"binary : {b} \nstring : {s} \nhackerrank sloution : {l}")