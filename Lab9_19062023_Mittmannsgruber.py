def addition(a,b):
    return a+b

def differenz(a,b):
    return a-b

while True:   
    input_a=input("Eingabe Zahl1:")
    try:
        int_a=int(input_a)
        break
    except ValueError:
        print("ungültig")

while True:   
    input_b=input("Eingabe Zahl2:")
    try:
        int_b=int(input_b)
        break
    except ValueError:
        print("ungültig")
        

print("Summe:", addition(int_a,int_b))
print("Differenz:", differenz(int_a,int_b))