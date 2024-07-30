#  #Doc string are the explainer of the function. It is used to explain what the function does.

# def add_bid( ):
#     """This function adds a bid to the bidding dictionary""" #IT ALWAYS AFTER THE FUNCTION DEFINITION JUST LIKE THIS
#     return "Hello"
#calculator 


def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mult(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2

dictionary ={
  "+": add,
  "-": sub,
  "*": mult,
  "/": div
}


def calculator():
  num1 = float(input("What's the first number?: "))
  for symbol in dictionary:
    print(symbol)
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    if operation_symbol =="/":
      num2 = float(input("What's the next number?: "))
      if num2 == 0:
        print("You can't divide by zero")
        continue
    try:
      calculation_function = dictionary[operation_symbol]
    except KeyError:
      print("Invalid operation")
      continue
    answer = calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()  # recursion in the function 


