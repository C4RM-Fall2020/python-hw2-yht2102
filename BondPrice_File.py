import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):

    t = np.arange(1, m * ppy + 1)

    coupon = face * couponRate / ppy

    cf = np.full(m * ppy, coupon)
    cf[-1] += face

    pv = 1 / (1 + y / ppy) ** t

    x = np.sum(cf * pv)

    return(x)

print(getBondPrice(0.03, 2000000, 0.04, 10))
