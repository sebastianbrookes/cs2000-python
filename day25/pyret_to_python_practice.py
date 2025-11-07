"""
Pyret to Python Conversion Practice

Instructions:
- For each problem below, rewrite the given Pyret function in Python.
- Follow the full design recipe: include a docstring, type signature, and at least one pytest test case (in a separate file).
- Once you finish all three, ask your instructor or AI for more!
"""

# Problem 1
# Pyret:
# fun double(x :: Number) -> Number:
#   doc: "returns twice the input"
#   x * 2
# end

# Write the equivalent Python function below:

def double(x: float) -> float:
    """returns twice the input"""
    return 2 * x

# Problem 2
# Pyret:
# fun is-even(n :: Number) -> Boolean:
#   doc: "checks if n is even"
#   n mod 2 == 0
# end

# Write the equivalent Python function below:

def is_even(n: int) -> bool:
    """checks if n is even"""
    return n % 2 == 0

# Problem 3
# Pyret:
# fun greet(name :: String) -> String:
#   doc: "produces Hello, name!"
#   "Hello, " + name + "!"
# end

# Write the equivalent Python function below:

def greet(name: str) -> str:
    """produces Hello, name!"""
    return "Hello, " + name + "!"

# Problem 4
# Pyret:
# fun square(n :: Number) -> Number:
#   doc: "returns the square of n"
#   n * n
# end

# Write the equivalent Python function below:

def square(n: float) -> float:
    """returns the square of n"""
    return n * n

# Problem 5
# Pyret:
# fun starts-with-a(s :: String) -> Boolean:
#   doc: "checks if the string starts with the letter 'a' (case-insensitive)"
#   string-lowercase(s)[0] == "a"
# end

# Write the equivalent Python function below:

def starts_with_a(s: str) -> bool:
    """checks if the string starts with the letter 'a' (case-insensitive)"""
    return s.lower()[:1] == "a"

# When you finish these, ask for more practice problems!

if __name__ == "__main__":
    # Quick manual checks
    print(double(10))
    print(is_even(7))
    print(is_even(10))