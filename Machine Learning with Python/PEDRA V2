def player(prev_play, opponent_history=[], plb = ['S', 'R', 'S', 'R'], hist = [[] ,[] ,[]], jogadas_hist = []):
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
        for x in range(len(playlast10[-10:])):
          #print(e, ideal_response[opponentlast10[x]], playlast10[x])
          if ideal_response[opponentlast10[x]] == playlast10[x]:
            acertos += 1
        chance_strage[e] = acertos/len(playlast10) if acertos != 0 else 0  
        #
      #quincy
        
      if prev_play == "S":
        plb[0] = 'P' if opponent_history[-2] == 'P' else "R"    
      
      elif len(set(opponent_history[-4:])) == 1:
        plb[0] = 'P' if opponent_history[-2] == 'P' else "R"  
      hist[0].append(plb[0])

      #mrugesh
      plb[1] = ideal_response[ideal_response[max(set(jogadas_hist), key=jogadas_hist.count)]]
      hist[1].append(plb[1])
      #print('mrugesh')

      #kris 
      plb[2] = ideal_response[ideal_response[jogadas_hist[-1]]]
      hist[2].append(plb[2])
      #print('kris')
      
      guess = plb[chance_strage.index(max(chance_strage))]
    
    jogadas_hist.append(guess)    
    return guess
