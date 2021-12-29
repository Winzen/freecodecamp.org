#LINK PROJECT: https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors
# LINK TEST RUN: https://replit.com/@LuizSinx/boilerplate-rock-paper-scissors-15#main.py

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
    # print(play_order[0])
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

    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]


def player(prev_play, opponent_history=[], plb=['X', 'X', 'X', 'X'], hist=[[], [], [], [], []], jogadas_hist=[],
           Q=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
    opponent_history.append(prev_play)
    chance_strage = [0, 0, 0, 0, 0, 0]
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    states = {'P': 0, 'R': 1, 'S': 2, 0: 'P', 1: 'R', 2: 'S'}

    if prev_play == '':
        jogadas_hist.clear()
        opponent_history.clear()
        Q = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for e in range(len(hist)):
            hist[e].clear()

    guess = "R"
    if len(opponent_history) > 2:

        # Chances
        opponentlast10 = opponent_history[-5:].copy()
        for e in range(len(hist)):
            acertos = 0
            playlast10 = hist[e][-5:].copy()
            for x in range(len(playlast10)):
                if ideal_response[opponentlast10[x]] == playlast10[x]:
                    acertos += 1
            chance_strage[e] = (acertos - (1 if ideal_response[hist[e][-1]] == prev_play else 0)) / len(
                playlast10) if acertos != 0 else 0
            # Chances

        # quincy
        reward = 1 if jogadas_hist[-1] == ideal_response[prev_play] else 0
        state = states[prev_play]
        action = states[jogadas_hist[-1]]

        Q[state][action] = Q[state][action] + 0.5 * (reward + 0.94 * max(Q[state]) - Q[state][action])
        plb[0] = ideal_response[jogadas_hist[-1]]

        if len(opponent_history) > 5:
            plb[0] = states[Q[state].index(max(Q[state]))]

        hist[0].append(plb[0])
        # quincy

        # mrugesh
        plb[1] = ideal_response[ideal_response[max(set(jogadas_hist[-10:]), key=jogadas_hist[-10:].count)]]
        hist[1].append(plb[1])
        # mrugesh

        # kris
        plb[2] = ideal_response[ideal_response[jogadas_hist[-1]]]
        hist[2].append(plb[2])
        # kris

        # abbey
        last_cem = jogadas_hist[-1000:]
        play_order = {"R": {"RR": 0, "RP": 0, "RS": 0}, "S": {"SR": 0, "SP": 0, "SS": 0},
                      "P": {"PR": 0, "PP": 0, "PS": 0}}
        for order in play_order[last_cem[-1]].keys():
            play_order[last_cem[-1]][order] = ''.join(last_cem).count(order)
        plb[3] = ideal_response[max(play_order[last_cem[-1]], key=play_order[last_cem[-1]].get)[-1]]
        plb[3] = ideal_response[plb[3]]
        hist[3].append(plb[3])
        # abbey

        guess = plb[chance_strage.index(max(chance_strage))]

    jogadas_hist.append(guess)
    return guess

if __name__ == '__main__':
    play(player, quincy, 1000)
    play(player, abbey, 1000)
    play(player, kris, 1000)
    play(player, mrugesh, 1000)