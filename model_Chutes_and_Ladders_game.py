#Model the game Chutes and Ladders
#How many turns does it take to win, on average?
#Roll die - random number between 1-6
#increment counter
#increment player position
#check if position = 100 -- wins
#if position is a special number with a chute or ladder, reassign position
#check if position 100 again -- wins
#loop back to die roll
#if win, record how many turns it took
#repeat the whole game 10,000 times
#what about going over 100?
#compare most recent two results, keep only the lower one to simulate a game
#would shift the distribution to the left and lower the numbers, gets rid of 311
#would also be nice to keep the game progression of each game, go back and investgate a 7 turn win

#1/30/2021

import os
import random
import matplotlib.pyplot as plt
import numpy as np

times_repeat = 100

final_output_filename = "Chutes_and_Ladders_model_" + str(times_repeat) + "x.txt"

def check_for_old_file(filename):
        if os.path.exists(filename):
                os.remove(filename)
                print("Removing old " + filename)
        else:
                print("Creating " + filename)

check_for_old_file(final_output_filename)

with open (final_output_filename, 'a') as final_output:
    final_output.write("Number of turns\n")
    
def check_position(number):
    if number==1:
        return(38)
    elif number==4:
        return(14)
    elif number==9:
        return(31)
    elif number==16:
        return(6)
    elif number==21:
        return(42)
    elif number==28:
        return(84)
    elif number==36:
        return(44)
    elif number==48:
        return(26)
    elif number==49:
        return(11)
    elif number==51:
        return(67)
    elif number==56:
        return(53)
    elif number==62:
        return(19)
    elif number==64:
        return(60)
    elif number==71:
        return(91)
    elif number==80:
        return(100)
    elif number==87:
        return(24)
    elif number==93:
        return(73)
    elif number==95:
        return(75)
    elif number==98:
        return(78)
    else:
        return(number)


player_position = 0
counter = 0
results = []

#start loop here
for i in range(times_repeat):
    
    while player_position!=100:
        dice = random.randint(1,6)
        counter+=1
        #print ("Dice " + str(dice))
        player_position += dice
        #print ("Player " + str(player_position))
        
        if player_position == 100:
            print ("Player wins!")
            
            results.append(counter)     #save number of turns it took
            counter=0                   #reset counters
            player_position=0
            
            #
            break
        
        player_position=check_position(player_position)
        
        if player_position == 100:
            print ("Player wins!")
            
            results.append(counter)     #save number of turns it took
            counter=0                   #reset counters
            player_position=0

            break
        
        if player_position>100:        #can't allow numbers over 100, so just stay put
            player_position-=dice
            #print ("Repeat player " + str(player_position))

print(results)

med=np.median(results)
minimum=np.min(results)
maximum=np.max(results)
mn = np.mean(results)
print("Median " + str(med), "Min " + str(minimum), "Max " + str(maximum) + " Mean " + str(mn))

plt.rcdefaults()
#plt.xkcd()
plt.hist(results, 30) # plotting by columns
plt.xlabel('Number of turns to win')
plt.ylabel('N')
plt.title('Number of turns to win Chutes & Ladders')
plt.show()

with open (final_output_filename, 'a') as final_output:
    final_output.write(str(results))

