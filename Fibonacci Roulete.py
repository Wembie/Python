import random

fib = [ 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ]

def win_chance():
    return random.random() < 0.48

def fibonacci_strategy( bankroll, bet_size, win_chance ):
    index = 0
    while bankroll >= bet_size and index < len( fib ):
        bet_size = fib[ index ]
        if bet_size > bankroll:
            break
        if win_chance():
            bankroll += bet_size
            index = 0
        else:
            bankroll -= bet_size
            index += 1
    return bankroll

bankroll = sum( fib )
bet_size = 1
result = fibonacci_strategy( bankroll, bet_size, win_chance )
print( "El saldo final de la banca es:", result, "Cuando llegaste tenias:", sum( fib ) )
