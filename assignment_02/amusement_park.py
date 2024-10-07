def printfee(fee):
    print(f"the admission fee is ${fee}")

age = int(input("enter your age:"))

if age < 4:
    printfee(0)
elif age < 18:
    printfee(25)

elif age > 100:
    printfee("0 and you get a free beer!")

elif age > 60:
    printfee(35)

#
#elif age > 100:
#    printfee("0 and you get a free beer!")
#

else:
    printfee(40)
