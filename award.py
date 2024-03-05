"""

start

design a program that determines the award one person competing in a triathalon will recieve
Time should be read in Minutes
3 events - swimming, cyclling, running 
calculate and display total time taken to complete triathalon 
award given based on total time taken to complete triathalon
the quallifying time for awards is 100mins
dispaly award participent will recieve based on criteria 
>>>(if else)

stop

"""

# Design a program that determines the award one person competing in a triathalon will recieve
print("\nYour one time passcode is 0000")
print("\nDo not share it with anyone as they will have access to your account.")
name = (input("\nPlease enter your name: "))
password = (input("\nPlease enter your passcode: "))
if password == "0000":
    print("\nWelcome to your personallised award dashboard. Here you can see your awards and events!!")
else:
    print("\nSorry, your password is incorrect. You have been denied access.")
    exit()
print("\nFirst, we need some information on your record breaking times today...")
print("\nIMPORTANT: All speeds will be calculated in minutes. Please provide times as whole numbers")
# Collect all times and calculate the total time
swim = int(input("\nPlease enter your swimming speed: "))
cycle = int(input("Please enter your cycling speed: "))
run = int(input("Please enter your running speed: "))
total_time = (swim + cycle + run)
print ("\nWell done for completing the triathalon. You made it to the end!")
print("\nYou completed the Triathalon in: " + str(total_time) + " minutes")
# Award based on total time taken
if total_time <= 100:
    print(f"\nCONGRATULATIONS {name}!!! You have completed the Triathalon in 100 minutes or less!")
    print("As you have finished among the fastest participents, we are pleased to inform you that you have won!!!")
    print("You have won the Provincial Colours award. The highest honour.")
elif (total_time >= 101) and (total_time <= 105):
    print(f"\nYou're a 2nd place cohort winner {name}! You finished within only 5 minutes of the qualifying time!")
    print("You have won the Provincial Half Colours award.")
elif (total_time >= 106) and (total_time <= 110):
    print(f"\nWell Done {name}! You completed the Triathalon in thrid cohort, within just 1o minutes of the qualifying time!")
    print("You will be awarded the Provincial Scroll for your very hard work.")
else:
    print(f"\nGreat efffort {name}. You were almost there. Unfortunatly you do not get an award.")
print("\nYou will recieve your award in the post to the address provided at registration")
print("Alternativly, please contact us on (+44)0208-593-1498 and provide a different address.")
print("\nThank you for participating in this years Triathalon for Cancer relief. Our charities are all so grateful for the money raised.")
print("We hope to see you next year :)")
print("\nYou will be logged out in 30 seconds. If not, please refresh this page.")