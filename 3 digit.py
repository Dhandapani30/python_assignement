i= int(input("Enter the number: "))
j=0
while(i!=0):
        j+=1
        i//=10

if(j==3):
    print("The given number is 3 digit")
else:
    print("The given number is not 3 digit")
    
