def blackjack_game():
      # 카드 뽑기 
  import random
  list = [ 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  my_pick = random.sample(list, 2)
  dealer_pick = random.sample(list, 2)
  dealer_show_card = random.choice(dealer_pick)

  print(f"나의 카드는 {my_pick}입니다")
  #print("#딜러 카드는:", dealer_pick)
  print(f"딜러 카드 중 한 장은 {dealer_show_card}입니다")

  # 내 점수, 딜러 점수
  def score_sum(card_pick):
    sum=0
    for card in card_pick:
      sum +=card
    return sum

  my_score = score_sum(my_pick)
  dealer_score = score_sum(dealer_pick)
  print(f"내 점수는 {my_score}입니다")
  #print("#딜러 점수는:", dealer_score)

  # 딜러 점수[1~16] < 17이면 카드 한 장 더 받고 합계 다시 계산하기
  # 딜러 점수 >21이면, 만약 새로 받은 한 장이 에이스일 경우에는 에이스 점수를 1로 바꾸고 점수에 따라 와일문 돌리기! 
  if dealer_score < 17:
    a = True
    while a:
      one_more_card = random.sample(list, 1)
      dealer_pick.extend(one_more_card)
      dealer_score = score_sum(dealer_pick)
      #print("#새로운 딜러의 카드:", dealer_pick)
      #print("#새로운 딜러 점수:", dealer_score)
      if dealer_score >16:
        if dealer_score >21:
          if one_more_card[0] == 11:
            dealer_pick.remove(11)
            dealer_pick.append(1)
            dealer_score = score_sum(dealer_pick)
            #print("#새로운 딜러의 카드:", dealer_pick)
            #print("#새로운 딜러 점수:", dealer_score)
            if dealer_score > 16:
              a = False
          else:
            a = False
        else:
          a = False

  # 승자 뽑기
  def winner(my_score, dealer_score):
    if my_score > dealer_score:
      if my_score == 21:
        print("블랙잭입니다.")
      print("승리입니다.")
    elif my_score == dealer_score:
      if my_score == 21:
        print("블랙잭입니다.")
      print("비겼습니다.")
    else:
      if dealer_score == 21:
        print("블랙잭입니다.")
      print("패배입니다.")

  # stand? or hit?
  def decision(my_score, dealer_score):
    stand_hit = input("stand 하시겠습니까? hit 하시겠습니까? ")
    keep_going = True
    while keep_going:
      if stand_hit == "stand":
        if dealer_score >21:
          print("승리입니다.")
          if my_score == 21:
            print("블랙잭입니다")
          keep_going = False
        else:
          winner(my_score, dealer_score)
          keep_going= False
      elif stand_hit == "hit":
        one_more_card = random.sample(list, 1)
        my_pick.extend(one_more_card)
        my_score = score_sum(my_pick)
        print(f"내가 가진 카드 리스트는 {my_pick}입니다")
        print(f"내 점수는 {my_score}입니다")
        if my_score > 21:
          if one_more_card[0] == 11:
            my_pick.remove(11)
            my_pick.append(1)
            my_score = score_sum(my_pick)
            print(f"내가 가진 카드 리스트는 {my_pick}입니다")
            print(f"내 점수는 {my_score}입니다")
            stand_hit = input("stand 하시겠습니까? hit 하시겠습니까? ")
          else:
            print("패배입니다.")
            if dealer_score == 21:
              print("블랙잭입니다!!!")
            keep_going = False
        else:
          stand_hit = input("stand 하시겠습니까? hit 하시겠습니까? ")

  decision(my_score, dealer_score)


game_going = True
while game_going:
  want_game = input("게임을 시작하시겠습니까? Y 아니면 N를 입력해주세요 : ")
  if want_game == "Y":
    print("게임을 시작합니다! 행운을 빕니다")
    blackjack_game()
  elif want_game == "y":
    print("게임을 시작합니다! 행운을 빕니다")
    blackjack_game()
  else:
    print("게임을 종료합니다.")
    game_going = False
    