def gadget_cost(num_gadgets: int, label: str) -> float:
    """ computes cost, at $0.50 per gadget plus $0.05 per character in label """
    return num_gadgets * (0.50 + (len(label) * 0.05))
# Testing -- we'll come back to this

def add_shipping(order_amt: float) -> float:
    """ adds 4 for orders <= 10 (but non-zero), 8 for orders < 30, 12 for larger orders """
    if order_amt == 0:
        return 0
    elif order_amt <= 10:
        return order_amt + 4
    elif order_amt < 30:
        return order_amt + 8
    else:
        return order_amt + 12
# Testing -- we'll come back to this

