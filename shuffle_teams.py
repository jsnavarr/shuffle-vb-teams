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


def split_array(array, team_size):
    game = []
    
    for i in range(0, int(len(array)/(2*team_size))):
        team = []
        for j in range(0,2):
            team.append(array[(i*4)+(j*2):(i*4)+(j*2)+2])
        game.append(team)
    return game


def shuffle_teams():
  n_part = int(sys.argv[1])
  team_size = int(sys.argv[2])
  participants=list(range(1, n_part+1))

  random.shuffle(participants)
  print(participants)
  round1=split_array(participants, team_size)
  print(round1)


if __name__ == "__main__":
    #arguments would be number of participants and team size
    if len(sys.argv)>=1 and sys.argv[1]:
        shuffle_teams()
    else:
        print('Please add number of players and team size')