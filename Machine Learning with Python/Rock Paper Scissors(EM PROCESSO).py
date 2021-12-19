#LINK PROJECT: https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors


def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""
    results = {"p1": 0, "p2": 0, "tie": 0}

    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            results["tie"] += 1
            winner = "Tie."
        elif (p1_play == "P" and p2_play == "R") or (
                p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                       and p2_play == "P"):
            results["p1"] += 1
            winner = "Player 1 wins."
        elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
            results["p2"] += 1
            winner = "Player 2 wins."

        if verbose:
            print("Player 1:", p1_play, "| Player 2:", p2_play)
            print(winner)
            print()

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_won = results['p2'] + results['p1']

    if games_won == 0:
        win_rate = 0
    else:
        win_rate = results['p1'] / games_won * 100

    print("Final results:", results)
    print(f"Player 1 win rate: {win_rate}%")

    return (win_rate)

def quincy(prev_play, counter=[0]):

    counter[0] += 1
    choices = ["R", "R", "P", "P", "S"]
    return choices[counter[0] % len(choices)]


def mrugesh(prev_opponent_play, opponent_history=[]):
    opponent_history.append(prev_opponent_play)
    last_ten = opponent_history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)

    if most_frequent == '':
        most_frequent = "S"

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[most_frequent]


def kris(prev_opponent_play):
    if prev_opponent_play == '':
        prev_opponent_play = "R"
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prev_opponent_play]


def abbey(prev_opponent_play,
          opponent_history=[],
          play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):

    if not prev_opponent_play:
        prev_opponent_play = 'R'
    opponent_history.append(prev_opponent_play)

    last_two = "".join(opponent_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    potential_plays = [
        prev_opponent_play + "R",
        prev_opponent_play + "P",
        prev_opponent_play + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }
    #print(sub_order)

    prediction = max(sub_order, key=sub_order.get)[-1:]
    #print(prediction)
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]


def player(prev_play, opponent_history=[], p =["R"], count=[0, 0, 0],
           play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):
    
    opponent_history.append(prev_play)
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    
    if count[0] >= 100:
      #print(count[1]/count[0], count[2])
      if count[1]/count[0] < 0.5:
        count[2] +=1
        count[0] = 0
        count[1] = 0
        count[2] = 0 if count[2] > 3 else count[2]
    
    if (p[-1] == "P" and prev_play == "R") or (p[-1] == "R" and prev_play == "S") or (p[-1] == "S" and prev_play == "P"): 
      count[1] += 1
      

    
    #print(count[2])

    
    if len(opponent_history) > 2:
      guess = p[0]
      if count[2] == 0:
        
        #quincy
        if prev_play == "S":
          p[0] = 'P' if opponent_history[-2] == 'P' else "R"
          guess = p[0]
          #print('quincy')
      
          
      elif count[2] == 1:
        #mrugesh
        guess = ideal_response[ideal_response[max(set(p), key=p.count)]]
        p.append(guess)
        #print('mrugesh')
      
      elif count[2] == 2:
        #kris 
        guess = ideal_response[ideal_response[p[-1]]]
        p[-1] = guess
        #print('kris')
      
      elif count[2] == 3:

        last_two = "".join(opponent_history[-2:])
        if len(last_two) == 2:
            play_order[0][last_two] += 1

        potential_plays = [
            p[-1]  + "R",
            p[-1]  + "P",
            p[-1] + "S",
        ]

        sub_order = {
            k: play_order[0][k]
            for k in potential_plays if k in play_order[0]
        }
        prediction = max(sub_order, key=sub_order.get)[-1:]
        #guess = ideal_response[prediction]

    
    else:
      guess = "R"

    count[0] += 1

    return guess



if __name__ == '__main__':
    play(player, quincy, 10)
    play(player, abbey, 10)
    play(player, kris, 10)
    play(player, mrugesh, 10)
