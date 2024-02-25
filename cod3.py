from logo import art
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2
operations = {
  '+': add,
   "-":subtract,
   "*":multiplication,
   "/":division  
}
def calculator():
    num1 = float(input("what's the first number?:"))
    for operation in operations:
     print(operation)
    should_continue = True
    while should_continue:
        operator = input("pick an operation:")
        num2 = float(input("what's the second number?:"))
        calculation_function = operations[operator]
        first_answer = calculation_function(num1, num2)
        print(f"{num1} {operator} {num2} = {first_answer}")
        if input(f"Type 'y' to continue or 'n' to exit:") == 'y':
            num1 = first_answer
            
        else:
            should_continue = False
calculator()