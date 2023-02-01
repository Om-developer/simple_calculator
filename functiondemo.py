def AddNumber():
    print ("\nAddtion Program\n")
    a = int(input("EnterFirst Number"))
    b = int(input("Enter Second Number"))
    print ("Addtion of {}and {} is {}". format (a, b, a+b))
def Multiplifun():
    print("\nMultiplication Program\n")
    a = int(input("EnterFirst Number"))
    b = int(input("Enter Second Number"))
    print("Multiplication of {}and {} is {}". format (a, b, a*b))
def Divifunc():
    print("\nDivision Program\n")
    a = int(input("EnterFirst Number"))
    b = int(input("Enter Second Number"))
    print("Division of {}and {} is {}".format(a, b, a / b))
def Subfunc():
    print("\nSubtraction Program\n")
    a = int(input("EnterFirst Number"))
    b = int(input("Enter Second Number"))
    print("Sutraction of {}and {} is {}".format(a, b, a - b))
# def Perfunc():
#     print("\nPercentage Program\n")
#     a = int(input("EnterFirst Number"))
#     b = int(input("Enter Second Number"))
#     print("Percentage of {}and {} is {}".format(a, b, a % b))

print("\n Program Starts Here\n")
print("1 .For Addition")
print("2.For Multiplication")
print("3. For Division")
print("4.For Subtraction")
# print("5 .For Percentage")
num = int(input("select option"))
if num == 1:
    # calling the Addnumber() function from the top
    AddNumber()
elif num == 2 :
# calling the Multifun() function from the top
    Multiplifun()
elif num == 3:
# calling the Divifunc() function from the top
    Divifunc()
elif num == 4:
#calling the Subfunc() function from the top
    Subfunc()
# elif num == 5:
# calling the Perfunc() function from the top
    Perfunc()
else:
    print("please enter correct number")
    print("\n end program \n")




