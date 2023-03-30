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



