# TODO: simplification
# TODO: evaluation


class Expression:
    def __add__(self, other):
        if isinstance(other, Expression):
            return Add(self, other)
        else:
            return Add(self, Constant(other))

    def __neg__(self):
        return Neg(self)

    def __sub__(self, other):
        if isinstance(other, Expression):
            return Sub(self, other)
        else:
            return Sub(self, Constant(other))

    def __mul__(self, other):
        if isinstance(other, Expression):
            return Mul(self, other)
        else:
            return Mul(self, Constant(other))

    def __truediv__(self, other):
        if isinstance(other, Expression):
            return Div(self, other)
        else:
            return Div(self, Constant(other))

    def to_latex(self):
        raise NotImplementedError("LaTeX representation not implemented for this class")


class Constant(Expression):
    def __init__(self, name):
        self.name = name

    @property
    def variables(self):
        return []

    def __repr__(self):
        return f"{self.name}"

    def diff(self):
        return Constant(0)

    def to_latex(self):
        return f"{self.name}"

    def substitute(self, **kwargs):
        return self


class Variable(Expression):
    def __init__(self, name):
        self.name = name

    @property
    def variables(self):
        return list({self.name})

    def __repr__(self):
        return f"{self.name}"

    def diff(self, var=None):
        if var is None:
            return D(self)
        elif var is self.name:
            return Constant(1)
        else:
            return Constant(0)

    def to_latex(self):
        return f"{self.name}"

    def substitute(self, **kwargs):
        if self.name in kwargs.keys():
            return Variable(kwargs[self.name])
        else:
            return self


class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @property
    def variables(self):
        return list(set(self.left.variables + self.right.variables))

    def __repr__(self):
        return f"({self.left} + {self.right})"

    def diff(self, var=None):
        u, v = self.left, self.right
        return Add(u.diff(var), v.diff(var))

    def to_latex(self):
        return f"({self.left.to_latex()} + {self.right.to_latex()})"

    def substitute(self, **kwargs):
        return Add(self.left.substitute(**kwargs), self.right.substitute(**kwargs))


class Neg(Expression):
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"-({self.expr})"

    def diff(self, var=None):
        return Neg(self.expr.diff(var))


class Sub(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @property
    def variables(self):
        return list(set(self.left.variables + self.right.variables))

    def __repr__(self):
        return f"({self.left} - {self.right})"

    def diff(self, var):
        u, v = self.left, self.right
        return Sub(u.diff(var), v.diff(var))

    def to_latex(self):
        return f"({self.left.to_latex()} - {self.right.to_latex()})"

    def substitute(self, **kwargs):
        return Sub(self.left.substitute(**kwargs), self.right.substitute(**kwargs))


class Mul(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @property
    def variables(self):
        return list(set(self.left.variables + self.right.variables))

    def __repr__(self):
        return f"({self.left} * {self.right})"

    def diff(self, var=None):
        u, v = self.left, self.right
        return Add(Mul(u.diff(var), v), Mul(u, v.diff(var)))

    def to_latex(self):
        return f"({self.left.to_latex()} \\times {self.right.to_latex()})"

    def substitute(self, **kwargs):
        return Mul(self.left.substitute(**kwargs), self.right.substitute(**kwargs))


class Div(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @property
    def variables(self):
        return list(set(self.left.variables + self.right.variables))

    def __repr__(self):
        return f"({self.left} / {self.right})"

    def diff(self, var=None):
        u, v = self.left, self.right
        return Div(Sub(Mul(v, u.diff(var)), Mul(u, v.diff())), Mul(v, v))

    def to_latex(self):
        return f"\\frac{{{self.left.to_latex()}}}{{{self.right.to_latex()}}}"

    def substitute(self, **kwargs):
        return Div(self.left.substitute(**kwargs), self.right.substitute(**kwargs))


# TODO:
class Pow(Expression):
    pass


# TODO:
class Sin(Expression):
    pass


# TODO:
class Cos(Expression):
    pass


class D(Expression):
    def __init__(self, expr, var=None):
        self.expression = expr
        self.var = var

    @property
    def variables(self):
        return self.variables

    def __repr__(self):
        return f"D({self.expression})"

    def diff(self, var):
        return self.expression.diff(var)

    def to_latex(self):
        return f"\\frac{{d}}{{dx}}\\left({self.expression.to_latex()}\\right)"
