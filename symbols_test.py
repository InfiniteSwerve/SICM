import pytest
from symbols import Constant, Variable, Add, Sub, Mul, Div


def test_constant_repr():
    c = Constant(5)
    assert repr(c) == "5"


def test_variable_repr():
    v = Variable("x")
    assert repr(v) == "x"


def test_add_repr():
    expr = Add(Constant(3), Variable("x"))
    assert repr(expr) == "(3 + x)"


def test_sub_repr():
    expr = Sub(Variable("x"), Constant(4))
    assert repr(expr) == "(x - 4)"


def test_mul_repr():
    expr = Mul(Constant(2), Variable("y"))
    assert repr(expr) == "(2 y)"


def test_div_repr():
    expr = Div(Variable("z"), Constant(5))
    assert repr(expr) == "(z / 5)"


def test_add_operation():
    expr = Variable("x") + Constant(3)
    assert isinstance(expr, Add)
    assert repr(expr) == "(x + 3)"


def test_sub_operation():
    expr = Variable("x") - Constant(3)
    assert isinstance(expr, Sub)
    assert repr(expr) == "(x - 3)"


def test_mul_operation():
    expr = Variable("x") * Constant(3)
    assert isinstance(expr, Mul)
    assert repr(expr) == "(x 3)"


def test_div_operation():
    expr = Variable("x") / Constant(3)
    assert isinstance(expr, Div)
    assert repr(expr) == "(x / 3)"
