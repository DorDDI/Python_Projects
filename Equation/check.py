import importlib
import os
from itertools import tee, islice, chain

def get_also_next_value_in_iterable(some_iterable):
    prevs, items = tee(some_iterable, 2)
    nexts = chain(islice(items, 1, None), [None])
    return zip(prevs, nexts)

# params:

I = ['const1', 'const2', 'const3', 'add1', 'add2', 'add3', 'add4', 'sub1', 'sub2', 'sub3', 'sub4', 'mul1', 'mul2', 'mul3', 'mul4', 'pow1', 'pow2', 'pow3', 'pow4',
     'pol1', 'pol2', 'pol3', 'pol4', 'comp1', 'comp2']

######################################################################################################
######################################################################################################
flag = True
File = ""
while flag:
    print("Please enter a file name:")
    File = input()
    if not (File.isdigit()):
        print("File name is invalid! The file name should be your identity number")
        exit(0)
    else:
        flag = False

# check for allowed libraries
lib = []
try:
    f = open(File+".py")
    for row in f:
        for now_word, next_word in get_also_next_value_in_iterable(row.split()):
            if now_word == "import":
                lib.append(next_word)
    if len(lib) > 0:
        print("No modules allowed to be used!")
        exit(0)
except:
    print("file dosn't exist. add it to the test folder")
    exit(0)

######################################################################################################
######################################################################################################


## import the py file:
Module = importlib.import_module(File)
score = 0

try:
    x = Module.VariableExpression("x")
    y = Module.VariableExpression("y")
    z = Module.VariableExpression("z")
    ass1 = Module.ValueAssignment(x, 10)
    ass2 = Module.ValueAssignment(y, 20)
    sda = Module.SimpleDictionaryAssignments()
    sda += ass1
    sda += ass2
except:
    print("pre definitions failed, can't test the others")

for t_name in I:
    ### --- const 1 ---- ###
    if t_name == "const1":
        try:
            con0 = Module.Constant(0.0)
            if str(con0) ==  "0.0":
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "const2":
        try:
            con0 = Module.Constant(0.0)
            if str(con0.evaluate(sda)) ==  "0.0":
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "const3":
        try:
            con0 = Module.Constant(0.0)
            d = con0.derivative(x)
            if str(d) == "0.0":
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    ################################################
    elif t_name == "add1":
        try:
            add = x + y
            if str(add) == "(x+y)":
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "add2":
        try:
            add = x + y
            if add.evaluate(sda) == 30:
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "add2":
        try:
            add = x + y
            if str(add.derivative(x)) == "(1.0+0.0)":
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "add3":
        try:
            add = x + y
            if str(add.derivative(y)) == "(0.0+1.0)":
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "add4":
        try:
            add = x + y
            if add.derivative(x).evaluate(sda) == 1.0:
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    ################################################
    elif t_name == "sub1":
        try:
            sub = x - y
            if str(sub) == "(x-y)":
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "sub2":
        try:
            sub = x - y
            if sub.evaluate(sda) == -10:
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "sub3":
        try:
            sub = x - y
            if str(sub.derivative(x)) == "(1.0-0.0)":
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "sub4":
        try:
            add = x + y
            sub = x - y
            if add != sub:
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    ################################################
    elif t_name == "mul1":
        try:
            mul = x * y
            if str(mul) == "(x*y)":
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "mul2":
        try:
            mul = x * y
            if mul.evaluate(sda) == 200:
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "mul3":
        try:
            mul = x * y
            if str(mul.derivative(x)) == "((1.0*y)+(x*0.0))":
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "mul4":
        try:
            mul2 = z * y
            mul2.evaluate(sda)
            print("test " + t_name + " failed")
        except:
            score += 1
            print("test " + t_name + " success")
    ################################################
    elif t_name == "pow1":
        try:
            add = x + y
            pow = add ** 3
            if str(pow) == "((x+y)^3.0)":
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "pow2":
        try:
            add = x + y
            pow = add ** 3
            if pow.evaluate(sda) == 27000:
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "pow3":
        try:
            add = x + y
            pow = add ** 3
            if str(pow.derivative(x)) == "((3.0*((x+y)^2.0))*(1.0+0.0))":
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "pow4":
        try:
            add = x + y
            pow = add ** 3
            if pow.derivative(x).evaluate(sda) == 2700.0:
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    ################################################
    elif t_name == "pol1":
        try:
            pol = Module.Polynomial(x, [12,-8,-1])
            if str(pol) == "(-1x^2-8x+12)":
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "pol2":
        try:
            pol = Module.Polynomial(x, [0, 0, -1])
            if str(pol) == "(-1x^2)":
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "pol3":
        try:
            pol = Module.Polynomial(x, [12, 8, 1])
            if str(pol.derivative(x)) == "(2x+8)":
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "pol4":
        try:
            pol = Module.Polynomial(x, [12, 8, 1])
            root = pol.NR_evaluate(Module.ValueAssignment(x, 0.5), 0.01, 1000)
            sda += Module.ValueAssignment(x, root+0.0)
            if -0.01 <= pol.evaluate(sda) <= 0.01:
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    ################################################
    elif t_name == "comp1":
        try:
            comp = ((x + y) * (y + x)) ** 3.0
            if str(comp) == "(((x+y)*(y+x))^3.0)":
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")
    elif t_name == "comp2":
        try:
            comp = ((x+y)*(y+x))**3.0
            if str(comp.derivative(x)) == "((3.0*(((x+y)*(y+x))^2.0))*(((1.0+0.0)*(y+x))+((x+y)*(0.0+1.0))))":
                score += 1
                print("test " + t_name + " success")
            else:
                print("test " + t_name + " failed")
        except:
            print("test " + t_name + " crashed")

print("Final score: " + str(score/ len(I) * 100))
