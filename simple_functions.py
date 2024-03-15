# Custom python functions

def double_number(a):
    """double_number gives the double of that given number"""
    print(f'value before double_number(): {a}')
    a+=a
    print(f'value before double_number(): {a}')
    return (a)

def square_number(a):
    """square_number gives the square of that given number"""
    print(f'value before square_number(): {a}')
    a*=a
    print(f'value before square_number(): {a}')
    return (a)
