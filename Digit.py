def square_digits(num):

    num_list=[]
    square_list=[]
    for x in (str(num)):
        num_list.append(x)
    # ints=[eval(i) for i in num_list]
    ints=list(map(int, num_list))
    for i in ints:
       square_list.append(pow(i,2))

    s=[str(i) for i in square_list]
    return int("".join(s))
            

print(square_digits(9119))