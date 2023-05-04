int_a=int(input("Eingabe Zahl1:"))
if int_a == 0:
    print("Zahl ist Null")
    print("Gib die Zahl erneut ein:")
    int_a=int(input("Eingabe Zahl1:"))
    
int_b=int(input("Eingabe Zahl2:"))
if int_b == 0:
    print("Zahl ist Null")
    print("Gib die Zahl erneut ein:")
    int_b=int(input("Eingabe Zahl2:"))

print(int_a+int_b)
print(abs(int_a-int_b))
print(int_a*int_b)
print(int_a/int_b, "oder", int_b/int_a)    