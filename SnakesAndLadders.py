import random

def get_players_list ():
    #retrieves names of two players
    player1=input ("Please enter name of player number 1: ")
    player2=input ("Please enter name of player number 2: ")
    name_list = [player1, player2]
    print ("The players are:", name_list)
    return name_list


def generate_ladders_position():
    #generates a random list of ladders positions
    ladders_list= []
    while len(ladders_list)<15:
        ladders=random.randint(5,85)
        if ladders not in ladders_list:
            ladders_list.append(ladders)
    ladders_list.sort()
    print ("Ladder cells: ", ladders_list)
    return ladders_list


def generate_snakes_position(ladders_list):
    #generates a random list of snake positions between 20 and 95 and not the same as ladder positions
    snakes_list=[]
    while len(snakes_list)<10:
        snakes=random.randint(20,95)
        if snakes not in snakes_list and snakes not in ladders_list:
            snakes_list.append(snakes)
    snakes_list.sort()
    print ("Snake cells:", snakes_list)
    return snakes_list


def roll_dice(current_position, player_name):
    #Rolls a random number between 1 and 6 both included and returns the new position of the player
        dice_roll=random.randint(1,6)
        new_current_position=int(current_position+dice_roll)
        print(str(player_name)+" dice is: " + str(dice_roll)+ " New current position is: "
              +str(new_current_position))
        return new_current_position

def check_for_ladder(current_position,ladders_list,player_name):
    #Checks to see if the new rolled position lands on a ladder
    if current_position in ladders_list:
        print("Woohoo! "+player_name+" it's a ladder! Climb up by 15 cells. Your new position is "+str(current_position+15))
        return current_position+15
    else:
        return current_position
    
        
   
def check_for_snake(current_position,snakes_list,player_name):
    #Checks to see if the new rolled position lands on a snake
    if current_position in snakes_list:
        print("Oops! You've been bitten! Go down 10 cells. Your new position is "+ str(current_position-10))
        return current_position-10
    else:
        return current_position
    

def main():
    players_positions=[0,0]
    name_list=get_players_list()
    ladders_list=generate_ladders_position()
    snakes_list=generate_snakes_position(ladders_list)
    
    while players_positions[0]<99 and players_positions[1]<99:
        for i in range(2):      
            new_current_position = roll_dice(players_positions[i], name_list[i])
            new_current_position = check_for_ladder(new_current_position, ladders_list, name_list[i])
            new_current_position = check_for_snake(new_current_position, snakes_list, name_list[i])
            players_positions[i]=new_current_position            
    winner_name = name_list[players_positions.index(max((players_positions[0],players_positions[1])))]  
    print("Hooray! Winner is "+winner_name)
                

main()