def Rock_Paper_Scissors():
    import random   
    user = (str(input("Which do you pick?\n'R' for Rock, 'P' for Paper, 'S' for Scissors\n: "))).upper()
    characters = ['R', 'P', 'S']
    if user in characters:
        if user == 'R':
            player = 'Rock'
        if user == 'P':
            player = 'Paper'
        if user == 'S':
            player = 'Scissors'
    else:
        player = 'Error'
    characters = ['R', 'P', 'S']
    computer = random.choice(characters) 
    if computer == 'R':
        CPU = 'Rock'
    if computer == 'P':
        CPU = 'Paper'
    if computer == 'S':
        CPU = 'Scissors'
    print('Player (' + player +') : CPU (' + CPU + ')')
    while user not in characters:
        print("Error!/nPick R, P or S")
        user = (str(input("Which do you pick?\n'R' for rock, 'P' for paper, 'S' for scissors\n: "))).upper()
    while user in characters:
        if user == computer:
            return "It\'s a tie"
        if is_win(user, computer):
            return "You win!!!"
        return "You lost!"
def is_win(user, computer):
    if (user == 'R' and computer == 'S') or (user == 'S' and computer == 'P') or (user == 'P' and computer == 'R'):
        return True      
print(Rock_Paper_Scissors())
again = str(input("Do you want to play another round?: Y/N\n:")).upper()
while again == 'Y':
    print(Rock_Paper_Scissors())
    again = str(input("Do you want to play another round?: Y/N\n:")).upper()
if again == 'N':
    print("Thanks for playing!")      
else:
    print("Invalid response!")
    again = str(input("Do you want to play another round?: Y/N\n:")).upper()
    while again == 'Y':
        print(Rock_Paper_Scissors())
        again = str(input("Do you want to play another round?: Y/N\n:")).upper()
    if again == 'N':
       print("Thanks for playing!")