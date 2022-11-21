HANGMAN_PHOTOS = {}  # A dict for hangman photos
MAX_TRIES = 6  # The max number of failed attempts to guess the secret word


def print_opening_page():
    """This function prints the welcome page"""
    global MAX_TRIES  # The max num of failed attempts of guessing secret word
    print("Welcome to the game Hangman")
    print("""      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/""")
    print("\n" + str(MAX_TRIES))


def check_valid_path(path_file):
    """
    This function checks that path file is exists.
    :param path_file: path file of words list
   :type path_file: string
   :return: isValid
   :rtype: bool
    """
    from pathlib import Path
    path = Path(path_file)  # Change the path file into a Path class
    if path.is_file():  # Method returns bool if the file is exists
        return True
    else:
        print("The file doesn't exist")
        return False


def check_valid_index(index):
    """
    This function checks that word index is valid.
    :param index: secret word index
   :type index: string
   :return: isValid
   :rtype: bool
    """
    if index.isnumeric():  # Method returns bool if the index is num
        return True
    else:
        print("The index is not a number")
        return False


def check_win(secret_word, old_letters_guessed):
    """
    The function checks if the user is win.
    :param secret_word: the secret word
    :type secret_word: string
    :param old_letters_guessed: the old letters guessed list
    :type old_letters_guessed: list
    :return: secret word contains the correct old letters
    :rtype: bool
    """
    for char in secret_word:  # Scanning every letter in the secret word
        if char in old_letters_guessed:  # Checking current letter in the  list
            continue  # if not continue to the next letter in the secret word
        else:  # if not stop the scanning loop and return False
            return False
    return True


def show_hidden_word(secret_word, old_letters_guessed):
    """
    This function shoes the secret word status
    :param secret_word: the word which the player has to guess
    :type secret_word: string
    :param old_letters_guessed: list of the guess letters
    :type old_letters_guessed: list
    :return: secret word with the correct old letters
    :rtype: string
    """
    word_with_guessed_letters = ""
    for char in secret_word:  # If char is an old letter than insert to str
        if char in old_letters_guessed:
            word_with_guessed_letters = word_with_guessed_letters + char
        else:
            word_with_guessed_letters = word_with_guessed_letters + "_"
    word_with_guessed_letters = " ".join(word_with_guessed_letters)  # Add s
    return word_with_guessed_letters


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    This function checks that string is valid
    :param letter_guessed: the current guess of the user
   :type letter_guessed: string
   :param old_letters_guessed: list of old guessed letters
   :return: isValid
   :rtype: bool
    """
    import string
    letter_guessed = letter_guessed.lower()
    if letter_guessed in string.ascii_letters and len(letter_guessed) == 1 and letter_guessed not in old_letters_guessed:
        return True
    else:
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    This function checks letter_guessed is valid and updates the list if true
    :param letter_guessed: the current guess of the user
    :type letter_guessed: string
    :param old_letters_guessed: list of  letters which the user already guessed
    :type old_letters_guessed: list
    :return: isValid
    :rtype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        old_letters_guessed.sort()  # sorted old letters with -> between them.
        print("X\n" + " -> ".join(old_letters_guessed))
        return False


def insert_hangman_photos():
    """
    The function returns dict with hangman with photos
    return: a dict with photos
    :rtype: dict
    """
    str0 = "    x-------x"

    str1 = """    x-------x
        |
        |
        |
        |
        |"""

    str2 = """    x-------x
        |       |
        |       0
        |
        |
        |"""

    str3 = """    x-------x
        |       |
        |       0
        |       |
        |
        |"""

    str4 = """    x-------x
        |       |
        |       0
        |      /|\\
        |
        |"""

    str5 = """    x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |"""

    str6 = """    x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |"""

    hangman_photos = {0: str0, 1: str1, 2: str2, 3: str3, 4: str4, 5: str5, 6: str6}
    return hangman_photos


def print_hangman(num_of_tries):
    """
    The function gets number trials and returns the Hangman photo by its value
    :param num_of_tries: number of trials
    :type num_of_tries: int
    """
    global HANGMAN_PHOTOS
    HANGMAN_PHOTOS = insert_hangman_photos()
    print(HANGMAN_PHOTOS[num_of_tries] + "\n")


def choose_word(file_path, index):
    """
    Function gets path file, index, and returns the secret word ine index place
    :param file_path: file path
    :type file_path: str
    :param index: index of secret word in file
    :type index: int
    :return: the secret word
    :rtype: str
    """
    with open(file_path, "r") as file_path_input_file:  # Opening word list
        words_list = str(file_path_input_file.read()).split(" ")
    for word in words_list:  # Cleaning the \n from every word
        word = word.strip("\n")
    if index - 1 >= len(words_list):  # If index not in range
        index = index % len(words_list)
    chosen_word = words_list[index - 1]  # Return secret word by index
    return chosen_word


def hangman(secret_word):
    """
    This function gets the secret words and manages the game
    :param secret_word: the secret word
    :type secret_word: str
    """
    global MAX_TRIES  # The max number of failed attempts to guess secret word
    num_of_tries = 0  # The current number of failed attempts
    old_letters_guessed = []  # The list of old guesses
    is_win = False  # Checks lose or win status
    check_valid = True  # Check validation of letter guessed
    print_hangman(num_of_tries)  # Print the current hangman picture
    print(show_hidden_word(secret_word, old_letters_guessed) + "\n")
    while (num_of_tries < MAX_TRIES) and (is_win is False):
        letter_guessed = input("Guess a letter:")
        check_valid = try_update_letter_guessed(letter_guessed, old_letters_guessed)
        if check_valid is True:
            if letter_guessed in secret_word:
                print(show_hidden_word(secret_word, old_letters_guessed) + "\n")
            else:  # Change the nums of tries in more failed attempt
                print(":(\n")
                num_of_tries += 1
                print_hangman(num_of_tries)  # Print the current picture
                print(show_hidden_word(secret_word, old_letters_guessed) + "\n")
        is_win = check_win(secret_word, old_letters_guessed)  # Checks win
    if MAX_TRIES == num_of_tries:  # If it is last attempt
        print_hangman(num_of_tries)  # Print the current hangman picture
        print(show_hidden_word(secret_word, old_letters_guessed) + "\n")
        print("LOSE")
    elif is_win is True:  # else print "WIN"
        print("WIN")


def main():
    print_opening_page()  # Printing the welcome page
    exits_file = False
    while exits_file is False:  # Checking is the path file is exits
        words_file_path = input("\nEnter file path:")
        exits_file = check_valid_path(words_file_path)
    valid_secret_word_index = False
    while valid_secret_word_index is False:  # Checking index is num
        secret_word_index = input("\nEnter index:")
        valid_secret_word_index = check_valid_index(secret_word_index)
    secret_word = choose_word(words_file_path, int(secret_word_index))
    print("\nLet’s start!")
    hangman(secret_word)  # Playing the game using the main method


if __name__ == "__main__":
    main()
