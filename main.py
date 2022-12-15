
from random import randint

random_digits = ''
lucky_num = []
random_int = str(randint(a=0, b=9))

def isUnique(num):              #we create this func to check if user input has a repeating digits
    number = str(num)           #convert provided num to string
    numberSet = set(number)
    return len(number) == len(numberSet)

def add_num():                  #we create this function to generate 3 random numbers and add them to a list than use built-in funcion join() to convert them into string
    added_nums = 0
    while added_nums < 3:
        random_int = str(randint(a=0, b=9))
        if random_int not in lucky_num:
            lucky_num.append(random_int)
            added_nums += 1
        else:
            continue
    global random_digits
    random_digits = ''.join(lucky_num)

max_guesses = 10        #we set max guesses to 10

def note():
    note = """I am thinking of a 3-digit number. Try to guess what it is PS: there's no repeating digits.
    Here are some clues:
    When I say: That means:
        Pico        One digit is correct but in the wrong position.
        Fermi       One digit is correct and in the right position.
        Bagels      No digit is correct.
    I have thought up a number.
    You have 10 guesses to get it. Good luck!
    """
    print(note, end=" ")

def guess():
    u = 0
    n = 0
    guessed = False
    bagels = True      #we create this var to know if we have a bagels situation or not. we set it to True cuz we don't know yet if we have a correct number.
    guesses = 1
    
    while(guesses <= max_guesses):
        
        print(f"\nGuess #{guesses}")
        global user_input
        user_input = str(input('> '))
        if user_input.isdigit() and len(user_input) == 3 and isUnique(user_input) is True:      #user input should respect this guidelines to play the game
            if user_input == random_digits:
                print("You got it!")
                guessed = True
                break
            while u < 3 and n < 3:
                if user_input[u] == random_digits[n]:
                        print("fermi", end=" ")
                        bagels = False         #set bagels to False because we have a correct number in the right position.
                else:
                    if user_input[u] in random_digits:       #we check if current number is in our lucky number, so we print pico
                        print("pico", end=" ")
                        bagels = False     #set bagels to False because we have a correct number but in the wrong position.
                u += 1
                n += 1                  #we increase n and u by 1 to compare the numbers in the second position
            u = 0
            n = 0                     
            if bagels == True:         
                print("Bagels", end=' ')         #we print bagels cuz we don't have any correctly guessed number
            else:
                bagels = True
            guesses += 1
        else:
            print("invalid input, try again!")
            continue
    if guessed != True:
        print(f"\nYou lost! the lucky number was: {random_digits}")
    print("\nDo you want to play again? (yes or no)")
    play_again = input('> ')
    if play_again == 'yes':
        lucky_num.clear()       #we use built-in func clear() to clear value of lucky_num var so we make sure old 3-digit number are gone, cuz we need a new 3-digit number.
        add_num()
        guess()
    else:
        print("Thanks for playing!")
        pass

add_num()
note()
guess()
