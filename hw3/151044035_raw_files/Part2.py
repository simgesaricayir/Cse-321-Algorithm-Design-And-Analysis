def OneMileNIM(N,M,gamer1_move,gamer2_move,term):
    if term == 1 :
          gamer1_move = int(input("Player 1 Enter a pile num>>> "))
          while gamer1_move > M or gamer1_move ==0:
              gamer1_move = int(input("Wrong number.Enter a chip num? "))
          N = N - gamer1_move
          print("Player 1 was played"," left chips:",N)
          if N==0:
              if term == 1:
                print("Player1 is winner")
                return
              if term == 2:
                print("Player2 is winner")
                return
          term = 2
          OneMileNIM(N,M,gamer1_move,gamer2_move,term) 
    elif term == 2 :
          gamer2_move = int(input("Player 2 Enter a pile num >>> "))
          while gamer2_move > M or gamer2_move ==0:
              gamer2_move = int(input("Wrong number.Enter a chip num? "))
          N = N - gamer2_move
          print("Player 2 was played"," left chips:",N)
          if N==0:
              if term == 1:
                print("Player1 is winner")
                return 
              if term == 2:
                print("Player2 is winner")
                return
          term = 1
          OneMileNIM(N,M,gamer1_move,gamer2_move,term) 
         
            
            
M = 4
N = 20
OneMileNIM(N,M,0,0,1)  
  