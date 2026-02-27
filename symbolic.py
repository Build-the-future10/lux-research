import sympy as sp

class SymbolicEngine:
    def differentiate(self, expression, var):
        return sp.diff(expression, var)

    def integrate(self, expression, var):
        return sp.integrate(expression, var)

    def simplify(self, expression):
        return sp.simplify(expression)
