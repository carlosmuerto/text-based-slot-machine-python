import rendom

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

if __name__ == "__main__":
    main()