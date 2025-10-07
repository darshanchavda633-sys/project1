name=input("Enter Your name : ")
gender=input("Enter gender : ")
age=int(input("Enter age : "))
print(" ")
product=input("Enter product : ")
pgram= int(input("Enter product gram :"))

currentgoldprice=12207
print("Current gold price (1 gram) :",currentgoldprice)

totalgoldrate=currentgoldprice*pgram

print("-------------------------------------------------------")
print("TOTAL GOLD RATE = ",totalgoldrate)

print(" ")

makingcharge=845

print("Making charge (1 gram) : ",makingcharge)

totalmakingcharge=pgram*makingcharge

print("Total making charge : ",totalmakingcharge)
print("-------------------------------------------------------")
totalamount=totalgoldrate+totalmakingcharge

print("TOTAL AMOUNT : ",totalamount)

discount=0

if (gender=='m' or gender=='M') and age >65:
    if totalamount >=21000 and totalamount <31000:
        discount=(totalamount*20)/100
    elif totalamount >=31000 and totalamount <51000:
        discount=(totalamount*30)/100
    else:
        discount=(totalamount*35)/100
else:
    if totalamount >=21000 and totalamount <31000:
        discount=(totalamount*10)/100
    elif totalamount >=31000 and totalamount <51000:
        discount=(totalamount*20)/100
    else:
        discount=(totalamount*25)/100
if (gender=='f' or gender=='F') and age >65:
    if totalamount >=21000 and totalamount <31000:
        discount=(totalamount*25)/100
    elif totalamount >=31000 and totalamount <51000:
        discount=(totalamount*35)/100
    else:
        discount=(totalamount*40)/100
else:
    if totalamount >=21000 and totalamount <31000:
        discount=(totalamount*15)/100
    elif totalamount >=31000 and totalamount <51000:
        discount=(totalamount*25)/100
    else:
        discount=(totalamount*30)/100
    
    print("Discount = ",discount)

    netamount=totalamount-discount

    print("---------------------------------------------------------")
    print("Total net amount = ",netamount)

