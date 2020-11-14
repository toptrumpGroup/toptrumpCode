import requests
import random


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


player_one_1 = get_pokemon()
player_one_2 = get_pokemon()
player_one_3 = get_pokemon()

player_two_1 = get_pokemon()
player_two_2 = get_pokemon()
player_two_3 = get_pokemon()

print('\nPokemon 1:')
print('name: {}'.format(player_one_1['name']))
print('ID: {}'.format(player_one_1['id']))
print('height: {}'.format(player_one_1['height']))
print('weight: {}'.format(player_one_1['weight']))

print('\nPokemon 2')
print('name: {}'.format(player_one_2['name']))
print('ID: {}'.format(player_one_2['id']))
print('height: {}'.format(player_one_2['height']))
print('weight: {}'.format(player_one_2['weight']))

print('\nPokemon 3')
print('name: {}'.format(player_one_3['name']))
print('ID: {}'.format(player_one_3['id']))
print('height: {}'.format(player_one_3['height']))
print('weight: {}'.format(player_one_3['weight']))

print('\nPlease wait, percentages loading...')

arrayids = []
arrayheights = []
arrayweights = []

id_numbers = range(1, 151)
for id_number in id_numbers:
    response_id_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(id_number)
    ids = requests.get(response_id_url)
    total = ids.json()
    total_id = total['id']
    total_height = total['height']
    total_weight = total['weight']
    arrayids.append(total_id)
    arrayheights.append(total_height)
    arrayweights.append(total_weight)


stat_u_id_1 = player_one_1['id']
stat_u_id_2 = player_one_2['id']
stat_u_id_3 = player_one_3['id']

if stat_u_id_1 > stat_u_id_2 and stat_u_id_1 > stat_u_id_3:
    stat_u_id = stat_u_id_1
    print('\n{} has the highest ID stat.'.format(player_one_1['name']))
elif stat_u_id_2 > stat_u_id_1 and stat_u_id_2 > stat_u_id_3:
    stat_u_id = stat_u_id_2
    print('\n{} has the highest ID stat.'.format(player_one_2['name']))
elif stat_u_id_3 > stat_u_id_1 and stat_u_id_3 > stat_u_id_2:
    stat_u_id = stat_u_id_3
    print('\n{} has the highest ID stat.'.format(player_one_3['name']))
elif stat_u_id_1 == stat_u_id_2 and stat_u_id_1 > stat_u_id_3:
    stat_u_id = stat_u_id_1
    print('\n{} and'.format(player_one_1['name']), print('{} have the highest ID stats.'.format(player_one_2['name'])))
elif stat_u_id_1 == stat_u_id_3 and stat_u_id_1 > stat_u_id_2:
    stat_u_id = stat_u_id_1
    print('\n{} and'.format(player_one_1['name']), print('{} have the highest ID stats.'.format(player_one_3['name'])))
elif stat_u_id_2 == stat_u_id_3 and stat_u_id_2 > stat_u_id_1:
    stat_u_id = stat_u_id_2
    print('\n{} and'.format(player_one_2['name']), print('{} have the highest ID stats.'.format(player_one_3['name'])))
else:
    print('\nAll Pokemon have equal ID stats.')
    stat_u_id = stat_u_id_1

i = 0
for arrayid in arrayids:
    if stat_u_id > arrayid:
        i = i + 1
chance_of_winning_i = (i / 150) * 100
print('Percentage chance of winning with highest ID value: ', chance_of_winning_i)

stat_u_h_1 = player_one_1['height']
stat_u_h_2 = player_one_2['height']
stat_u_h_3 = player_one_3['height']

if stat_u_h_1 > stat_u_h_2 and stat_u_h_1 > stat_u_h_3:
    stat_u_h = stat_u_h_1
    print('\n{} has the highest height stat.'.format(player_one_1['name']))
elif stat_u_h_2 > stat_u_h_1 and stat_u_h_2 > stat_u_h_3:
    stat_u_h = stat_u_h_2
    print('\n{} has the highest height stat.'.format(player_one_2['name']))
elif stat_u_h_3 > stat_u_h_1 and stat_u_h_3 > stat_u_h_2:
    stat_u_h = stat_u_h_3
    print('\n{} has the highest height stat.'.format(player_one_3['name']))
elif stat_u_h_1 == stat_u_h_2 and stat_u_h_1 > stat_u_h_3:
    stat_u_h = stat_u_h_1
    print('\n{} and'.format(player_one_1['name']),
          print('{} have the highest height stats.'.format(player_one_2['name'])))
elif stat_u_h_1 == stat_u_h_3 and stat_u_h_1 > stat_u_h_2:
    stat_u_h = stat_u_h_1
    print('\n{} and'.format(player_one_1['name']),
          print('{} have the highest height stats.'.format(player_one_3['name'])))
elif stat_u_h_2 == stat_u_h_3 and stat_u_h_2 > stat_u_h_1:
    stat_u_h = stat_u_h_2
    print('\n{} and'.format(player_one_2['name']),
          print('\n{} have the highest height stats.'.format(player_one_3['name'])))
else:
    print('\nAll Pokemon have equal height stats.')
    stat_u_h = stat_u_h_1

j = 0
for arrayheight in arrayheights:
    if stat_u_h > arrayheight:
        j = j + 1
chance_of_winning_j = (j / 150) * 100
print('Percentage chance of winning with highest height value: ', chance_of_winning_j)

stat_u_w_1 = player_one_1['weight']
stat_u_w_2 = player_one_2['weight']
stat_u_w_3 = player_one_3['weight']

if stat_u_w_1 > stat_u_w_2 and stat_u_w_1 > stat_u_w_3:
    stat_u_w = stat_u_w_1
    print('\n{} has the highest weight stat.'.format(player_one_1['name']))
elif stat_u_w_2 > stat_u_w_1 and stat_u_w_2 > stat_u_w_3:
    stat_u_w = stat_u_w_2
    print('\n{} has the highest weight stat.'.format(player_one_2['name']))
elif stat_u_w_3 > stat_u_w_1 and stat_u_w_3 > stat_u_w_2:
    stat_u_w = stat_u_w_3
    print('\n{} has the highest weight stat.'.format(player_one_3['name']))
elif stat_u_w_1 == stat_u_w_2 and stat_u_w_1 > stat_u_w_3:
    stat_u_w = stat_u_w_1
    print('\n{} and'.format(player_one_1['name']),
          print('{} have the highest weight stats.'.format(player_one_2['name'])))
elif stat_u_w_1 == stat_u_w_3 and stat_u_w_1 > stat_u_w_2:
    stat_u_w = stat_u_w_1
    print('\n{} and'.format(player_one_1['name']),
          print('{} have the highest weight stats.'.format(player_one_3['name'])))
elif stat_u_w_2 == stat_u_w_3 and stat_u_w_2 > stat_u_w_1:
    stat_u_w = stat_u_w_2
    print('\n{} and'.format(player_one_2['name']),
          print('{} have the highest weight stats.'.format(player_one_3['name'])))
else:
    print('\nAll Pokemon have equal weight stats.')
    stat_u_w = stat_u_w_1


k = 0
for arrayweight in arrayweights:
    if stat_u_w > arrayweight:
        k = k + 1
chance_of_winning_k = (k / 150) * 100
print('Percentage chance of winning with highest weight value: ', chance_of_winning_k)

if chance_of_winning_i > chance_of_winning_j and chance_of_winning_i > chance_of_winning_k:
    print('\nYou are most likely to win using the highest ID value!')
elif chance_of_winning_j > chance_of_winning_i and chance_of_winning_j > chance_of_winning_k:
    print('\nYou are most likely to win using the highest height value!')
elif chance_of_winning_k > chance_of_winning_i and chance_of_winning_k > chance_of_winning_j:
    print('\nYou are most likely to win using the highest weight value!')
elif chance_of_winning_i > chance_of_winning_j and chance_of_winning_i == chance_of_winning_k:
    print('\nYou are most likely to win using the highest ID or height value!')
elif chance_of_winning_j > chance_of_winning_i and chance_of_winning_j == chance_of_winning_k:
    print('\nYou are most likely to win using the highest height or weight value!')
elif chance_of_winning_i > chance_of_winning_k and chance_of_winning_i == chance_of_winning_j:
    print('\nYou are most likely to win using the highest ID or weight value!')
else:
    print('\nYou are equally likely to win with any value!')


stat_c_id_1 = player_two_1['id']
stat_c_id_2 = player_two_2['id']
stat_c_id_3 = player_two_3['id']

if stat_c_id_1 > stat_c_id_2 and stat_c_id_1 > stat_c_id_3:
    stat_c_id = stat_c_id_1
elif stat_c_id_2 > stat_c_id_1 and stat_c_id_2 > stat_c_id_3:
    stat_c_id = stat_c_id_2
elif stat_c_id_3 > stat_c_id_2 and stat_c_id_3 > stat_c_id_1:
    stat_c_id = stat_c_id_3
elif stat_c_id_1 == stat_c_id_2 and stat_c_id_1 > stat_c_id_3:
    stat_c_id = stat_c_id_1
elif stat_c_id_1 == stat_c_id_3 and stat_c_id_1 > stat_c_id_2:
    stat_c_id = stat_c_id_1
elif stat_c_id_3 == stat_c_id_2 and stat_c_id_3 > stat_c_id_1:
    stat_c_id = stat_c_id_2
else:
    stat_c_id = stat_c_id_1

stat_c_h_1 = player_two_1['height']
stat_c_h_2 = player_two_2['height']
stat_c_h_3 = player_two_3['height']

if stat_c_h_1 > stat_c_h_2 and stat_c_h_1 > stat_c_h_3:
    stat_c_h = stat_c_h_1
elif stat_c_h_2 > stat_c_h_1 and stat_c_h_2 > stat_c_h_3:
    stat_c_h = stat_c_h_2
elif stat_c_h_3 > stat_c_h_2 and stat_c_h_3 > stat_c_h_1:
    stat_c_h = stat_c_h_3
elif stat_c_h_1 == stat_c_h_2 and stat_c_h_1 > stat_c_h_3:
    stat_c_h = stat_c_h_1
elif stat_c_h_1 == stat_c_h_3 and stat_c_h_1 > stat_c_h_2:
    stat_c_h = stat_c_h_1
elif stat_c_h_3 == stat_c_h_2 and stat_c_h_3 > stat_c_h_1:
    stat_c_h = stat_c_h_2
else:
    stat_c_h = stat_c_h_1

stat_c_w_1 = player_two_1['weight']
stat_c_w_2 = player_two_2['weight']
stat_c_w_3 = player_two_3['weight']

if stat_c_w_1 > stat_c_w_2 and stat_c_w_1 > stat_c_w_3:
    stat_c_w = stat_c_w_1
elif stat_c_w_2 > stat_c_w_1 and stat_c_w_2 > stat_c_w_3:
    stat_c_w = stat_c_w_2
elif stat_c_w_3 > stat_c_w_2 and stat_c_w_3 > stat_c_w_1:
    stat_c_w = stat_c_w_3
elif stat_c_w_1 == stat_c_w_2 and stat_c_w_1 > stat_c_w_3:
    stat_c_w = stat_c_w_1
elif stat_c_w_1 == stat_c_w_3 and stat_c_w_1 > stat_c_w_2:
    stat_c_w = stat_c_w_1
elif stat_c_w_3 == stat_c_w_2 and stat_c_w_3 > stat_c_w_1:
    stat_c_w = stat_c_w_2
else:
    stat_c_w = stat_c_w_1

pokemon_choice_input = input('\nWhich Pokemon do you want to choose - 1, 2, or 3? ')

stat_choice_input = input('\nWhich stat do you want to use - ID, height, or weight? ')

if pokemon_choice_input == '1':
    pokemon_choice = player_one_1
elif pokemon_choice_input == '2':
    pokemon_choice = player_one_2
elif pokemon_choice_input == '3':
    pokemon_choice = player_one_3
else:
    pokemon_choice = random.choice([player_two_1, player_one_2, player_one_3])


def find_stat(stat_choice_input):
    if stat_choice_input == 'id':
        stat_u = pokemon_choice['id']
        stat_c = stat_c_id
        if stat_u > stat_c:
            print('\nYou win!')
            print('Your value:', stat_u)
            print('Computer value:', stat_c)
        elif stat_u == stat_c:
            print('\nDraw!')
        else:
            print('\nYou lose!')
            print('Your value:', stat_u)
            print('Computer value:', stat_c)

    elif stat_choice_input == 'height':
        stat_u = pokemon_choice['height']
        stat_c = stat_c_h
        if stat_u > stat_c:
            print('\nYou win!')
            print('Your value:', stat_u)
            print('Computer value:', stat_c)
        elif stat_u == stat_c:
            print('\nDraw!')
        else:
            print('\nYou lose!')
            print('Your value:', stat_u)
            print('Computer value:', stat_c)

    elif stat_choice_input == 'weight':
        stat_u = pokemon_choice['weight']
        stat_c = stat_c_w
        if stat_u > stat_c:
            print('\nYou win!')
            print('Your value:', stat_u)
            print('Computer value:', stat_c)
        elif stat_u == stat_c:
            print('\nDraw!')
        else:
            print('\nYou lose!')
            print('Your value:', stat_u)
            print('Computer value:', stat_c)

    else:
        replace = input('Incorrect value entered, please choose id, height, or weight ')
        find_stat(replace)


find_stat(stat_choice_input)
