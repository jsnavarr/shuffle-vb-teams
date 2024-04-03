# start with a list with n elements
# shuffle the list and create the first teams
# the next round of teams would consider past partners and remaining members:

# participants: initial list
# n_part: number of participants
# team_size: the team size, 2 for sand volleyball
# aval_part: available participants, would be all members minus current participant,
#           minus previous partners

import sys
import random

#players = ["Chevy", "Rebekah", "VJ", "Andrei", "Luke", "Danika", "Greg", "RV", 
#           "Salvador", "Benji", "Jet", "Eric", "Nat", "Olivia", "Vanessa", "Eddy", "Sameep", "Bri"]

players = ["Chevy", "Rebekah", "VJ", "Luke", "RV", "Salvador"]


players_dict = {}

def split_array(array, team_size):
    game = []

    for i in range(0, int(len(array)/(2*team_size))): # number of participants divided by team_size*2
        team = []
        for j in range(0,2): # run it twice per iteration to set 2 teams
            team.append(array[(i*team_size*2)+(j*team_size):(i*team_size*2)+(j*team_size)+team_size])

        #add the player index to the list of players each player has played with
        #print("Team: ", team)

        game.append(team)

    # add the third element in  players_dict that represents who this player has played with
    # go team by team
    for g in game:
        for team in g: # should always be 2?
            #print("Team     :", team)
            if len(team):
                for k in range(team_size-1): # go player by player
                    for l in range(k+1, team_size): #but start in the next one
                        #print("Team member: ", team[k])
                        #print("Team member: ", team[l])
                        players_dict[team[k]][2].append(team[l])
                        players_dict[team[l]][2].append(team[k])
    
    # increase the counter for those who were not included in this game
    # that is the second element of players_dict
    # we could just take the last elements in array argument who were not added to a game
    # len(array)-len(game*2*team_size) -> is the starting element?
    
    #print("len(game):   ", len(game))
    for i in range(len(game)*2*team_size, len(array)):
        #print("i:  ", i)
        players_dict[array[i]][1]=players_dict[array[i]][1]+1

    return game

def init_teams(n_part, team_size, participants):
    # players_dict first element is the player name
    # second element is a counter for the times player has sat
    # third element is the index of the player who this player has played with

    for i in range(1, n_part+1):
        # if we have less/equal participants that current names in "players", add the name
        if(n_part<=len(players)):
            players_dict[i]=[players[i-1], 0, []]
        else:
            # if we have less/equal participants that current names in "players", add the name
            players_dict[i]=["playerX"+str(i), 0, []]

def print_names(games):
    #print(players_dict)
    for i in range(0,len(games)):
        print("Game "+str(i)+" :")
        for j in range(0, len(games[i])):
            print("    Team "+str(j)+" :")
            for k in range(0, len(games[i][j])):
                print("          "+players_dict[games[i][j][k]][0])

def order_teams(n_part, team_size, participants, game_number):
    # game_number would help to sort the participants, this function is called starting game 2
    # at game N, people might have sat no more than N-1 (i.e. game 2 players would have sat 1 time)
    # create 2 lists, one with those who has sat more and the rest
    
    unlucky_players=[] #those who has sat more (game number -1 times)
    lucky_players=[] #thos who has sat less

    #check if somebody has sat (n_part%(team_size*2))     
    if(n_part%(team_size*2)>0):
        # they have sat the game_number (i.e. in game 2 they have sat once)
        # loop one by one in the participants list to separate the 2 groups
        for i in range(len(participants)):
            #print("i: ", i)
            #print("participants[i] : ", participants[i])
            if players_dict[participants[i]][1]==game_number-1:
                #those who has sat more
                unlucky_players.append(participants[i])
            else:
                #those who has sat less
                lucky_players.append(participants[i])
        random.shuffle(unlucky_players)
        random.shuffle(lucky_players)

        return unlucky_players+lucky_players
    else:
        #print("no mix, just shuffle the participants")
        #print("participants before shuffle: ", participants)
        random.shuffle(participants)
        return participants



def shuffle_teams(n_part, team_size, participants, n_games):
  for i in range(n_games):
    if i==0:
        random.shuffle(participants) #shuffle the participants
    else:
        # only shuffle the people who has not sat or who has sat less
        # try to pair people who they have not played with
        participants = order_teams(n_part, team_size, participants, i)
    #print("after calling order_teams: ", participants)
    #split the array to create the teams after it was shuffled
    game=split_array(participants, team_size)
    print_names(game)
    


if __name__ == "__main__":
    #arguments would be number of participants, team size, number of games
    if len(sys.argv)>=1 and sys.argv[1]:
        n_part = int(sys.argv[1])
        team_size = int(sys.argv[2])
        participants=list(range(1, n_part+1))
        n_games=int(sys.argv[3])
        init_teams(n_part, team_size, participants)
        shuffle_teams(n_part, team_size, participants, n_games)
        
    else:
        print('Please add number of players and team size')