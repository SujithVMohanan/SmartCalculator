import operator
from getVoice import getVoice


def getOperator(op):
    return {
        '+' : operator.add,
        'plus' : operator.add,
        'add' : operator.add,
        '-' : operator.sub,
        'substract' : operator.sub,
        'minus' :  operator.sub,
        'x' : operator.mul,
        'multiple' : operator.mul,
        'divided' :operator.__truediv__,
        'divide' : operator.__truediv__,
        '/' : operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
        'power' : operator.pow
        }[op]

def eval_binary_expr(op1, oper, op2):
    op1,op2 = float(op1), float(op2)
    return getOperator(oper)(op1, op2)

def getNumber(*args):
    global ra
    op1 = 0
    args = list(args)
    indx = 0 
    len_arg = len(args)
    ra = 0
    while ra < len_arg + 1:
        try:
            if args[ra] == 'x' or args[ra] == '/':
                indx = ra
            else:
                ra += 1 
                continue
            op1 = args[indx-1]
            oper = args[indx]
            op2 = args[indx+1]
            val = float(eval_binary_expr(op1,oper,op2))
            args.remove(args[indx - 1])
            args.remove(args[indx - 1])
            args.remove(args[indx - 1])
            op1 = 0
            args.insert(indx-1,str(val))
            ra -= 1
        except Exception as es:
            # print(args)
            print('Special ones completed')
            break
    # print(args)


    for ar in range(len(args)):
        if ar % 2 == 0:
            op2 = float(args[ar])
            if ar > 1:
                oper = args[ar-1]
            else:
                oper = '+'
            value = eval_binary_expr(op1,oper,op2)
            op1 = float(value)
    
    print('total '+ str(value))
    return str(value)



def callOpr(my_st):
    try:
        my_string = getVoice(my_st)
        # my_string = [1, '+', 2, '+', 3, 'x', 6, 'x', 4, 'x', 20]
        print(my_st)
        print(my_string)

        if my_string == "Can't Calculate":
            print("Something happended")
            val = "Can't Calculate please check values uoy given "
        else:
            val = getNumber(*(my_string))
    except Exception as es:
        print(es)
        print("Can't Recognized")
        val = "Can't Recognized"
    return val                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

# callOpr(my_string = getVoice())