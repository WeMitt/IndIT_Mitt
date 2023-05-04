int_a=int(input("Eingabe Zahl1:"))
if int_a == 0:
    while int_a==0:
        print("Die Zahl ist Null!")
        int_a=int(input("Gib die Zahl erneut ein:"))
   
int_b=int(input("Eingabe Zahl2:"))
if int_b == 0:
    while int_b==0:   
        print("Die Zahl ist Null!")
        int_b=int(input("Gib die Zahl erneut ein:"))

print(int_a+int_b)
print(abs(int_a-int_b))
print(int_a*int_b)
print(int_a/int_b, "oder", int_b/int_a)