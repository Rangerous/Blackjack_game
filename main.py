import random
#from art import logo



def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score, pc_score):
  if pc_score > 21 and user_score > 21:
    return "You went over. You lose."
  elif user_score == pc_score:
    return "It's a draw!"
  elif pc_score == 0:
    return "Opponent has a Blackjack, you lose."
  elif user_score == 0:
    return "You got a Blackjack, you win!"
  elif user_score > 21:
    return "You went over, you lose."
  elif pc_score > 21:
    return "Your opponent went over, you win!"
  elif user_score > pc_score:
    return "You win!"
  else:
    return "You lose"

def blackjack_game():
  user_cards = []
  pc_cards = []

  for i in range(0,2):
    user_cards.append(deal_card())
    pc_cards.append(deal_card())

  is_game_over = False
  while not is_game_over:
    user_score = calculate_score(user_cards)
    pc_score = calculate_score(pc_cards)
    print(f"Your cards: {user_cards}, current score {user_score}.")
    print(f"The PC's first card: {pc_cards[0]}")

    if user_score == 0 or pc_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_new_card = input("Type 'y' for a new card, type 'n' to pass.")
      if user_new_card == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while pc_score != 0 and pc_score < 17:
    pc_cards.append(deal_card())
    pc_score = calculate_score(pc_cards)

  print(f"Your final cards: {user_cards}, final score: {user_score}")
  print(f"PC's final cards: {pc_cards}, final score: {pc_score}")
  print(compare(user_score,pc_score))

while input("Do you wanna play a round of Blackjack? Type 'y' or 'n'") == "y":
  blackjack_game()
