import sympy as s, sys
x = s.Symbol('x')
y, i, n, a, b, f, g = s.symbols('y i n a b f g')
print("\n"+"#"*32)
print("#Welcome to the Limit-Algorithm#")
print("#"*32+"\n[+] Enter help for options")
try:
    while True:
        LA = input("\n[+] Limit-Algorithm > ")
        if LA == 'help' or LA == 'Help':
            print("""
    [+] ** To raise the forces
    [+] *for multiplication
    [+] +,- The process of addition and subtraction
    [+] / for the division process
    [+] s.sin(x) Trigonometric ratios You can replace sin with a non-ratio
    [+] Enter C to add the compensation value and also to change the compensation value
    [+] Enter EQ to add the equation and also to change the equation
    [+] Enter FL to perform the equation
    [+] Enter Exit To Exit
    """)
        if LA == 'C' or LA == 'c':
            try:
                print("\n[+] Enter numerical values only")
                c = int(input("[+] Enter the compensation value > "))
            except:
                print("\n[+] Enter numerical values only mf")
                c = int(input("[+] Enter the compensation value > "))
        if LA == 'EQ' or LA == 'eq':
            try:
                eq = input("[+] Enter the equation > ")
            except:
                print("\n[+] Enter a valid equation mf")
                eq = input("[+] Enter the equation > ")
        if LA == 'FL' or LA == 'fl':
            try:
                r = (s.limit(eq, x, c))
                print(f"\n[+] Result {r}")
            except:
                print("[+] There is an error in the value or equation you entered, re-enter the compensation value by entering C and enter the equation by entering EQ")
        if LA == 'exit' or LA == 'Exit':
            sys.exit()
except:
    sys.exit()
