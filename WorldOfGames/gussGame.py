import random

def generate_number(difficulty):
    secret_number=random.randint(1,int(difficulty))
    return secret_number

def get_guess_from_user(difficulty):
    user_input = input(f"Choose a number between 1 and {difficulty}.")
    return user_input

def compare_results(secret_number,user_input):
    if int(secret_number)==int(user_input):
        return True
    else:
        return False

def play(difficulty):
   secretnumber=generate_number(difficulty)
   user_input=get_guess_from_user(difficulty)
   result=compare_results(secretnumber,user_input)
   return result
