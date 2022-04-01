import operator
from getVoice import getMicVoice

my_string = getMicVoice()
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

def eval_binary_expr(*args):
    for arg in args:
        print(arg)
    #op1,op2 = int(op1), int(op2)
    # return getOperator(oper)(op1, op2)

def callOpr():
    try:
        print(eval_binary_expr(*(my_string.split())))
    except:
        print("Can't Recognized ..")

callOpr()