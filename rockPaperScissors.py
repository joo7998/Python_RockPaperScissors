import random

def play():
    user = input("Enter 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    print(f'\nYou chose {user}, computer chose {computer}.\n')

    if user == computer:
        return 'It\'s a tie'

    if win(user, computer):
        return 'You won'

    return 'You lost'

def win(player, opponent):
    # TURE if player wins
    # r > s, p > r, s > p
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') \
        or (player == 's' and opponent == 'p'):
        return True

print(play())