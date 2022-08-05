msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

equation = True


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


result = 0

while equation:
    x = 0
    y = 0
    oper = ''
    operator_check = True
    xy_check = True

    while operator_check and xy_check:
        calc = input(msg_0 + '\n')

        calc_list = calc.split(" ")

        oper = calc_list[1]

        while xy_check:

            if (isfloat(calc_list[0]) or isint(calc_list[0])) and (isfloat(calc_list[2]) or isint(calc_list[2])):
                x = float(calc_list[0])
                y = float(calc_list[2])
                if operator_check:
                    if oper == "+":
                        result = x + y
                        print(result)
                        equation = False
                        operator_check = False
                        xy_check = False
                        break
                    elif oper == "-":
                        result = x - y
                        print(result)
                        operator_check = False
                        xy_check = False
                        equation = False
                        break
                    elif oper == "*":
                        result = x * y
                        print(result)
                        operator_check = False
                        xy_check = False
                        equation = False
                        break
                    elif oper == "/":
                        if (y == 0) or (y == 0.0):
                            print(msg_3)
                            operator_check = False
                            xy_check = False
                            break
                        result = x / y
                        print(result)
                        operator_check = False
                        xy_check = False
                        equation = False
                        break
                    else:
                        operator_check = False
                        xy_check = False
                        print(msg_2)
                        break
            else:
                print(msg_1)
                xy_check = False
                break