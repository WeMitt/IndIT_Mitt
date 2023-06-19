#Wörterbuch
woerterbuch = {"eins":"one","zwei":"two","drei":"three","vier":"four","fünf":"five","sechs":"six"}
eingabe=input("wort")
for de,en in woerterbuch.items():
    if eingabe==de:
        print(de, ":", en)
              
worterbuch["sieben"]="seven"
