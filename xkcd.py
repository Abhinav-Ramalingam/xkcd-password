"""
Secure Computer Systems I [1DT072 HT24]

Lab 1 Task 3
"""

import sys
import random
from math import log2


def main():
    if len(sys.argv) != 3:
        print("Usage: python xkcd.py <wordlist_file> <number_of_words>")
        return

    wordlist_file = sys.argv[1]
    try:
        num_words = int(sys.argv[2])
        if num_words <= 0:
            print("Error: Number of words must be a positive integer.")
            return
    except ValueError:
        print("Error: Number of words must be a positive integer.")
        return

    # Choose `num_words` words from a wordlist and get the size of the wordlist
    (random_words, wordlist_length) = choose_random_words(wordlist_file, num_words)

    # Calculate the entropy of the generated password
    password_entropy = entropy_xkcd(num_words, wordlist_length)

    # Calculate how many random characters are needed to achieve the same entropy
    length_for_entropy = entropy_to_length(password_entropy)


    for w in random_words:
        print(w, end=' ')
    print()
    print(f"{num_words} RANDOM words from word list of {wordlist_length} words")
    print(f"Entropy: {password_entropy:.2f} bits")
    print(f"You need {length_for_entropy:.2f} RANDOM characters in [a-zA-Z0-9] to get the same entropy")



def choose_random_words(wordlist_file, num_words):
    try:
        with open(wordlist_file, 'r') as file:
            words = file.read().splitlines()
            wordlist_length = len(words)

        if len(words) == 0:
            print("Error: The wordlist file is empty.")
            return

        if num_words > len(words):
            print(f"Error: The wordlist only contains {len(words)} words.")
            return

        # Choose random words with replacement
        selected_words = random.choices(words, k=num_words)

        return (selected_words, wordlist_length)

    except FileNotFoundError:
        print(f"Error: File '{wordlist_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def entropy_xkcd(num_words: int, wordlist_size: int) -> float:
    """
    Calculate the entropy of a password assuming
    the use of xkcd generation method is known

    Params:
        num_words (int): the number of words making up the password
        wordlist_size (int): the size of the wordlist used in constructing the password
    Returns:
        The entropy of the password in bits
    """

    return num_words * log2(wordlist_size)



def entropy_to_length(E: float):
    """
    Calculate how many random characters from the set
    [a-zA-Z0-9] is needed in order to achieve a given entropy

    Params:
        E (float): The desired entropy
    Returns:
        (float): The number of random characters from [a-zA-Z0-9] needed to achieve entropy E
    """
    
    return E / log2(62)


if __name__ == "__main__":
    main()
