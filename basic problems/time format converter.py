def timecoverter(s):
    if s[-2:] == "AM" and s[:2] == "12":
        print("00"+s[2:-2])

    if s[-2:] == "AM":
        print(s[:-2])

    if s[-2:] == "PM" and s[:2] == "12":
        print(s[:-2])
    
    else:
        print((str(int(s[:2])+12))+s[2:-2])

timecoverter("12:10:54PM")