import art
import random
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_two_cards():
    ''' Creating list with two random card
    '''
    player_cards = []
    for i in range(2):
        random_card = random.choice(cards)
        player_cards.append(cards[random_card])
    eleven = True
    while eleven:
        if player_cards[0] == player_cards[1] == 11:
            player_cards.remove(11)
            random_card = random.choice(cards)
            player_cards.append(cards[random_card])
            continue
        else:
            eleven = False
            break
    return player_cards

def score_now(player_cards, computer_cards):
    '''Outputting information about your card now and one card by computer'''
    print(f"It's your card:{player_cards}, your sum: {sum(player_cards)}")
    print(f"It is one of card from computer {computer_cards[0]}")

def blackjack(player_cards, computer_cards):
    if sum(player_cards) == 21 and sum(computer_cards) == 21:
        print("Draw")
        return True
    elif sum(computer_cards) == 21:
        print("You lose")
        return True
    elif sum(player_cards) == 21:
        print("You win")
        return True
    else:
        return False


def adding_cards(player_cards):
    '''Bringing new card, so adding new random card to list'''
    max_num = len(cards)
    random_card = random.randint(0, max_num - 1)
    player_cards.append(cards[random_card])
    return player_cards

def checking_over_twenty_one(players_cards):
    '''Check if sum of card is more than 21 and return bool'''
    gave_over = False
    if sum(players_cards) > 21:
        if 11 in players_cards:
            index_of_ace = players_cards.index(11)
            players_cards[index_of_ace] = 1
            if sum(players_cards) > 21:
                gave_over = True
        else:
            gave_over = True
    return gave_over

def computer_play (computer_cards):
    '''Playing of computer. It can do nothing or add new cards '''
    stop = True
    while stop:
        over = checking_over_twenty_one(computer_cards)
        if over > 21:
            stop = False
        else:
            if sum(computer_cards) < 17:
                adding_cards(computer_cards)
            else:
                stop = False
    return computer_cards

def action(user, computer_cards):
    '''Action of user. You can choose to add card or do nothing'''
    while True:
        action = input("Do you want to add card? If you want , you must write y\n")
        if action == 'y' and checking_over_twenty_one(user) == False and blackjack(user, computer_cards) == False:
            adding_cards(user)
            print(f"It's your card: {user} and sum:{sum(user)}")
            checking_over_twenty_one(user)

        else:
            break
    return user

def win(user, computer):
    '''Method return output with info who win or lose'''
    check_user = checking_over_twenty_one(user)
    check_computer = checking_over_twenty_one(computer)
    print(f"It's your cards: {user} and sum: {sum(user)}")
    print(f"It's computer cards: {computer} and sum: {sum(computer)}")
    if check_user == True or (sum(user)<sum(computer) and check_computer == False):
        print("You lose")
    elif check_computer == True or sum(user)>sum(computer):
        print("You win")
    else:
        print("Draw")

def game():
    '''Start and control game'''
    print(art.logo)
    user = deal_two_cards()
    computer = deal_two_cards()
    score_now(user, computer)
    now = blackjack(user, computer)
    if now == False:
        action(user, computer)
        if checking_over_twenty_one(user) == True:
            print("You lose")
        else:
            computer_play(computer)
            win(user, computer)


def main():
    game()
    while True:
        answer = input("Do you want to play more? If you want, you must write y ")
        if answer != 'y':
            break
        else:
            clear()
            game()


if __name__ == '__main__':
    main()






