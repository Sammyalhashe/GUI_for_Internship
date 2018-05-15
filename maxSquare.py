
def maxSquare(matrix):
    largest_area = 1
    for i in range(len(matrix[0]) - 1):  # don't care about last row
        one_count = 0
        print("on level %d" % i)
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                one_count += 1
                print("  encountered 1: %d" % one_count)
            else:
                one_count = 0  # reset
                print("  reset: %d" % one_count)
            if one_count <= len(matrix) and one_count > largest_area:
                print("  checking levels")
                for x in range(i + 1, one_count):
                    print("    checking level %d" % x)
                    if not all(matrix[x][j - one_count + 1:j + 1]):
                        print("    non square, breaking")
                        one_count = 0
                        break
                largest_area = one_count if one_count != 0 else largest_area
                print("  largest_area: %d" % largest_area)
    return largest_area


if __name__ == '__main__':
    test = [[1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 1]]
    ret = maxSquare(test)
    print(ret)
