import random
import os
import time

def generate_sequence(difficulty):
    sequence=random.sample(range(1, 100), int(difficulty))
    return sequence

def get_list_from_user(difficulty):
    user_input = input('Enter numbers separated by space ')
    print("\n")
    user_list = user_input.split()
    # convert each item to int type
    for i in range(len(user_list)):
        # convert each item to int type
        user_list[i] = int(user_list[i])
    return user_list

def is_list_equal(sequence,user_input):
    if sequence==user_input:
        return True
    else:
        return False

def play(difficulty):
    input(f"you will see a {difficulty} numbers, you need to remember it and enter again press enter to start")
    sequence=generate_sequence(difficulty)
    print(sequence)
    time.sleep(0.7)
    os.system('cls')
    user_input=get_list_from_user(difficulty)
    result=is_list_equal(sequence,user_input)
    return result

