while True:   
    input_a=input("Eingabe Zahl1:")
    try:
        int_a=int(input_a)
        break
    except ValueError:
        print("ungültig")
              
# if int_a == 0:
#     print("Zahl ist Null")
#     print("Gib die Zahl erneut ein:")
#     int_a=int(input("Eingabe Zahl1:"))
    

while True:   
    input_b=input("Eingabe Zahl2:")
    try:
        int_b=int(input_b)
        break
    except ValueError:
        print("ungültig")

# if int_b == 0:
#     print("Zahl ist Null")
#     print("Gib die Zahl erneut ein:")
#     int_a=int(input("Eingabe Zahl1:"))

print(int_a+int_b)
print(abs(int_a-int_b))
print(int_a*int_b)
print(int_a/int_b, "oder", int_b/int_a)
    