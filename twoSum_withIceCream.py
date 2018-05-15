'''input
"2"
"4"
"5"
"1 4 5 3 2"
"4"
"4"
"2 2 4 3"
'''


class tuples2:

    def __init__(self, val1, val2):
        self.tupl = (val1, val2)

    def comparitor(self):
        return self.tupl[1]


t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))

    # This next line is messy (I know), but what it does is takes the array, a, and then turns it into a sorted array
    # based on the price value (the second value in the enumeration) and places the result into a 2 valued tuple object I created.
    # To sort, it uses python's sorting function and sorts based on the price value (key takes a function of one paramater, in this
    # case comparitor, and applies it to all elements in the list and sorts based on the result). The comparitor returns the second
    # value of the tuple (the price). I then take that sorted array of tuple2
    # objects, and make it look nicer.
    final = list(map(lambda x: x.tupl, sorted(
        [tuples2(i, j) for i, j in enumerate(a)], key=tuples2.comparitor)))

    # Logic: Greedy Algorithm
    # 1) Choose the largest priced item first, if it's too large, remove it as an option
    # 2) If I haven't bought anything yet, try to buy one and see if you have an exact amount of money left for one of the items left
    #   if you don't remove it as an option
    # 3) Otherwise, buy an item and subtract from the money you have available
    bought = 0
    ice_cream = []
    while m > 0 or bought != 2:
        if(final != []):
            if(m < final[-1][1]):
                final.pop()
            else:
                # Theoretically buy an ince-cream, if you can't buy anything
                # else after you bought the current one you shouldn't have
                # bougthen it in the first place
                if(len(list(filter(lambda x: x[1] == m - final[-1][1], final[:len(final) - 1]))) == 0 and bought == 0):
                    final.pop()
                else:
                    m -= final[-1][1]
                    bought += 1
                    # plus 1 due to indexing
                    ice_cream.append(str(final[-1][0] + 1))
                    final.pop()  # pop because we choose distinct flavours and not the same multiple times: remove the option
        else:
            print("No two sum solution")
            break

    print(" ".join(sorted(ice_cream, key=lambda x: int(x))))
