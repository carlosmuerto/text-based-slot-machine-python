import random

MAX_LINES = 3

MIN_BET = 10
MAX_BET = 100

ROWS = 3
COLS = 3

SYMBOLS_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

SYMBOLS_VALUES = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                break
        else: # execute if no else
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    return winnings, winnings_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [] 
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

def pretty_str_columns(columns):
    return_str = ""
    for row in range(len(columns[0])):
        return_str += "\n" if return_str != "" else ""
        for i,column in enumerate(columns):
            pipe = " | " if i != len(columns) - 1 else ""
            return_str += f"{column[row]}{pipe}"

    return return_str

def deposit():
    while True:
        amout = input("What would you like to deposit? $")
        if amout.isdigit():
            amout = int(amout)
            if amout > 0:
                break
            else:
                print("Amout most be greater than 0.")
        else:
            print("Please enter a number")
    return amout

def get_number_of_line():
    while True:
        lines = input(f"Enter the nomber of line to bet on (1 - {MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid nomber of lines")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        bet = lines = input(f"what would you like to bet (${MIN_BET} to ${MAX_BET}) ? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amout must be between ${MIN_BET} to ${MAX_BET}.")
        else:
            print("Please enter a number")
    return bet

def main():
    balance = deposit()
    lines = get_number_of_line()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You dont have enoogh Balance (${balance}) for a bet of ${total_bet}")
        else:
            break

    print(f"you are betting ${bet} on {lines} lines.  total bet is ${total_bet}")
    slots = get_slot_machine_spin(ROWS,COLS,SYMBOLS_COUNT)
    # slots = [["A","A","A"],["B","A","A"],["A","A","A"]]
    print(pretty_str_columns(slots))
    winnings, winnings_lines = check_winnings(slots, lines, bet, SYMBOLS_VALUES)
    print(f"You won ${winnings}.")
    print(f"You won on lines:",*winnings_lines)

if __name__ == "__main__":
    main()