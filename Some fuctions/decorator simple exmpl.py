def fun1(display):
    print("To change or add the functionality in display function")
    return display


@fun1
def display():
    print("display")


display()


# somethings extra
# clousers and decorators

def fun3(the_fun_as_arg):
    def fun2(*args):
        print("To change or add the functionality in disp function")
        return the_fun_as_arg(*args)
    return fun2


@fun3
def disp():
    print("disp")


@fun3
def dis2(s):
    print(s)


dis2("hello")
disp()
