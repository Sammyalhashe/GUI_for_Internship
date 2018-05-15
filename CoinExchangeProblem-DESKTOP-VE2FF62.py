"""
Problem:
Given an amount, A, and a set of coin
denokminations,
d = [d1,d2,d3,d4,d5,...dn]
Task is to give an optimum list of coins,
C = [c1,c2,c3,...] s.t. A = c[1]+c[2]+c[3]+...
Note: Penny is necessary to solve this problem, so it will be in the list of denominations passed in
"""

try:
    from sys import maxsize
except ImportError as I:
    print(I)


def CoinExchange(A, d):
    """
    @brief      DP solution of the Coin Exchange problem.
    Logic:
    1) Define 2D array N[i,j] = optimum # of coins for sum i, considering up to denomination, j.
    2) Base Cases:
        a) N[0,j] = 0
        b) N[i,0] = Inf
    3) Cycle through all values of i, j: {i = 0...A; j = 0...len(d)}, filling up N. The answer to the question is the last value: N[A,n = len(d)]
    4) Recurrence:
    N[i,j] = N[i,j-1] if d[j]>i else min(N[i,j-1],N[i-d[j],j]+1) -> d[j] does not necessarily have to be in the result!

    @param      A     { amount to add to }
    @param      d     { list of coin denominations -> should be sorted }

    @return     { optimum number of coins to sum to A }
    """

    # Make sure the denominations are sorted:
    denoms = sorted(d)

    # Create array, N[A,len(d)]
    N = [[0 for j in range(len(denoms))] for i in range(A + 1)]

    # Keep a running index of coins chosen from sorted d
    C = []

    # Load base cases
    for i in range(A + 1):
        for j in range(len(denoms)):
            N[0][j] = 0  # Unnecesary bt just for show
            N[i][0] = maxsize

    for i in range(1, A + 1):
        for j in range(1, len(denoms)):
            N[i][j] = N[i][j - 1] if (denoms[j] > i) else min(N[i]
                                                              [j - 1], N[i - d[j]][j] + 1)
    # get coins used: (check if the optimal number of coins changes when cycling through the denoms considered for the same sum)
    i = A
    j = len(d) - 1
    while j >= 0 and i > 0:
        if N[i][j] == N[i][j - 1]:
            # didn't use this coin
            j = j - 1
        else:
            C.append(d[j])
            i -= denoms[j]

    return (N[A][len(d) - 1], C)


if __name__ == '__main__':
    denoms = [1, 2, 3, 5, 6, 10, 15]
    Amount = 34
    opt, coins = CoinExchange(Amount, denoms)
    print("For sum to %d, with these denominations offered: %s, the optimum number of coins: %d, with these coins chosen: %s" %
          (Amount, str(' '.join(list(map(lambda x: str(x), denoms)))), opt, str(' '.join(list(map(lambda x: str(x), coins))))))
