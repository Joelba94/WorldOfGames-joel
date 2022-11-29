from forex_python.converter import CurrencyRates
import datetime
import random

def get_money_interval(difficulty, num):
    c = CurrencyRates()
    rate = 1 / c.get_rate('ILS', 'USD')
    total = num * rate
    return [total - (5 - int(difficulty)), total + (5 - int(difficulty))]


def get_guess_from_user(difficulty,num, num_range):
    user_input = float(input(f"Guess the amount of {num} USD in shekels, within {5 - int(difficulty)} shekels."))

    if num_range[0] <= float(user_input) <= num_range[1]:
        return True
    else:
        return False

def play(difficulty):
        usd = random.randint(1, 100)
        interval = get_money_interval(int(difficulty),usd)
        guess = get_guess_from_user(int(difficulty),usd, interval)
        return guess

