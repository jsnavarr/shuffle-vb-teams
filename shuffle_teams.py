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

players = ["Chevy", "Rebekah", "VJ", "Andrei", "Luke", "Danika", "Greg", "RV", 
           "Salvador", "Benji", "Jet", "Eric", "Nat", "Olivia", "Vanessa", "Eddy", "Sameep", "Bri"]

players_dict = {}

def split_array(array, team_size):
    game = []

    for i in range(0, int(len(array)/(2*team_size))):
        team = []
        for j in range(0,2):
            team.append(array[(i*team_size*2)+(j*team_size):(i*team_size*2)+(j*team_size)+team_size])
        game.append(team)
    return game

def init_teams(n_part, team_size, participants):
    # players_dict first element is the player name
    # second element is a counter for the times player has sat
    # third element is the index of the player who this player has played with

    for i in range(1, n_part+1):
        # if we have less/equal participants that current names in "players", add the name
        if(n_part<=len(players)):
            players_dict[i]=[players[i], 0, 0]
        else:
            # if we have less/equal participants that current names in "players", add the name
            players_dict[i]=["playerX"+i, 0, 0]

def print_names(games):
    for i in range(0,len(games)):
        print("Game "+str(i)+" :")
        for j in range(0, len(games[i])):
            print("    Team "+str(j)+" :")
            for k in range(0, len(games[i][j])):
                print("          "+players_dict[games[i][j][k]][0])


def shuffle_teams(n_part, team_size, participants):
  random.shuffle(participants)
  round1=split_array(participants, team_size)
  print_names(round1)


if __name__ == "__main__":
    #arguments would be number of participants and team size
    if len(sys.argv)>=1 and sys.argv[1]:
        n_part = int(sys.argv[1])
        team_size = int(sys.argv[2])
        participants=list(range(1, n_part+1))
        init_teams(n_part, team_size, participants)
        shuffle_teams(n_part, team_size, participants)
        
    else:
        print('Please add number of players and team size')