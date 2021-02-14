def numbinput(numb):
    if(type(numb) not in [int]):
        raise TypeError("Enter positive number")
    elif(numb<1):
        raise ValueError("No negative number")
    return numb 
while(True):
    try:
        numb=int(input("\nHow many times you want to run the program:"))
        if(numb>0):            
            break               
        else:
            print("\nEnter only positive number)
    except:
        print("\nInvalid input")

while(numb):
    char=input("\nEnter character:")
    if(len(char)>1):
        print("\nNOTE")
        print("It checks only first character")
    if(char[0].isalpha()==True):
        print("\nCharacter is Alphabet")
    else:
        print("\nCharacter is not Alphabet")
    numb=numb-1
