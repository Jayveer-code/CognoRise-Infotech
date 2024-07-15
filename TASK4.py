import random
word_list = ["python", "java", "kotlin", "javascript", "hangman", "programming"]
def get_random_word(word_list):
    return random.choice(word_list)
def display_initial_state(word):
    return ["_" for _ in word]
def get_user_input():
    return input("Guess a letter: ").lower()
def check_guess(word, guess, correct_guesses, incorrect_guesses):
    if guess in word:
        correct_guesses.add(guess)
    else:
        incorrect_guesses.add(guess)
    return correct_guesses, incorrect_guesses
def update_word_state(word, correct_guesses):
    return [letter if letter in correct_guesses else "_" for letter in word]
hangman_stages = [
    """
     ------
     |    |
          |
          |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
          |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    --------
    """
]

def display_hangman(incorrect_guesses):
    print(hangman_stages[len(incorrect_guesses)])
def check_win_loss(word, correct_guesses, incorrect_guesses):
    if set(word) <= correct_guesses:
        return "win"
    elif len(incorrect_guesses) >= len(hangman_stages) - 1:
        return "loss"
    return "continue"
def play_again():
    return input("Do you want to play again? (yes/no): ").lower().startswith('y')
def hangman_game():
    while True:
        word = get_random_word(word_list)
        correct_guesses = set()
        incorrect_guesses = set()
        word_state = display_initial_state(word)
        
        while True:
            print("Current word state: ", " ".join(word_state))
            display_hangman(incorrect_guesses)
            guess = get_user_input()
            
            correct_guesses, incorrect_guesses = check_guess(word, guess, correct_guesses, incorrect_guesses)
            word_state = update_word_state(word, correct_guesses)
            
            game_state = check_win_loss(word, correct_guesses, incorrect_guesses)
            if game_state == "win":
                print("Congratulations, you won! The word was:", word)
                break
            elif game_state == "loss":
                print("You lost! The word was:", word)
                display_hangman(incorrect_guesses)
                break
        
        if not play_again():
            break

# Run the game
hangman_game()
