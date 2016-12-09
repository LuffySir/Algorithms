def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """

    len_num2 = len(num2) - 1
    len_num1 = len(num1) - 1
    sum = ''
    if (len_num1 > len_num2):
        flag = 0
        while(len_num2 >= 0):
            n2 = int(num2[len_num2])
            n1 = int(num1[len_num1])
            if(len_num2 == len(num2) - 1):
                if((n1 + n2) < 10):
                    n = n1 + n2
                    flag = 0
                else:
                    n = n1 + n2 - 10
                    flag = 1
                sum = str(n)
            else:
                if((n1 + n2 + flag) < 10):
                    n = n1 + n2 + flag
                    flag = 0
                else:
                    n = n1 + n2 + flag - 10
                    flag = 1
                sum = str(n) + sum
            len_num2 -= 1
            len_num1 -= 1
        while(len_num1 > 0):
            if(int(num1[len_num1]) + flag < 10):
                n = int(num1[len_num1]) + flag
                flag = 0
            else:
                n = int(num1[len_num1]) + flag - 10
                flag = 1
            sum = str(n) + sum
            len_num1 -= 1
        if(len_num1 == 0):
            if(int(num1[len_num1]) + flag < 10):
                n = int(num1[len_num1]) + flag
                sum = str(n) + sum
            else:
                n = int(num1[len_num1]) + flag - 10
                sum = str(n) + sum
                sum = '1' + sum
    elif(len_num1 == len_num2):
        flag = 0
        while(len_num2 > 0):
            n2 = int(num2[len_num2])
            n1 = int(num1[len_num1])
            if(len_num2 == len(num2) - 1):
                if((n1 + n2) < 10):
                    n = n1 + n2
                    flag = 0
                else:
                    n = n1 + n2 - 10
                    flag = 1
            elif((n1 + n2 + flag) < 10):
                n = n1 + n2 + flag
                flag = 0
            else:
                n = n1 + n2 + flag - 10
                flag = 1
            sum = str(n) + sum
            len_num2 -= 1
            len_num1 -= 1
        if(int(num2[len_num2]) + int(num1[len_num1]) + flag < 10):
            n = int(num2[len_num2]) + int(num1[len_num1]) + flag
            sum = str(n) + sum
        else:
            n = int(num2[len_num2]) + int(num1[len_num1]) + flag - 10
            sum = str(n) + sum
            sum = '1' + sum
    else:
        flag = 0
        while(len_num1 >= 0):
            n2 = int(num2[len_num2])
            n1 = int(num1[len_num1])
            if(len_num1 == len(num1) - 1):
                if((n1 + n2) < 10):
                    n = n1 + n2
                    flag = 0
                else:
                    n = n1 + n2 - 10
                    flag = 1
                sum = str(n)
            else:
                if((n1 + n2 + flag) < 10):
                    n = n1 + n2 + flag
                    flag = 0
                else:
                    n = n1 + n2 + flag - 10
                    flag = 1
                sum = str(n) + sum
            len_num2 -= 1
            len_num1 -= 1
        while(len_num2 > 0):
            if(int(num2[len_num2]) + flag < 10):
                n = int(num2[len_num2]) + flag
                flag = 0
            else:
                n = int(num2[len_num2]) + flag - 10
                flag = 1
            sum = str(n) + sum
            len_num2 -= 1
        if(len_num2 == 0):
            if(int(num2[len_num2]) + flag < 10):
                n = int(num2[len_num2]) + flag
                sum = str(n) + sum
            else:
                n = int(num2[len_num2]) + flag - 10
                sum = str(n) + sum
                sum = '1' + sum

    return sum
