def question1():
    res = "Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are"
    print(res)

def question2():
    a = input("Enter input:")
    number_list = a.split(',')
    number_tuple = tuple(number_list)
    print("List:", number_list)
    print("Tuple:", number_tuple)

def question3():
    a = input("Enter input:")
    index = 0
    for x in a:
        if(x == '.'):
            print(a[index + 1: len(a)])
            break
        index += 1

def question4():
    n = int(input("Enter input:"))
    res = n * n + n - n * 2
    print("Result =", res)

def question5():
    n = int(input("Enter input:"))
    if n >= 10 and n <= 80:
        print("0")
    elif n >= 100 and n <= 200:
        print("1")
    else:
        print("-1")
    
def question6():
    a = input("Enter input:")
    num_upper = 0
    num_lower = 0
    for x in a:
        if x.isupper():
            num_upper += 1
        if x.islower():
            num_lower += 1
    print("Num upper:", num_upper)
    print("Num lower:", num_lower)

# def question7():
    # a = input("Enter input:")
    # a_sub_string = a[1:len(a) - 1]
    # a_sub_string_2 = a_sub_string.replace(',', ' ')
    # a_list = a_sub_string_2.split()
    # res_list = []
    # for x in a_list:
        # if int(x) not in res_list:
            # res_list.append(int(x))
    # print(res_list)

if __name__=="__main__":
    question3()
