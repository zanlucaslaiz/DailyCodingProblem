"""
EASY

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish 
this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""

class Order():
    def __init__(self):
        self.orderId = []

    def record(self, order_id):
        self.orderId.append(order_id)

    def get_last(self, i):
        return self.orderId[len(self.orderId) - 1 - i]

if __name__ == "__main__":
    eCommerceOrder = Order()
    for i in range(1, 101):
        eCommerceOrder.record(i)
    
    print(eCommerceOrder.get_last(10)) 
    print(eCommerceOrder.get_last(50))     