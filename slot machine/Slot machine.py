import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


def check_wining(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    return winnings, winnings_lines


def get_slot_machine_spint(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        myAmount = input('How much you want to deposit? ')
        if myAmount.isdigit():
            myAmount = int(myAmount)
            if myAmount > 0:
                break
            else:
                print('Amount must be greater than 0')
        else:
            print('Invalid Argument')
    return myAmount


def get_num_of_lines():
    while True:
        lines = input(f'Enter a number of lines to bet on (1 - {str(MAX_LINES)} )? ')
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print('Enter the valid numbers of lines.')
        else:
            print('Please enter a number')
    return lines


def get_bet():
    while True:
        amount = input('How would you like to bet on each line? $ ')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET < amount < MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}.')
        else:
            print('Please enter a number')

    return amount


def spin(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f" you dont have enough balance to bet that amount, your current balance is ${balance}")
        else:
            break
    print(f"you are betting ${bet} on {lines} lines.\nTotal Bet = {total_bet} ")
    slots = get_slot_machine_spint(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_wining(slots, lines, bet, symbol_value)
    print(f"You Won ${winnings}.")
    print(f"You won on ", *winnings_lines)
    return winnings- total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("press enter to play (q to quit).")
        if answer == 'q':
            break
        balance += spin(balance)
    print(f"you left with{balance}")


main()
