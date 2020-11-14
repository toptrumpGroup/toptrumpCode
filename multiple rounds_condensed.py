import requests
import random

wins = list()
i = 0


def single_round():
    def one_round():
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


        player_one_1_r1 = get_pokemon()
        player_one_2_r1 = get_pokemon()
        player_one_3_r1 = get_pokemon()

        player_two_1_r1 = get_pokemon()
        player_two_2_r1 = get_pokemon()
        player_two_3_r1 = get_pokemon()

        print('\nPokemon 1:')
        print('name: {}'.format(player_one_1_r1['name']))
        print('ID: {}'.format(player_one_1_r1['id']))
        print('height: {}'.format(player_one_1_r1['height']))
        print('weight: {}'.format(player_one_1_r1['weight']))

        print('\nPokemon 2')
        print('name: {}'.format(player_one_2_r1['name']))
        print('ID: {}'.format(player_one_2_r1['id']))
        print('height: {}'.format(player_one_2_r1['height']))
        print('weight: {}'.format(player_one_2_r1['weight']))

        print('\nPokemon 3')
        print('name: {}'.format(player_one_3_r1['name']))
        print('ID: {}'.format(player_one_3_r1['id']))
        print('height: {}'.format(player_one_3_r1['height']))
        print('weight: {}'.format(player_one_3_r1['weight']))

        stat_c_id_1 = player_two_1_r1['id']
        stat_c_id_2 = player_two_2_r1['id']
        stat_c_id_3 = player_two_3_r1['id']

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

        stat_c_h_1 = player_two_1_r1['height']
        stat_c_h_2 = player_two_2_r1['height']
        stat_c_h_3 = player_two_3_r1['height']

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

        stat_c_w_1 = player_two_1_r1['weight']
        stat_c_w_2 = player_two_2_r1['weight']
        stat_c_w_3 = player_two_3_r1['weight']

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
            pokemon_choice = player_one_1_r1
        elif pokemon_choice_input == '2':
            pokemon_choice = player_one_2_r1
        elif pokemon_choice_input == '3':
            pokemon_choice = player_one_3_r1
        else:
            pokemon_choice = random.choice([player_two_1_r1, player_one_2_r1, player_one_3_r1])

        def find_stat(stat_choice_input):
            if stat_choice_input == 'id':
                stat_u = pokemon_choice['id']
                stat_c = stat_c_id
                if stat_u > stat_c:
                    print('\nYou win!')
                    print('Your value:', stat_u)
                    print('Computer value:', stat_c)
                    round1 = i+1
                    wins.append('Win')
                elif stat_u == stat_c:
                    print('\nDraw!')
                    wins.append('Draw')
                else:
                    print('\nYou lose!')
                    print('Your value:', stat_u)
                    print('Computer value:', stat_c)
                    wins.append('Lose')

            elif stat_choice_input == 'height':
                stat_u = pokemon_choice['height']
                stat_c = stat_c_h
                if stat_u > stat_c:
                    print('\nYou win!')
                    print('Your value:', stat_u)
                    print('Computer value:', stat_c)
                    wins.append('Win')
                elif stat_u == stat_c:
                    print('\nDraw!')
                    wins.append('Draw')
                else:
                    print('\nYou lose!')
                    print('Your value:', stat_u)
                    print('Computer value:', stat_c)
                    wins.append('Lose')

            elif stat_choice_input == 'weight':
                stat_u = pokemon_choice['weight']
                stat_c = stat_c_w
                if stat_u > stat_c:
                    print('\nYou win!')
                    print('Your value:', stat_u)
                    print('Computer value:', stat_c)
                    wins.append('Win')
                elif stat_u == stat_c:
                    print('\nDraw!')
                    wins.append('Draw')
                else:
                    print('\nYou lose!')
                    print('Your value:', stat_u)
                    print('Computer value:', stat_c)
                    wins.append('Lose')

            else:
                replace = input('Incorrect value entered, please choose id, height, or weight ')
                find_stat(replace)

        find_stat(stat_choice_input)

    one_round()

    play_again_choice = input('\nWould you like to add another round? y or n? ')

    def play_again(play_again_choice):
        if play_again_choice == 'y':
            single_round()
        elif play_again_choice == 'n':
            print('\nThanks for playing!')
        else:
            replace_play_again = input('\nIncorrect value entered, please choose y or n ')
            play_again(replace_play_again)

    play_again(play_again_choice)


single_round()

for win in wins:
    if win == 'Win':
        i = i+1
    elif win == 'Draw':
        i = i+0.5
    else:
        i = i+0

if i/len(wins) > 0.5:
    print('You win overall!')
elif i/len(wins) == 0.5:
    print('You draw overall!')
else:
    print('You lose overall!')
