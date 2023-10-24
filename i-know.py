from termcolor import colored
y=2
while y==2:
    a1=colored('****Lets Play the Game find what inside in your brain******','green')
    print(a1)
    print("\n\nYou will going to select any number in your mind and\n I will Say what's the number in remain\n")
    
    print("Say Yes(1)if your are ready to play!")
    x=int(input("\n"))
    if(x==1):
    
        print("\t\nPlease!! choose any number of rupess you want to put in your pocket !!! \n Don't let you know the amount to others!!\n")
        y=int(input("Press,(1) if you done this task\n"))
        if(y==1):
        
            print("Now Borrow the same money from your friends\n And add this money in your pocket\nAnd Again keep it seceret all money you have\n")
            z=int(input("Press,(1) if you done this task\n"))
            if(z==1):
                print("Add following rupees in your pocket  which is given by me to you is:\n")
                import random
                ran=random.randint(1,10000)
                half=ran/2
                print("$:",ran," And add this money in your pocket\nAnd keep it seceret\n")
                a=int(input("Press,(1) if you done this task\n"))
                if(a==1):
                
                    print("\tNow give the half of your money to some charity funds\nMeans,,, whatever money you have!!\nJust Donate half of money you had \n\n")
                    b=int(input("Press,(1) if you done this task\n"))
                    if(b==1):
                        
                        print("\tNow !!! Return the that amount of your money which you have borrow's earlier from your friend\nAnd see in your pocekt!!!you have remain !!!!\n\n\n")
                        c=int(input("Press,(1) if you done this task\n"))
                        if(c==1):
                            print("\n\n\tThe money remain in your pocket is:",half)
    
    y=int(input("\n\nLets Play for another time--press:2\nAnd press:0 for Exits the program\n"))

