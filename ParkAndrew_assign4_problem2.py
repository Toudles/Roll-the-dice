"""
Assignment #4, Part 2
Andrew Park
"""
import random
sides = int(input("Enter the number of sides on your dice (4, 6, 8, 10, 12, or 20): "))
roll = True
while roll == True:
    if sides == 4:
        print()
        print()
        print("----- Thanks, here we go! -----")
        roll = False
        print()
        print()
        rolls = 1
        total1 = 0
        total2 = 0
        doubles = 0
        twohigh = 0
        twoeven = 0
        twoodd = 0
        hl = 0
        sum = 0
        snake = False
        while snake == False:
            die1 = random.randint(1,4)
            die2 = random.randint(1,4)
            type1 = ""
            #doubles
            if die1 == die2:
                type1 += " Doubles!"
                doubles += 1
            #evens
            if (die1 % 2) == 0 and (die2 % 2) == 0:
                type1 += " Evens!"
                twoeven += 1
            #odds
            if (die1 % 2) != 0 and (die2 % 2) != 0:
                type1 += " Odds!"
                twoodd += 1
            #sum value
            if die1 + die2 == sides:
                type1 += " Sum value is size value!"
                sum += 1
            #high roll
            if die1 == 4 and die2 == 4:
                type1 += " High value!"
                twohigh += 1
            #high/low die1
            if die1 == 4 and die2 == 1:
                type1 += " High / Low!"
                hl += 1
            if die1 == 1 and die2 == 4:
                type1 += " High / Low!"
                hl += 1
            #Snake Eyes
            if die1 == 1 and die2 == 1:
                type1 += " Snake eyes!"
                snake = True
            if die1 != die2:
                print(rolls,".", sep="", end=" ")
                print("die #1 is ", die1, " and die #2 is ", die2, " " + type1, sep="*")
                rolls += 1
                total1 += die1
                total2 += die2
            else:
                print(rolls,".", sep="", end=" ")
                print("die #1 is ", die1, " and die #2 is ", die2, " " + type1, sep="*")
                rolls += 1 
                total1 += die1
                total2 += die2
            if snake == True:
                print()
                print("You finally got snake eyes on roll #", (rolls-1),". Way to go!")
                print()
                print("Along the way you rolled DOUBLES ", doubles, " times." + " (" + format((doubles/(rolls-1))*100,'.2f'), "%", " of all rolls were doubles)", sep="")
                print("Along the way you rolled TWO HIGH VALUES ", hl, " times." + " (" ,format((twohigh/(rolls-1))*100,'.2f'), "%", " of all rolls were two high values)", sep="")
                print("Along the way you rolled TWO EVENS ", twoeven, " times. (" ,format((twoeven/(rolls-1))*100,'.2f'), "%", " of all rolls were two evens)", sep="")
                print("Along the way you rolled TWO ODDS ", twoodd, " times. (" ,format((twoodd/(rolls-1))*100,'.2f'), "%", " of all rolls were two odds)", sep="")
                print("Along the way you rolled HIGH / LOW ", hl, " times. (" ,format((hl/(rolls-1))*100,'.2f'), "%", " of all rolls were high/low)", sep="")
                print("Along the way you rolled A SUM VALUE ", sum, " times. (" ,format((sum/(rolls-1))*100,'.2f'), "%", " of all rolls were a sum value)", sep="")
                print("Average roll for die #1:", format((total1/(rolls-1)), '.2f'))
                print("Average roll for die #2:", format((total2/(rolls-1)), '.2f'))
    elif sides == 6:
        print()
        print()
        print("----- Thanks, here we go! -----")
        roll = False
        print()
        print()
        rolls = 1
        total1 = 0
        total2 = 0
        doubles = 0
        twohigh = 0
        twoeven = 0
        twoodd = 0
        hl = 0
        sum = 0
        snake = False
        while snake == False:
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            type1 = ""
            #doubles
            if die1 == die2:
                type1 += " Doubles!"
                doubles += 1
            #evens
            if (die1 % 2) == 0 and (die2 % 2) == 0:
                type1 += " Evens!"
                twoeven += 1
            #odds
            if (die1 % 2) != 0 and (die2 % 2) != 0:
                type1 += " Odds!"
                twoodd += 1
            #sum value
            if die1 + die2 == sides:
                type1 += " Sum value is size value!"
                sum += 1
            #high roll
            if die1 == 6 and die2 == 6:
                type1 += " High value!"
                twohigh += 1
            #high/low die1
            if die1 == 6 and die2 == 1:
                type1 += " High / Low!"
                hl += 1
            if die1 == 1 and die2 == 6:
                type1 += " High / Low!"
                hl += 1
            #Snake Eyes
            if die1 == 1 and die2 == 1:
                type1 += " Snake eyes!"
                snake = True
            if die1 != die2:
                print(rolls,".", sep="", end=" ")
                print("die #1 is ", die1, " and die #2 is ", die2, " " + type1, sep="*")
                rolls += 1
                total1 += die1
                total2 += die2
            else:
                print(rolls,".", sep="", end=" ")
                print("die #1 is ", die1, " and die #2 is ", die2, " " + type1, sep="*")
                rolls += 1 
                total1 += die1
                total2 += die2
            if snake == True:
                print()
                print("You finally got snake eyes on roll #", (rolls-1),". Way to go!")
                print()
                print("Along the way you rolled DOUBLES ", doubles, " times." + " (" + format((doubles/(rolls-1))*100,'.2f'), "%", " of all rolls were doubles)", sep="")
                print("Along the way you rolled TWO HIGH VALUES ", hl, " times." + " (" ,format((twohigh/(rolls-1))*100,'.2f'), "%", " of all rolls were two high values)", sep="")
                print("Along the way you rolled TWO EVENS ", twoeven, " times. (" ,format((twoeven/(rolls-1))*100,'.2f'), "%", " of all rolls were two evens)", sep="")
                print("Along the way you rolled TWO ODDS ", twoodd, " times. (" ,format((twoodd/(rolls-1))*100,'.2f'), "%", " of all rolls were two odds)", sep="")
                print("Along the way you rolled HIGH / LOW ", hl, " times. (" ,format((hl/(rolls-1))*100,'.2f'), "%", " of all rolls were high/low)", sep="")
                print("Along the way you rolled A SUM VALUE ", sum, " times. (" ,format((sum/(rolls-1))*100,'.2f'), "%", " of all rolls were a sum value)", sep="")
                print("Average roll for die #1:", format((total1/(rolls-1)), '.2f'))
                print("Average roll for die #2:", format((total2/(rolls-1)), '.2f'))
    elif sides == 8:
        print()
        print()
        print("----- Thanks, here we go! -----")
        roll = False
        print()
        print()
        rolls = 1
        total1 = 0
        total2 = 0
        doubles = 0
        twohigh = 0
        twoeven = 0
        twoodd = 0
        hl = 0
        sum = 0
        snake = False
        while snake == False:
            die1 = random.randint(1,8)
            die2 = random.randint(1,8)
            type1 = ""
            #doubles
            if die1 == die2:
                type1 += " Doubles!"
                doubles += 1
            #evens
            if (die1 % 2) == 0 and (die2 % 2) == 0:
                type1 += " Evens!"
                twoeven += 1
            #odds
            if (die1 % 2) != 0 and (die2 % 2) != 0:
                type1 += " Odds!"
                twoodd += 1
            #sum value
            if die1 + die2 == sides:
                type1 += " Sum value is size value!"
                sum += 1
            #high roll
            if die1 == 8 and die2 == 8:
                type1 += " High value!"
                twohigh += 1
            #high/low die1
            if die1 == 8 and die2 == 1:
                type1 += " High / Low!"
                hl += 1
            if die1 == 1 and die2 == 8:
                type1 += " High / Low!"
                hl += 1
            #Snake Eyes
            if die1 == 1 and die2 == 1:
                type1 += " Snake eyes!"
                snake = True
            if die1 != die2:
                print(rolls,".", sep="", end=" ")
                print("die #1 is ", die1, " and die #2 is ", die2, " " + type1, sep="*")
                rolls += 1
                total1 += die1
                total2 += die2
            else:
                print(rolls,".", sep="", end=" ")
                print("die #1 is ", die1, " and die #2 is ", die2, " " + type1, sep="*")
                rolls += 1 
                total1 += die1
                total2 += die2
            if snake == True:
                print()
                print("You finally got snake eyes on roll #", (rolls-1),". Way to go!")
                print()
                print("Along the way you rolled DOUBLES ", doubles, " times." + " (" + format((doubles/(rolls-1))*100,'.2f'), "%", " of all rolls were doubles)", sep="")
                print("Along the way you rolled TWO HIGH VALUES ", hl, " times." + " (" ,format((twohigh/(rolls-1))*100,'.2f'), "%", " of all rolls were two high values)", sep="")
                print("Along the way you rolled TWO EVENS ", twoeven, " times. (" ,format((twoeven/(rolls-1))*100,'.2f'), "%", " of all rolls were two evens)", sep="")
                print("Along the way you rolled TWO ODDS ", twoodd, " times. (" ,format((twoodd/(rolls-1))*100,'.2f'), "%", " of all rolls were two odds)", sep="")
                print("Along the way you rolled HIGH / LOW ", hl, " times. (" ,format((hl/(rolls-1))*100,'.2f'), "%", " of all rolls were high/low)", sep="")
                print("Along the way you rolled A SUM VALUE ", sum, " times. (" ,format((sum/(rolls-1))*100,'.2f'), "%", " of all rolls were a sum value)", sep="")
                print("Average roll for die #1:", format((total1/(rolls-1)), '.2f'))
                print("Average roll for die #2:", format((total2/(rolls-1)), '.2f'))
    elif sides == 10:
        print()
        print()
        print("----- Thanks, here we go! -----")
        roll = False
        print()
        print()
        rolls = 1
        total1 = 0
        total2 = 0
        doubles = 0
        twohigh = 0
        twoeven = 0
        twoodd = 0
        hl = 0
        sum = 0
        snake = False
        while snake == False:
            die1 = random.randint(1,10)
            die2 = random.randint(1,10)
            type1 = ""
            #doubles
            if die1 == die2:
                type1 += " Doubles!"
                doubles += 1
            #evens
            if (die1 % 2) == 0 and (die2 % 2) == 0:
                type1 += " Evens!"
                twoeven += 1
            #odds
            if (die1 % 2) != 0 and (die2 % 2) != 0:
                type1 += " Odds!"
                twoodd += 1
            #sum value
            if die1 + die2 == sides:
                type1 += " Sum value is size value!"
                sum += 1
            #high roll
            if die1 == 10 and die2 == 10:
                type1 += " High value!"
                twohigh += 1
            #high/low die1
            if die1 == 10 and die2 == 1:
                type1 += " High / Low!"
                hl += 1
            if die1 == 1 and die2 == 10:
                type1 += " High / Low!"
                hl += 1
            #Snake Eyes
            if die1 == 1 and die2 == 1:
                type1 += " Snake eyes!"
                snake = True
            if die1 != die2:
                print(rolls,".", sep="", end=" ")
                print("die #1 is ", die1, " and die #2 is ", die2, " " + type1, sep="*")
                rolls += 1
                total1 += die1
                total2 += die2
            else:
                print(rolls,".", sep="", end=" ")
                print("die #1 is ", die1, " and die #2 is ", die2, " " + type1, sep="*")
                rolls += 1 
                total1 += die1
                total2 += die2
            if snake == True:
                print()
                print("You finally got snake eyes on roll #", (rolls-1),". Way to go!")
                print()
                print("Along the way you rolled DOUBLES ", doubles, " times." + " (" + format((doubles/(rolls-1))*100,'.2f'), "%", " of all rolls were doubles)", sep="")
                print("Along the way you rolled TWO HIGH VALUES ", hl, " times." + " (" ,format((twohigh/(rolls-1))*100,'.2f'), "%", " of all rolls were two high values)", sep="")
                print("Along the way you rolled TWO EVENS ", twoeven, " times. (" ,format((twoeven/(rolls-1))*100,'.2f'), "%", " of all rolls were two evens)", sep="")
                print("Along the way you rolled TWO ODDS ", twoodd, " times. (" ,format((twoodd/(rolls-1))*100,'.2f'), "%", " of all rolls were two odds)", sep="")
                print("Along the way you rolled HIGH / LOW ", hl, " times. (" ,format((hl/(rolls-1))*100,'.2f'), "%", " of all rolls were high/low)", sep="")
                print("Along the way you rolled A SUM VALUE ", sum, " times. (" ,format((sum/(rolls-1))*100,'.2f'), "%", " of all rolls were a sum value)", sep="")
                print("Average roll for die #1:", format((total1/(rolls-1)), '.2f'))
                print("Average roll for die #2:", format((total2/(rolls-1)), '.2f'))
    elif sides == 12:
        print()
        print()
        print("----- Thanks, here we go! -----")
        roll = False
        print()
        print()
        rolls = 1
        total1 = 0
        total2 = 0
        doubles = 0
        twohigh = 0
        twoeven = 0
        twoodd = 0
        hl = 0
        sum = 0
        snake = False
        while snake == False:
            die1 = random.randint(1,12)
            die2 = random.randint(1,12)
            type1 = ""
            #doubles
            if die1 == die2:
                type1 += " Doubles!"
                doubles += 1
            #evens
            if (die1 % 2) == 0 and (die2 % 2) == 0:
                type1 += " Evens!"
                twoeven += 1
            #odds
            if (die1 % 2) != 0 and (die2 % 2) != 0:
                type1 += " Odds!"
                twoodd += 1
            #sum value
            if die1 + die2 == sides:
                type1 += " Sum value is size value!"
                sum += 1
            #high roll
            if die1 == 12 and die2 == 12:
                type1 += " High value!"
                twohigh += 1
            #high/low die1
            if die1 == 12 and die2 == 1:
                type1 += " High / Low!"
                hl += 1
            if die1 == 1 and die2 == 12:
                type1 += " High / Low!"
                hl += 1
            #Snake Eyes
            if die1 == 1 and die2 == 1:
                type1 += " Snake eyes!"
                snake = True
            if die1 != die2:
                print(rolls,".", sep="", end=" ")
                print("die #1 is ", die1, " and die #2 is ", die2, " " + type1, sep="*")
                rolls += 1
                total1 += die1
                total2 += die2
            else:
                print(rolls,".", sep="", end=" ")
                print("die #1 is ", die1, " and die #2 is ", die2, " " + type1, sep="*")
                rolls += 1 
                total1 += die1
                total2 += die2
            if snake == True:
                print()
                print("You finally got snake eyes on roll #", (rolls-1),". Way to go!")
                print()
                print("Along the way you rolled DOUBLES ", doubles, " times." + " (" + format((doubles/(rolls-1))*100,'.2f'), "%", " of all rolls were doubles)", sep="")
                print("Along the way you rolled TWO HIGH VALUES ", hl, " times." + " (" ,format((twohigh/(rolls-1))*100,'.2f'), "%", " of all rolls were two high values)", sep="")
                print("Along the way you rolled TWO EVENS ", twoeven, " times. (" ,format((twoeven/(rolls-1))*100,'.2f'), "%", " of all rolls were two evens)", sep="")
                print("Along the way you rolled TWO ODDS ", twoodd, " times. (" ,format((twoodd/(rolls-1))*100,'.2f'), "%", " of all rolls were two odds)", sep="")
                print("Along the way you rolled HIGH / LOW ", hl, " times. (" ,format((hl/(rolls-1))*100,'.2f'), "%", " of all rolls were high/low)", sep="")
                print("Along the way you rolled A SUM VALUE ", sum, " times. (" ,format((sum/(rolls-1))*100,'.2f'), "%", " of all rolls were a sum value)", sep="")
                print("Average roll for die #1:", format((total1/(rolls-1)), '.2f'))
                print("Average roll for die #2:", format((total2/(rolls-1)), '.2f'))
    elif sides == 20:
        print()
        print()
        print("----- Thanks, here we go! -----")
        roll = False
        print()
        print()
        rolls = 1
        total1 = 0
        total2 = 0
        doubles = 0
        twohigh = 0
        twoeven = 0
        twoodd = 0
        hl = 0
        sum = 0
        snake = False
        while snake == False:
            die1 = random.randint(1,20)
            die2 = random.randint(1,20)
            type1 = ""
            #doubles
            if die1 == die2:
                type1 += " Doubles!"
                doubles += 1
            #evens
            if (die1 % 2) == 0 and (die2 % 2) == 0:
                type1 += " Evens!"
                twoeven += 1
            #odds
            if (die1 % 2) != 0 and (die2 % 2) != 0:
                type1 += " Odds!"
                twoodd += 1
            #sum value
            if die1 + die2 == sides:
                type1 += " Sum value is size value!"
                sum += 1
            #high roll
            if die1 == 20 and die2 == 20:
                type1 += " High value!"
                twohigh += 1
            #high/low die1
            if die1 == 20 and die2 == 1:
                type1 += " High / Low!"
                hl += 1
            if die1 == 1 and die2 == 20:
                type1 += " High / Low!"
                hl += 1
            #Snake Eyes
            if die1 == 1 and die2 == 1:
                type1 += " Snake eyes!"
                snake = True
            if die1 != die2:
                print(rolls,".", sep="", end=" ")
                print("die #1 is ", die1, " and die #2 is ", die2, " " + type1, sep="*")
                rolls += 1
                total1 += die1
                total2 += die2
            else:
                print(rolls,".", sep="", end=" ")
                print("die #1 is ", die1, " and die #2 is ", die2, " " + type1, sep="*")
                rolls += 1 
                total1 += die1
                total2 += die2
            if snake == True:
                print()
                print("You finally got snake eyes on roll #", (rolls-1),". Way to go!")
                print()
                print("Along the way you rolled DOUBLES ", doubles, " times." + " (" + format((doubles/(rolls-1))*100,'.2f'), "%", " of all rolls were doubles)", sep="")
                print("Along the way you rolled TWO HIGH VALUES ", hl, " times." + " (" ,format((twohigh/(rolls-1))*100,'.2f'), "%", " of all rolls were two high values)", sep="")
                print("Along the way you rolled TWO EVENS ", twoeven, " times. (" ,format((twoeven/(rolls-1))*100,'.2f'), "%", " of all rolls were two evens)", sep="")
                print("Along the way you rolled TWO ODDS ", twoodd, " times. (" ,format((twoodd/(rolls-1))*100,'.2f'), "%", " of all rolls were two odds)", sep="")
                print("Along the way you rolled HIGH / LOW ", hl, " times. (" ,format((hl/(rolls-1))*100,'.2f'), "%", " of all rolls were high/low)", sep="")
                print("Along the way you rolled A SUM VALUE ", sum, " times. (" ,format((sum/(rolls-1))*100,'.2f'), "%", " of all rolls were a sum value)", sep="")
                print("Average roll for die #1:", format((total1/(rolls-1)), '.2f'))
                print("Average roll for die #2:", format((total2/(rolls-1)), '.2f'))
    else:
        print("Invalid dice size, try again.")
        print()
        sides = int(input("Enter the number of sides on your dice (4, 6, 8, 10, 12, or 20): "))
        
        