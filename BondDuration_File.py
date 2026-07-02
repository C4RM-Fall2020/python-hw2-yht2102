import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):

    t = np.arange(1, m * ppy + 1)

    coupon = face * couponRate / ppy

    cf = np.full(m * ppy, coupon)
    cf[-1] += face

    pv = 1 / (1 + y / ppy) ** t

    pvcf = cf * pv

    x = np.sum(t * pvcf) / np.sum(pvcf) / ppy

    return(x)
