#Is the shop for list
shop = {"Python": 60,
        "Machine Learning": 80,
        "Network Security": 45,
        "English": 25,
        "Calculus I": 35,
        "Big Data": 30,
        "Java": 50}

#Asks for minimum value and max value
minVal = int(input("Give a minumum value: "))
maxVal = int(input("Give a maximum value: "))
selection = []
for i in shop:
    d= shop.get(i,"none")
    if((d > minVal) and (d <maxVal)):
        selection.append(i)

#print the books based in price range
print("Books are:")
for i in selection:
    print(i)

