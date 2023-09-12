import random
import time

class TradingEngine:
    def __init__(self):
        self.balance = 10000000 
        self.position = 0     
        self.price = 100     

    def run(self):
        while True:
            signal = random.choice(['buy', 'sell'])
            quantity = random.randint(1, 10) 

            if signal == 'buy':
                cost = quantity * self.price
                if cost <= self.balance:
                    self.balance -= cost
                    self.position += quantity
                    print(f'Bought {quantity} shares at ${self.price} each.')
                else:
                    print('Insufficient balance to buy.')

            elif signal == 'sell':
                if self.position >= quantity:
                    revenue = quantity * self.price
                    self.balance += revenue
                    self.position -= quantity
                    print(f'Sold {quantity} shares at ${self.price} each.')
                else:
                    print('Insufficient position to sell.')

            time.sleep(1)  

if __name__ == '__main__':
    trading_engine = TradingEngine()
    trading_engine.run()
