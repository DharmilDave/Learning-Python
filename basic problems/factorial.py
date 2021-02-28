def fac_rec(n):
  if n ==1:
    return n
  else:
    return n*fac(n-1)

def fac(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f

print(fac_rec(3))
print(fac(5))