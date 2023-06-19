#for Schleife in Python
a=["eins","zwei","drei","vier","fünf","sechs"]
b=["one","two","three","four","five","six","nope"]

wort=input("Gib ein Wort an:")
j=6
for i in range(0,5):
   if a[i]==wort:
       j=i    
print(b[j])

   
    