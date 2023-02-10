import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_two_cards():
    ''' Creating list with two random card
    '''
    player_cards = []
    for i in range(2):
        max_num = len(cards)
        random_card = random.randint(0, max_num-1)
        player_cards.append(cards[random_card])
    eleven = True
    while eleven:
        if player_cards[0] == player_cards[1] == 11:
            max_num = len(cards)
            random_card = random.randint(0, max_num - 1)
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
        random_act = random.randint(0, 1)
        print(random_act)
        if over > 21:
            stop = False
        else:
            if sum(computer_cards) < 17:
                adding_cards(computer_cards)
            else:
                stop = False
    return computer_cards

def action(user):
    '''Action of user. You can choose to add card or do nothing'''
    while True:
        action = input("Do you want to add card? If you want , you must write y\n")
        if action == 'y' and checking_over_twenty_one(user) == False:
            adding_cards(user)
            print(str(user) + " " + str(sum(user)))
            checking_over_twenty_one(user)
        else:
            break
    return user

def win(user, computer):
    '''Method return output with info who win or lose'''
    check_user = checking_over_twenty_one(user)
    check_computer = checking_over_twenty_one(computer)
    print(str(user)+" "+str(sum(user)))
    print(str(computer)+" "+str(sum(computer)))
    if check_user == True or (sum(user)<sum(computer) and check_computer == False):
        print("You lose")
    elif check_computer == True or sum(user)>sum(computer):
        print("You win")
    else:
        print("Draw")

def main():
    print(art.logo)
    user = deal_two_cards()
    computer = deal_two_cards()
    score_now(user, computer)
    action(user)
    if checking_over_twenty_one(user) == True:
        print("You lose")
    else:
        computer_play(computer)
        win(user, computer)

main()










