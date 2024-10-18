balance = 3000

def buy(item, price):
    global balance
    print(f'balance before buying {item}', balance)
    balance -= balance - price
    print(f'balance after buying {item}', balance)

buy("Watch", 1000)