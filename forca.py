import random

def game_opening():
    #game opening
    print("*********************************")
    print("***Welcome to the Forca game!****")
    print("*********************************")

def fruit_file_calling():
    #call to the fruit archive file and puting the content in words list
    archive = open("Fruits_list.txt", "r")
    fruits_list = []

    for line in archive:
        line = line.strip()
        fruits_list.append(line)

    archive.close()

    #number is the random position from word's list
    number = random.randrange(0, len(fruits_list))
    secret_word = fruits_list[number].upper()
    return secret_word

def start_right_tries(right_tries_word):
    return ["_" for letter in right_tries_word]   #set how many times "_" appears based on secret word lenght

def kick_receiver():
    kick = input("Type a letter: ")
    kick = kick.strip().upper()    #clean the user input
    return kick

def show_correct_kick(kick, right_tries, secret_word):
    index = 0   #position
    for letter in secret_word:
        if kick.upper() == letter.upper():
            right_tries[index] = letter
        index += 1

def game_ending():
    print("******************")
    print("Thanks for Playing")
    print("******************")

def print_winner_msg():
    print("Congratulatioins, you won!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_loser_msg(secret_word):
    print("Damn, you lost!")
    print("The word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def draw_forca(chances):
    print("  _______     ")
    print(" |/      |    ")

    if(chances == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(chances == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(chances == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(chances == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(chances == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(chances == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (chances == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def play_forca(): #main function, whom the code get linked himself
    exit_game = False
    while not exit_game:

        game_opening()
        secret_word = fruit_file_calling()
        
        right_tries = start_right_tries(secret_word)
        print(right_tries)
        
        loser = False
        winner = False
        chances = 0

        while not loser and not winner:
            
            kick = kick_receiver()

            if kick in secret_word:
                show_correct_kick(kick, right_tries, secret_word)
            else:
                chances += 1
                draw_forca(chances)

            loser = chances == 7    #if loser = true, end game
            winner = "_" not in right_tries    #if winner = true, game won
            print(right_tries)
        
        if winner:
            print_winner_msg()
        else:
            print_loser_msg(secret_word)

        game_ending()

        play_choice = int(input("Do you wanto to play again? 1 - YES  2 - NO  : "))
        if play_choice ==1:
            exit_game = False
        else:
            exit_game = True

if __name__ == " __main__":
    play_forca()
else:
    play_forca()