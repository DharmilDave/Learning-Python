a = [1,2,3,4,5]
b= ['one','two','three','four']
c= ['x','y','z']
c = list(zip(a,b,c))
d = list(zip(a,b))
p,q = zip(*d) # '*' will unzip the elements
print(c)
print(d)
print(p,q)