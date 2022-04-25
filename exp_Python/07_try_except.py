####################
### Exception
print("-"*10,"Exception","-"*10)

try:
    a = 1/0
except Exception as e:
    print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")



####################
### try,except,else,finally Actions
print("\n","-"*10,"try,except,else,finally Actions","-"*10)

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause\n")

divide(2, 1)
divide(2, 0)
