# Assignment operators: =, +=, -=
price=float(input("Enter Product Price"))
discount=price*0.10
disPrice=price-discount
print(f"Price: {price} \nDiscount: {discount} \nDiscountedPrice:{disPrice}")





#Logical operators: and, or, not.

mathMarks=int(input("Enter marks obtained in Maths: "))
phyMarks=int(input("Enter marks obtained in Physics: "))
chemMarks=int(input("Enter marks obtained in Chemistry: "))


if ((mathMarks>=50) and (phyMarks>=55) and (chemMarks>=60)):
    print("You are eligible to sit in pre exam of MBBS")
else:
    print("You have not got the required marks")

idProof=input("Enter Id proof you have")
if((idProof=="passport") or (idProof=="dl") or (idProof=="voter id")):
    print(f"Valid Id {idProof} we accept here")
else:
    print("Only passport, dl and voter id are accepted as Identity Proof")
    print(f"{idProof}:is not valid ID here")


mathMarks=int(input("Enter marks obtained in Maths: \t"))
gapYear=int(input("Enter year gap if any otherwise zero: \t"))
if((mathMarks<=55) or (gapYear != 0)):
    print("Not Eligible for BTech")
else:
    print("Eligible for BTech")


name=input("Enter User Name")
if(notname):
    print("Error!!!")
else:
    print("Welcome" ,name)