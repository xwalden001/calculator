def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mult(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2


def main():
    flag = 1
    while(flag == 1):
        print("What operation would you like to use?")
        user = input("(a)ddition --- (s)ubtraction --- (m)ultiply --- (d)ivision ---- e(xit): ")

        if user == "a":
            val1 = int(input("value 1: "))
            val2 = int(input("value 2: "))
            result = add(val1,val2)
            print("result equals "+str(result))
        if user == "s":
            val1 = int(input("value 1: "))
            val2 = int(input("value 2: "))
            result = sub(val1,val2)
            print("result equals "+str(result))
        if user == "m":
            val1 = int(input("value 1: "))
            val2 = int(input("value 2: "))
            result = mult(val1,val2)
            print("result equals "+str(result))
        if user == "d":
            val1 = int(input("value 1: "))
            val2 = int(input("value 2: "))
            result = div(val1,val2)
            print("result equals "+str(result))
        if user == "e":
            flag = 0
    
if __name__ == "__main__":
    main()