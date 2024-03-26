#start with a list with n elements
#shuffle the list and create the first teams
#the next round of teams would consider past partners and remaining members:

#participants: initial list
#n_part: number of participants
#aval_part: available participants, would be all members minus current participant,
#           minus previous partners

import sys
import random


def split_array(array, size):
    result = []
    for i in range(0, len(array), size):
        result.append(array[i:i+size])
    return result


def shuffle_teams():
  n_part = int(sys.argv[1])
  participants=list(range(1, n_part+1))

  random.shuffle(participants)
  round1=split_array(participants, 2)
  print(round1)


if __name__ == "__main__":
    #arguments would be number of participants and team size
    if len(sys.argv)>=1 and sys.argv[1]:
        shuffle_teams()
    else:
        print('Please add number of players and team size')