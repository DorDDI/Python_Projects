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


