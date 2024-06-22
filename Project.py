import random
import requests


def split_into_sentences(introduction):
    sentences = introduction.replace('!', '.').replace('?', '.').split('.')
    return [sentence.strip() for sentence in sentences if sentence]

introduction = ("Hello Welcome to Top Trumps where you will play with the computer."
                "Each player has a pile of cards, and and the highest value wins the round, taking all the revealed cards."
                "The goal is to collect all the cards from the deck. Good Luck!!! ")

sentences = split_into_sentences(introduction)

for sentence in sentences:
    print(sentence)


def game():
    while True:
        machine = input("Please click Start or End? ").capitalize()
        if machine == "Start":
            print("Welcome to Top Trumps Game")
            break
        elif machine == "End":
            print("Bye")
            quit()
game()
def pokemon_game():
    pokemon_number = random.randint(1, 151)
    url = "https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon_number)
    request = requests.get(url)
    pokemon_request = request.json()
    return {'name': pokemon_request['name'],
            "height": pokemon_request['height'],
            'id': pokemon_request['id'],
            "weight": pokemon_request['weight']}
pokemon_game()

# Ask the user which stat they want to use (id, height or weight)
#Get a random Pokemon for the player and another for their opponent
# Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
def pokemon():
    my_pokemon = pokemon_game()
    print(my_pokemon)
    game = input("Please choose a category? (height, id, weight) ")
    player_1 = my_pokemon.get(game)
    print("Your stat: {} ".format(player_1))
    computer_pokemon = pokemon_game()
    computer = computer_pokemon.get(game)
    print("Computer stat: {} ".format(computer))

    if player_1 == computer:
        return "Draw"
    elif player_1 > computer:
        return "You win"
    else:
        return "You lose"


# Play multiple rounds and record the outcome
def play_multiple_rounds(num_rounds):
    player_wins = 0
    computer_wins = 0

    for _ in range(num_rounds):
        result = pokemon()
        print(result)

        if "win" in result:
            player_wins += 1
        elif "lose" in result:
            computer_wins += 1

    print("\nGame Over!")
    print(f"You won {player_wins} rounds.")
    print(f"Computer won {computer_wins} rounds.")

    if player_wins > computer_wins:
        print("You win the game!")
    elif player_wins < computer_wins:
        print("Computer wins the game!")
    else:
        print("The game is a draw!")


# Play the game with 5 rounds (you can change the number of rounds)
play_multiple_rounds(5)