import csv
import random
import requests
from pprint import pprint

player_name = input("What is your player name?")
print('Hi', player_name, 'Welcome to the pokemon top trump game!')

results = []
with open("pokemon_records.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        results.append(row)


with open('pokemon_records.csv', 'w') as records:
    pokemon_scores = csv.writer(records, delimiter=',')
    if len(results) > 0:
        for value in results:
            pokemon_scores.writerow([value])
    else:
        pokemon_scores.writerow(['Player name', 'ID', 'Pokemon name', 'Weight', 'Height', 'Result'])

    def get_pokemon():
        pokemon_number = random.randint(1, 151)
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
        response = requests.get(url)
        pokemon = response.json()

        return {
            'name': pokemon['name'],
            'id': pokemon['id'],
            'height': pokemon['height'],
            'weight': pokemon['weight'],
        }

    player_one = get_pokemon()
    player_two = get_pokemon()
    print('Congratulations! you have been given {}!\n\nStats:'.format(player_one['name']))
    print('Pokemon ID: ' + str(player_one['id']))
    print('Pokemon Name: ' + player_one['name'])
    print('Pokemon Height: ' + str(player_one['height']))
    print('Pokemon Weight: ' + str(player_one['weight']))


    def find_stat(stat):
        global player_score
        if stat == 'id':
            player_one_value = player_one['id']
            player_two_value = player_two['id']
            if player_one_value > player_two_value:
                print("You won")
                print("Enemies value was:" + str(player_two_value))
                player_score = 'win'
            else:
                print("You lose")
                print("Enemies value was:" + str(player_two_value))
                player_score = 'loss'
        elif stat == 'height':
            player_one_value = player_one['height']
            player_two_value = player_two['height']
            if player_one_value > player_two_value:
                print("You won")
                print("Enemies value was:" + str(player_two_value))
                player_score = 'win'
            else:
                print("You lose")
                print("Enemies value was:" + str(player_two_value))
                player_score = 'loss'

        elif stat == 'weight':
            player_one_value = player_one['weight']
            player_two_value = player_two['weight']
            if player_one_value > player_two_value:
                print("You won")
                print("Enemies value was:" + str(player_two_value))
                player_score = 'win'
            else:
                print("You lose")
                print("Enemies value was:" + str(player_two_value))
                player_score = 'loss'
        else:
            replace = input('Incorrect stat value, please choose a different value')
            find_stat(replace)

    choose_stat = input('Which stat would you like to choose from (by id, height, weight)?')

    find_stat(choose_stat)

    pokemon_scores.writerow([player_name, player_one['id'], player_one['name'], player_one['weight'], player_one['height'], player_score])
























