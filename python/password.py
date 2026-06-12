def password(str):
    up = False
    low = False
    digit = False
    special = False

    if(len(str)<8):
        print("password should contains atleast 8 characters") 
        return
    for i in str:
        if i.isupper():
            up = True
        elif i.islower():
            low = True
        elif i.isdigit():
            digit = True
        else:
            special = True # special

    count = 0
    if(up): count += 1
    if(low): count += 1
    if(digit): count += 1
    if(special): count += 1

    match count:
        case 0:
            print("very Weak")
        case 1:
            print("weak")
        case 2:
            print("Decent")
        case 3:
            print("Good")
        case 4:
            print("Strong")

password("$1a@hsjvHbhsj")
