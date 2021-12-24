def player(prev_play, opponent_history=[], plb = ['S', 'R', 'S', 'R'], hist = [[] ,[] ,[], []], jogadas_hist = []):
    opponent_history.append(prev_play if prev_play != '' else "R")
    chance_strage = [0, 0, 0, 0]
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
  
    guess = "R"
    if len(opponent_history) > 2: 
        #
      opponentlast10 = opponent_history[-10:].copy()
      for e in range(len(hist)):
        acertos = 0
        playlast10 = hist[e][-10:].copy()
        for x in range(len(playlast10)):
          #print(e, ideal_response[opponentlast10[x]], playlast10[x])
          if ideal_response[opponentlast10[x]] == playlast10[x]:
            acertos += 1
        chance_strage[e] = acertos/len(playlast10) if acertos != 0 else 0
     # print(chance_strage)  
        #
      #quincy
        
      if prev_play == "S":
        plb[0] = 'P' if opponent_history[-2] == 'P' else "R"    
      
      elif len(set(opponent_history[-4:])) == 1:
        plb[0] = 'P' if opponent_history[-2] == 'P' else "R"  
      hist[0].append(plb[0])
      #quincy

      #mrugesh
      plb[1] = ideal_response[ideal_response[max(set(jogadas_hist), key=jogadas_hist.count)]]
      hist[1].append(plb[1])
      #print('mrugesh')

      #kris 
      plb[2] = ideal_response[ideal_response[jogadas_hist[-1]]]
      hist[2].append(plb[2])
      #print('kris')

      #abbey
      plb[3] = ideal_response[max(set(opponent_history), key=opponent_history.count)]
      plb[3] = ideal_response[plb[3]] if chance_strage[3] >= 0.6 else plb[3]
      plb[3] = ideal_response[ideal_response[plb[3]]] if chance_strage[3] >= 0.5 and opponent_history[-1] == jogadas_hist[-1] else plb[3]
      hist[3].append(plb[3])
      #abbey
      #print(plb)
      guess = plb[chance_strage.index(max(chance_strage))]
    
    jogadas_hist.append(guess)    
    return guess


def player(prev_play, opponent_history=[], plb = ['S', 'R', 'S', 'R', "P", "S"], hist = [[] ,[] ,[], [], [], []], jogadas_hist = []):
    opponent_history.append(prev_play if prev_play != '' else "R")
    chance_strage = [0, 0, 0, 0, 0, 0]
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
  
    guess = "R"
    if len(opponent_history) > 2: 
      #Chances
      opponentlast10 = opponent_history[-10:].copy()
      for e in range(len(hist)):
        acertos = 0
        playlast10 = hist[e][-10:].copy()
        for x in range(len(playlast10)):
          if ideal_response[opponentlast10[x]] == playlast10[x]:
            acertos += 2
        chance_strage[e] = acertos/len(playlast10) if acertos != 0 else 0        
        #Chances
      print(chance_strage)
      #quincy
      if prev_play == "S":
        plb[0] = 'P' if opponent_history[-2] == 'P' else "R"    
      
      elif len(set(opponent_history[-4:])) == 1:
        plb[0] = 'P' if opponent_history[-2] == 'P' else "R"  
      hist[0].append(plb[0])
      #quincy

      #mrugesh
      plb[1] = ideal_response[ideal_response[max(set(jogadas_hist[-10:]), key=jogadas_hist[-10:].count)]]
      hist[1].append(plb[1])
      #mrugesh

      #kris 
      plb[2] = ideal_response[ideal_response[jogadas_hist[-1]]]
      hist[2].append(plb[2])
      #kris

      #abbey
      last_cem = jogadas_hist[-50:]
      play_order = {"R":{"RR":0, "RP":0, "RS":0}, "S":{"SR":0, "SP":0, "SS":0}, "P":{"PR":0, "PP":0, "PS":0}}
      for order in play_order[last_cem[-1]].keys():
        play_order[last_cem[-1]][order] = ''.join(last_cem).count(order)
      plb[3] = ideal_response[max(play_order[last_cem[-1]], key=play_order[last_cem[-1]].get)[-1]]
      plb[3] = ideal_response[plb[3]]
      hist[3].append(plb[3])
      #abbey
      
      #Suport
      plb[4] = ideal_response[plb[3]]
      hist[4].append(plb[4])
      #Suport

      last_cem = opponent_history[-500:]
      play_order = {"R":{"RR":0, "RP":0, "RS":0}, "S":{"SR":0, "SP":0, "SS":0}, "P":{"PR":0, "PP":0, "PS":0}}
      for order in play_order[last_cem[-1]].keys():
        play_order[last_cem[-1]][order] = ''.join(last_cem).count(order)
      plb[5] = ideal_response[max(play_order[last_cem[-1]], key=play_order[last_cem[-1]].get)[-1]]
      #plb[5] = ideal_response[plb[5]]
      hist[5].append(plb[5])
      print(plb)
      guess = plb[chance_strage.index(max(chance_strage))]
    
    jogadas_hist.append(guess)    
    return guess
