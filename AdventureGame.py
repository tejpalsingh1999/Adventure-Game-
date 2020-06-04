import time
import random


def print_pause(string):

    print(string)
    time.sleep(2)


def intro(characters):

    print_pause('You find yourself standing in an open field,'
                ' filled with grass and yellow wildflowers.')
    print_pause('Rumor has it that a ' + characters + ' is somewhere around,'
                ' here and has been terrifying the nearby village.')
    print_pause('In front of you is a house.')
    print_pause('To your right is a dark cave.')
    print_pause('In your hand you hold your trusty '
                '(but not very effective) dagger.')
    print()


def field(player_with_weapon, characters, weapons):
    print('Enter 1 to knock on the door of the house.')
    print('Enter 2 to peer into the cave.')
    print('What would you like to do?')
    while True:
        response = input('(Please enter 1 or 2.)\n')
        if response == '1':
            house(player_with_weapon, characters, weapons)
        elif response == '2':
            cave(player_with_weapon, characters, weapons)
        else:
            print('Invalid Input')


def house(player_with_weapon, characters, weapons):
    print_pause('You approach the door of the house.')
    print_pause('You are about to knock when the door opens and'
                ' out steps a ' + characters)
    print_pause('Eep! This is the ' + characters + '\'s house!')
    print_pause('The ' + characters + ' attacks you!')
    if len(player_with_weapon) == 0:
        print_pause('You feel a bit under-prepared for this,'
                    ' what with only having a tiny dagger.\n')
    while True:
        print_pause('Would you like to (1) fight or (2) run away?')
        response = input()
        if response == '1':
            if len(player_with_weapon) >= 1:
                print_pause('As the ' + characters + ' moves to attack, '
                            ' you unsheath your new ' + weapons[0])
                print_pause('The ' + weapons[0] + ' of ' + weapons[1] +
                            ' shines brightly in your hand as you '
                            ' brace yourself for the attack.')
                print_pause('But the ' + characters + ' takes one '
                            'look at your shiny new toy and runs away!')
                print_pause('You have rid the town of the ' + characters +
                            '. You are victorious! \n')
                restart_game()
            else:
                print_pause('You do your best...')
                print_pause('but your dagger is no match '
                            'for the ' + characters)
                print_pause('You have been defeated!\n')
                restart_game()

        elif response == '2':
            print_pause('You run back into the field. Luckily,'
                        ' you don\'t seem to have been followed.')
            print()
            field(player_with_weapon, characters, weapons)
        else:
            print('INVALID INPUT')


def cave(player_with_weapon, characters, weapons):
    if len(player_with_weapon) >= 1:
        print_pause('You peer cautiously into the cave.')
        print_pause('You\'ve been here before, and gotten all '
                    'the good stuff. It\'s just an empty cave now')
        print_pause('.')
        print_pause('You walk back out to the field.\n')
        field(player_with_weapon, characters, weapons)

    else:
        print_pause('It turns out to be only a very small cave.')
        print_pause('Your eye catches a glint of metal behind a rock.')
        print_pause('You have found the ' + weapons[0] + ' of ' + weapons[1])
        print_pause('You discard your silly old dagger and '
                    'take the ' + weapons[0] + ' with you.')
        print_pause('You walk back out to the field.\n')
        player_with_weapon.append(weapons)
        field(player_with_weapon, characters, weapons)


def restart_game():
    while True:
        response = input('Would you like to play again? (y/n)\n')
        if response == 'y' or response == 'Y':
            print_pause('Excellent! Restarting the game ...\n')
            print()
            game()
        elif response == 'n' or response == 'N':
            print_pause('Thanks for playing! See you next time.')
            time.sleep(3)
            exit()
        else:
            print_pause('INVALID INPUT')


def game():
    player_with_weapon = []
    game_characters = ['Wicked Fairie', 'Aresok', 'Zaloruoznar', 'Onatnekou']
    characters = random.choice(game_characters)
    player_has_magical_weapon = [['Magical Sword', 'Dungeon Master'],
                                 ['Hammer', 'Thor'],
                                 ['Sheild', 'Captain America']]
    weapons = random.choice(player_has_magical_weapon)
    intro(characters)
    field(player_with_weapon, characters, weapons)
    restart_game()


game()
