liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

def getAmount(A, balenceA, balenceB):
    B = 997 * A/(1000 * balenceA + 997 * A) * balenceB
    return B

tokenB = 5
tokenA = getAmount(tokenB, liquidity[("tokenA", "tokenB")][1], liquidity[("tokenA", "tokenB")][0])
tokenE = getAmount(tokenA, liquidity[("tokenA", "tokenE")][0], liquidity[("tokenA", "tokenE")][1])
tokenD = getAmount(tokenE, liquidity[("tokenD", "tokenE")][1], liquidity[("tokenD", "tokenE")][0])
tokenC = getAmount(tokenD, liquidity[("tokenC", "tokenD")][1], liquidity[("tokenC", "tokenD")][0])
tokenB = getAmount(tokenC, liquidity[("tokenB", "tokenC")][1], liquidity[("tokenB", "tokenC")][0])
print("path: tokenB->tokenA->tokenE->tokenD->tokenC->tokenB, tokenB balance="+str(tokenB))