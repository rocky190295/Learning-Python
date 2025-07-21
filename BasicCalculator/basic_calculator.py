"""
A beginner-friendly calculator that performs basic arithemetic operations.
Designed to be CLI-usable and GUI ready by keeping core logic modular.
"""
import operator

# Operators Mapping
ops={
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv,
    '%':operator.mod,
    '**':operator.pow
}

# Core calculation logics
def calculate(a:float,b:float,op:str)->float:
    """
    Perform arithemetic operations based on user input
    Parameters:
    a (float): First operand
    b (float): Second operand
    op (str): operator symbol (+,-,*,/,%,**)

    Returns:
    float: Results of the calculations
    """
    if op not in ops:
        raise ValueError(f"Unsupported operator: {op}")
    if op=='/' and b==0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return ops[op](a,b)

def main():
# CLI interface for user input
    """
    Command line interface for user input:
    """
    try:
        a=float(input("Enter first number: "))
        op= input("Enter operator (+, -, *, /, %, **): ").strip()
        b= float(input("Enter the second number: "))

        result=calculate(a,b,op)
        print(f"{a} {op} {b} = {result}")
    
    except ValueError as ve:
        print(f"input error: {ve}")
    
    except ZeroDivisionError as zde:
        print(f"Math Error: {zde}")

# Entry point
if __name__=="__main__":
    main()