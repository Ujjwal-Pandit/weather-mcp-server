# Task 2 Deliverables - Written Responses

## Deliverable 1: Completed calc.py ✅
**Status**: Completed - All functions implemented including:
- `differentiate` - Differentiation with variable order support
- `integrate_expr` - Indefinite and definite integration
- `solve_equation` - Equation solving over ℝ or ℂ
- `stats_expectation_variance` - Statistical distributions (Uniform, Normal, Bernoulli)

Screenshot taken showing natural language input → calculator tool call → results.

---

## Deliverable 2: Symbolic vs Numeric Output Distinction (4 pts)

The `evaluate` tool distinguishes between symbolic and numeric outputs based on whether the expression contains free variables. This distinction is crucial for several reasons:

### 1. **Preservation of Mathematical Structure**
Symbolic expressions maintain the mathematical structure and relationships between variables. For example, `x**2 + 2*x + 1` preserves the quadratic form, allowing further operations like differentiation, integration, or substitution. If we forced numeric evaluation, we'd lose this structure and couldn't perform symbolic manipulations.

### 2. **Exact vs Approximate Computation**
Numeric evaluation (`evalf()`) produces floating-point approximations, which can introduce rounding errors. Symbolic computation maintains exact mathematical relationships. For instance, `sin(pi/3)` evaluated symbolically remains exact, while numeric evaluation gives an approximation. This is especially important in mathematical proofs and when precision matters.

### 3. **Functionality for Further Operations**
Symbolic expressions can be used as inputs to other tools. For example:
- A symbolic result from `evaluate("x^2 + 1")` can be directly passed to `differentiate()` 
- The symbolic form `x**2 + 2*x + 1` can be integrated, solved, or substituted
- Numeric results like `1.0` cannot be meaningfully differentiated or integrated

### 4. **User Intent and Context**
When a user provides an expression with variables, they likely want to work with the symbolic form, not a numeric value. The distinction respects user intent:
- `evaluate("2 + 3")` → numeric `5` (user wants a calculation)
- `evaluate("x + 1")` → symbolic `x + 1` (user wants to work with the expression)

### 5. **Educational and Mathematical Clarity**
Symbolic output helps users understand mathematical relationships. Seeing `x**2 + 2*x + 1` is more informative than a numeric value when variables are involved, especially for learning and mathematical reasoning.

### Implementation in evaluate():
```python
evaluated = val.evalf() if val.free_symbols == set() else val
```
This checks if there are free symbols (variables) in the expression. If none exist, it evaluates numerically; otherwise, it returns the symbolic form, maintaining mathematical integrity and enabling further symbolic operations.

---

## Deliverable 3: Edge Cases and Error Handling (2 pts)

When using calculator MCP tools, users can encounter various edge cases and errors. Here are the key categories:

### 1. **Input Parsing Errors**
- **Malformed expressions**: Invalid syntax like `"x++"`, `"sin("`, or `"x^"` 
- **Unsupported operations**: Operations not recognized by SymPy
- **Invalid variable names**: Reserved keywords or invalid identifiers
- **Mixed notation**: Mixing `^` and `**` inconsistently

**Handling**: The `_safe_expr()` function converts `^` to `**` and uses `sympify()` with error catching. All tools wrap parsing in try-except blocks.

### 2. **Mathematical Domain Errors**
- **Division by zero**: `"1/0"` or expressions that evaluate to division by zero
- **Undefined operations**: `log(0)`, `sqrt(-1)` over reals, `tan(pi/2)`
- **Complex domain issues**: Requesting real solutions when only complex exist
- **Infinite limits**: Expressions that don't converge

**Handling**: SymPy handles many of these symbolically, but some may raise exceptions that are caught and returned as error messages.

### 3. **Integration and Differentiation Errors**
- **Non-integrable expressions**: Some functions don't have closed-form integrals
- **Infinite bounds**: Definite integrals with infinite limits may not converge
- **Invalid bounds**: Lower bound > upper bound in definite integration
- **Only one bound provided**: Providing `lower` but not `upper` (or vice versa)

**Handling**: The `integrate_expr` function explicitly checks for partial bounds and returns a helpful error. SymPy may return unevaluated integrals or raise exceptions for non-integrable cases.

### 4. **Equation Solving Errors**
- **No solutions**: Equations with no solutions over the specified domain
- **Infinite solutions**: Equations like `0 = 0` or `sin(x) = sin(x)`
- **Transcendental equations**: Some equations can't be solved symbolically
- **Domain mismatch**: Requesting real solutions when only complex exist

**Handling**: `solveset` returns empty sets or condition sets, which are formatted appropriately. The tool handles these cases gracefully.

### 5. **Statistics Tool Errors**
- **Missing parameters**: Not providing required parameters (e.g., `a` and `b` for Uniform)
- **Invalid parameter values**: 
  - Probability `p` outside [0, 1] for Bernoulli
  - Negative standard deviation `sigma` for Normal
  - `a >= b` for Uniform distribution
- **Unknown distribution**: Providing unsupported distribution name

**Handling**: The `stats_expectation_variance` function validates all parameters before creating distributions and returns specific error messages for each case.

### 6. **Type and Format Errors**
- **Wrong parameter types**: Passing strings where numbers expected, or vice versa
- **Invalid order**: Negative or zero order for differentiation
- **Empty inputs**: Empty strings or None values

**Handling**: Type hints help, but runtime validation catches issues. The `differentiate` function explicitly checks `order >= 1`.

### 7. **Performance Issues**
- **Very complex expressions**: Expressions that take too long to evaluate
- **Large symbolic results**: Results that are too large to format or return
- **Recursive or infinite expressions**: Expressions that cause infinite loops

**Handling**: Timeout handling could be added, but currently relies on SymPy's internal limits. Very large results may cause formatting issues.

### 8. **Edge Cases in Specific Operations**
- **Differentiation**: Differentiating constants, or expressions with no dependency on the variable
- **Integration**: Integrating constants, or expressions that simplify to zero
- **Solving**: Solving `x = x` (infinite solutions) or `x = x + 1` (no solutions)

**Handling**: SymPy handles these cases appropriately, returning correct symbolic results (e.g., derivative of constant is 0, integral of 0 is C).

### Error Handling Pattern Used:
All tools follow this pattern:
```python
try:
    # Validate inputs
    # Perform computation
    # Format and return result
except Exception as e:
    return f"Error: [operation] failed. Details: {e}"
```

This ensures that:
- Users always receive a response (never crashes)
- Error messages are informative
- The MCP server remains stable even with invalid inputs
- The AI client can handle errors gracefully and inform users

---

## Deliverable 4: Statistical Tool Implementation ✅
**Status**: Completed - `stats_expectation_variance` tool implemented with support for:
- Uniform distribution (parameters: `a`, `b`)
- Normal distribution (parameters: `mu`, `sigma`)
- Bernoulli distribution (parameter: `p`)

The tool computes both expectation E[X] and variance Var(X) using SymPy's stats module.

