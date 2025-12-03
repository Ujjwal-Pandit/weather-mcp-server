from typing import Any, Optional
from mcp.server.fastmcp import FastMCP
from sympy import sympify, Symbol, Eq, integrate, diff, solveset, S, latex
from sympy.stats import Uniform, Normal, Bernoulli, E, variance

# Initialize MCP server
mcp = FastMCP("calculator")

def _safe_expr(expr: str):
    """
    Parse a math expression safely into a SymPy object.
    Examples:
      "sin(x) + x^2"  -> use ** for power: x**2
      "exp(-x)*cos(x)"
    """
    expr = expr.replace("^", "**")
    return sympify(expr, convert_xor=True)

def _fmt(obj) -> str:
    """Human-friendly string with LaTeX (optional) for clarity."""
    try:
        return f"{str(obj)}\nLaTeX: {latex(obj)}"
    except Exception:
        return str(obj)

@mcp.tool()
async def evaluate(expression: str) -> str:
    """
    Evaluate a numeric/symbolic expression.
    Args:
        expression: e.g., "2+3*4", "sin(pi/3)", "limit(sin(x)/x, x, 0)"
    """
    try:
        val = _safe_expr(expression)
        # Try to evaluate to a number if possible
        evaluated = val.evalf() if val.free_symbols == set() else val
        return f"Result:\n{_fmt(evaluated)}"
    except Exception as e:
        return f"Error: could not evaluate expression. Details: {e}"

@mcp.tool()
async def differentiate(expression: str, variable: str = "x", order: int = 1) -> str:
    """
    Differentiate an expression wrt a variable.
    Args:
        expression: e.g., "sin(x)*exp(x)"
        variable:   e.g., "x"
        order:      e.g., 2 for second derivative
    """
    try:
        if order < 1:
            return f"Error: order must be >= 1, got {order}"

        # TODO: create a SymPy symbol from `variable`
        x = Symbol(variable)

        # TODO: parse `expression` safely to a SymPy object using _safe_expr
        f = _safe_expr(expression)

        # TODO: compute the derivative of given order
        result = diff(f, x, order)

        return f"d^{order}/{variable}^{order} of {expression}:\n{_fmt(result)}"
    except Exception as e:
        return f"Error: differentiation failed. Details: {e}"

@mcp.tool()
async def integrate_expr(expression: str, variable: str = "x",
                         lower: Optional[str] = None,
                         upper: Optional[str] = None) -> str:
    """
    Integrate an expression (indefinite or definite).
    Args:
        expression: e.g., "exp(-x^2)"
        variable:   e.g., "x"
        lower:      e.g., "0" (omit for indefinite)
        upper:      e.g., "1" (omit for indefinite)
    """
    try:
        if (lower is not None and upper is None) or (lower is None and upper is not None):
            return "Error: both lower and upper bounds must be provided for definite integration, or both omitted for indefinite integration."
        
        # TODO: create a SymPy symbol from `variable`
        x = Symbol(variable)

        # TODO: parse `expression` safely to a SymPy object using _safe_expr
        f = _safe_expr(expression)

        # TODO: compute the integral
        if lower is not None and upper is not None:
            # lower_bound = ... using _safe_expr
            lower_bound = _safe_expr(lower)
            # upper_bound = ... using _safe_expr
            upper_bound = _safe_expr(upper)
            # definite_int = ... using integrate(f, (x, lower_bound, upper_bound))
            definite_int = integrate(f, (x, lower_bound, upper_bound))
            return f"∫_{lower}^{upper} {expression} d{variable} =\n{_fmt(definite_int)}"
        else:
            # indefinite_int = ... using integrate(f, x)
            indefinite_int = integrate(f, x)
            return f"∫ {expression} d{variable} =\n{_fmt(indefinite_int)} + C"
    except Exception as e:
        return f"Error: integration failed. Details: {e}"

@mcp.tool()
async def solve_equation(equation: str, variable: str = "x", domain: str = "C") -> str:
    """
    Solve equation(s) for a variable.
    Args:
        equation: e.g., "x^2 - 2 = 0" or "sin(x)=1/2"
        variable: variable to solve for
        domain:   'R' (reals) or 'C' (complex)
    """
    try:
        # TODO: create a SymPy symbol for the variable
        x = Symbol(variable)

        # TODO: handle input string
        # If equation contains "=", split into lhs and rhs
        if "=" in equation:
            # lhs, rhs = using .split()
            parts = equation.split("=", 1)
            lhs = _safe_expr(parts[0].strip())
            rhs = _safe_expr(parts[1].strip())
            # expr = ... using Eq(...)
            expr = Eq(lhs, rhs)
        # Otherwise, treat as "expression = 0" using Eq(...)
        else:
            # expr = ... using Eq(...) with S.Zero
            expr = Eq(_safe_expr(equation), S.Zero)

        # TODO: select domain (S.Reals if domain == "R", else S.Complexes)
        dom = S.Reals if domain == "R" else S.Complexes

        # TODO: solve using solveset
        sol = solveset(expr, x, domain=dom)

        return f"Solutions for {equation} over {domain}:\n{_fmt(sol)}"
    except Exception as e:
        return f"Error: solving failed. Details: {e}"

@mcp.tool()
async def stats_expectation_variance(distribution: str, a: Optional[float] = None, b: Optional[float] = None, 
                                     mu: Optional[float] = None, sigma: Optional[float] = None, 
                                     p: Optional[float] = None) -> str:
    """
    Compute expectation and variance for simple distributions.
    Args:
        distribution: "Uniform", "Normal", or "Bernoulli"
        a: Lower bound for Uniform distribution
        b: Upper bound for Uniform distribution
        mu: Mean for Normal distribution
        sigma: Standard deviation for Normal distribution
        p: Probability of success for Bernoulli distribution
    """
    try:
        if distribution.lower() == "uniform":
            if a is None or b is None:
                return "Error: Uniform distribution requires 'a' (lower) and 'b' (upper) parameters."
            dist = Uniform('X', a, b)
            params = {'a': a, 'b': b}
        elif distribution.lower() == "normal":
            if mu is None or sigma is None:
                return "Error: Normal distribution requires 'mu' (mean) and 'sigma' (std dev) parameters."
            dist = Normal('X', mu, sigma)
            params = {'mu': mu, 'sigma': sigma}
        elif distribution.lower() == "bernoulli":
            if p is None:
                return "Error: Bernoulli distribution requires 'p' (probability) parameter."
            if not 0 <= p <= 1:
                return "Error: Bernoulli probability p must be between 0 and 1."
            dist = Bernoulli('X', p)
            params = {'p': p}
        else:
            return f"Error: Unknown distribution '{distribution}'. Supported: Uniform, Normal, Bernoulli."
        
        exp_val = E(dist)
        var_val = variance(dist)
        
        return f"Distribution: {distribution}\nParameters: {params}\nExpectation E[X] = {_fmt(exp_val)}\nVariance Var(X) = {_fmt(var_val)}"
    except Exception as e:
        return f"Error: statistics computation failed. Details: {e}"

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
