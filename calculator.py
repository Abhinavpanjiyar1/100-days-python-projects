def add(n1,n2):
    return n1+n2 

def sub(n1,n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

operation ={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculator():
    num1=int(input("what is your first number?"))
    for symbol in operation:
        print(symbol)
    should_continue=True
    
    while should_continue:     
        operation_symbol= input("pick a symbol for the calculation:")
        num2= int(input("what is your second number?"))
        calculation_function =operation[operation_symbol]
        result= calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2}= {result}")
        if input("type 'yes' to continue calculation{result}, or type 'no' for a fresh start:")=='yes':
            num1= result
        else:
            should_continue=False
            calculator()
            
calculator()