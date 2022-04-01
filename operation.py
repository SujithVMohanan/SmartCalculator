import operator
from getVoice import getMicVoice

# my_string = getMicVoice()
my_string = '1 + 2 x 3 + 10'
print(my_string)
print(my_string.split())
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
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
        'power' : operator.pow
        }[op]

def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return getOperator(oper)(op1, op2)

def getNumber(*args):
    op1 = 0
    args = list(args)
    if 'x' in args:
        indx = args.index('x')
        op1 = args[indx-1]
        oper = args[indx]
        op2 = args[indx+1]
        val = eval_binary_expr(op1,oper,op2)
        args.remove(args[indx - 1])
        args.remove(args[indx - 1])
        args.remove(args[indx - 1])
        print(val)
        op1 = 0
        args.insert(indx-1,val)
        print('After MD '+str(args))


    for ar in range(len(args)):
        if ar % 2 == 0:
            op2 = int(args[ar])
            if ar > 1:
                oper = args[ar-1]
            else:
                oper = '+'
            value = eval_binary_expr(op1,oper,op2)
            op1 = value
    
            print('total '+ str(value))



def callOpr():
    try:
       # print(eval_binary_expr(*(my_string.split())))
       getNumber(*(my_string.split()))
    except Exception as es:
        print(es)
        print("Can't Recognized                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ..")

callOpr()