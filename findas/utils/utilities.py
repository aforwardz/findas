
# 万2.5
FEE_RATE = 0.00025


def deduct_fee(trans_value):
    return max(trans_value * FEE_RATE, 5)
