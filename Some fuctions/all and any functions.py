# Without using all and any functions

a = 70
b = 80
c = 90

if a >= 70 and b >= 80 and c >= 90:
    print("All conditions satisfied \nYou passed :)")

if a >= 70 or b <= 50 or c != 100:
    print("Any of the one condition satisfied :|")

# With using  'all' and 'any' functions
# these functions returns bool value

l = [a >= 70, b >= 80, c >= 85]
if all(l):
    print("All statement")

if any(l):
    print("Any statement")

# ! some other examples

x = ["1", "2", "hello", True]
y = ["", 0, 0.0]
print(any(x))  # ? will print True if any value in the list is true or has any values
print(all(x))  # ? will print True if all of the value in the list are valid or say true
print(any(y))
