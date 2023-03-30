class Variable:
    def get_name(self):  # return the name of the variable
        return self.var_name


class Assignment:
    def get_var(self):
        return self.var

    def get_value(self) -> float:
        return float(self.value)

    def set_value(self, f: float):
        self.value = f
        return self.value

    def __repr__(self):
        return str(self.var)+"="+str(self.value)


class Assignments:
    def __getitem__(self, v: Variable) -> float:
        if v in self.sda.keys():
            return self.sda[v]
        else:
            return None

    def __iadd__(self, ass: Assignment):
        self.sda[ass.get_var().get_name()] = ass.get_value()
        return self


class ValueAssignment(Assignment):
    def __init__(self, v:Variable, value:float):
        self.var = v
        self.value = value

    def __repr__(self) :
        return str(self.var)+"="+str(self.value)

    def __eq__(self, other):
        if (self.value == other.value) and (self.var.get_name()==other.var.get_name()):
            return True
        else:
            return False

class SimpleDictionaryAssignments(Assignments):
    def __init__(self):
        self.sda = {}
    # TODO complete all Assignments interface methods


class Expression:
    def evaluate(self, assgms: Assignments) -> float:
        if self.var_name == None:
            return self.value
        else:
            self.value = assgms[self.var_name]
            if self.value == None:
                raise ValueError
            else:
                return self.value

    def derivative(self, v: Variable):
        if self.var_name == None:
            return Constant()
        else:
            if v.get_name() == self.var_name:
                return Constant(1.0)
            else:
                return Constant()

    def __repr__(self) -> str:
        return self.var_name

    def __eq__(self, other):
        if self.var_name == None:
            return (self.value == other.value)
        if (type(other)==Addition) or (type(other)==Power) or (type(other)==Subtraction) or (type(other)==Multiplication):
            return (self.var_name == other.var_name)
        if self.var_name == other.get_name():
            return True
        else:
            return False

    def __add__(self, other):
        return Addition(self, other)

    def __sub__(self, other):
        return Subtraction(self, other)

    def __mul__(self, other):
        return Multiplication(self, other)

    def __pow__(self, power: float, modulo=None):
        return Power(self, power)


class Constant(Expression):

    def __init__(self, value: float = 0.0):
        self.var_name = None
        self.value = value

    def __repr__(self):
        return str(self.value)

    def evaluate(self,a=0):
        return self.value


class VariableExpression(Variable,Expression):
    def __init__(self, variable_name):
        self.var_name = variable_name
        # TODO complete all Variable & Expression interface methods



class Addition(Expression):
    def __init__(self, A: Expression, B: Expression) -> Expression:
        self.A = A
        self.B = B
        self.var_name = (str(self.A)+"+"+str(self.B))


    def evaluate(self, assgms: Assignments) -> float:
        return self.A.evaluate(assgms) + self.B.evaluate(assgms)

    def derivative(self, v: Variable):
        return Addition(self.A.derivative(v), self.B.derivative(v))

    def __repr__(self) -> str:
        return ("("+str(self.A)+"+"+str(self.B)+")")


class Subtraction(Expression):
    def __init__(self, A: Expression, B: Expression) -> Expression:
        self.A = A
        self.B = B
        self.var_name = (str(self.A) + "-" + str(self.B))

    def evaluate(self, assgms: Assignments) -> float:
        return self.A.evaluate(assgms) - self.B.evaluate(assgms)

    def derivative(self, v: Variable):
        return Subtraction(self.A.derivative(v), self.B.derivative(v))

    def __repr__(self) -> str:
        return ("("+str(self.A)+"-"+str(self.B)+")")
    # TODO complete all Expression interface methods


class Multiplication(Expression):
    def __init__(self, A: Expression, B: Expression) -> Expression:
        self.A = A
        self.B = B
        self.var_name = (str(self.A) + "*" + str(self.B))
    def evaluate(self, assgms: Assignments) -> float:
        return self.A.evaluate(assgms) * self.B.evaluate(assgms)

    def derivative(self, v: Variable):
        return Addition((self.A.derivative(v))*self.B, self.A*(self.B.derivative(v)))

    def __repr__(self) -> str:
        return ("("+str(self.A)+"*"+str(self.B)+")")
    # TODO complete all Expression interface methods


class Power(Expression):
    def __init__(self, exp: Expression, p: float) -> Expression:
        self.exp = exp
        self.power = float(p)
        self.var_name = (str(self.exp) + "^" + str(self.power))

    def evaluate(self, assgms: Assignments) -> float:
        return self.exp.evaluate(assgms)**self.power

    def derivative(self, v: Variable):
        return Multiplication(Multiplication(Constant(self.power),Power(self.exp,self.power-1)),self.exp.derivative(v))

    def __repr__(self) -> str:
        return ("("+str(self.exp)+"^"+str(self.power)+")")


class Polynomial(Expression):
    def __init__(self, v: Variable, coefs: list) -> Expression:
        self.var_name = v
        self.lenc = len(coefs)
        self.polly = {0:coefs[0]}
        if self.lenc !=1:
            self.polly[1] = coefs[1]
            for i in range (2,self.lenc):
                self.polly[i] = coefs[i]
        pass


    def evaluate(self, assgms: Assignments) -> float:
        var_value = assgms[self.var_name.get_name()]
        if var_value == None:
            return 0
        sum = self.polly[0]
        for i in range (1,len(self.polly)):
            sum += self.polly[i]*(var_value**i)
        return float(sum)

    def derivative(self, v: Variable):
        if v == self.var_name:
            new_polly = {}
            for i in range (1,self.lenc):
                new_polly[i-1] = self.polly[i]*i
            new_list = []
            for i in range (len(new_polly)):
                new_list.append(new_polly[i])
            return Polynomial(self.var_name,new_list)
        else:
            return Constant(0.0)
    def __repr__(self) -> str:
        rep = "("
        for i in range(self.lenc-1,-1,-1):
            if self.polly[i]!=0:
                if i ==1:
                     if self.polly[i]>0:
                          rep += "+"
                     rep += str(self.polly[i]) + "x"
                elif i == 0:
                     if self.polly[i] > 0:
                          rep += "+"
                     rep +=  str(self.polly[i])
                elif i == self.lenc-1:
                        rep += str(self.polly[i]) + "x^" + str(i)
                else:
                    if self.polly[i] > 0:
                        rep += "+"
                    rep += str(self.polly[i]) + "x^" + str(i)
        rep+=")"
        if rep[1]=="+":
            rep = "(" + rep[2:]
        return rep


    def NR_evaluate(self, assgms:Assignments, epsilon: int = 0.0001, times: int = 100):
        NR_sda = SimpleDictionaryAssignments()
        NR_sda += assgms
        x_n = NR_sda[self.var_name.get_name()]
        if abs(self.evaluate(NR_sda)) <= epsilon:
            return x_n
        for i in range (times):
            new_x_n = self.x_n_1(x_n,NR_sda)
            asa = (ValueAssignment(self.var_name, new_x_n))
            NR_sda += asa
            if abs(self.evaluate(NR_sda)) <= epsilon:
                return new_x_n
            x_n = new_x_n
        raise ValueError

    def x_n_1(self,x_n, NR_sda:Assignments):
        fx = self.evaluate(NR_sda)
        ftagx = self.derivative(self.var_name)
        ff = ftagx.evaluate(NR_sda)
        return x_n-(fx/ff)
