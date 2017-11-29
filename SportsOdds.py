def odds(string):
    """You give sports odds (ie. 4/1, and it gives actual percent outputs)

    [
    runs through input string and picks up the numbers on both sides of bracket;
    is flexible, does not need the same input format, all it needs is numbers on both sides of a "/"
    ]

    Arguments:
        string {str} -- [input string containing the odds and includes two numbers separated by "/"]
    """
    nums = []
    build = ""
    i = 0
    for char in string:
        try:
            int(char)
            build += char
        except ValueError:
            if(char == "/"):
                nums.append(int(build.strip()))
                build = ""
        if(i == len(string) - 1):
            nums.append(int(build.strip()))
        i += 1

    return (nums[1] / (nums[0] + nums[1]))


def main():
    FedererOdds = "11  /           4"
    NadalOdds = "3/1  "
    DjokovicOdds = "7     /        2"
    MurrayOdds = DjokovicOdds
    fed = odds(FedererOdds)
    nad = odds(NadalOdds)
    djok = odds(DjokovicOdds)
    murr = odds(MurrayOdds)
    print("%f percent" % (fed * 100))
    print("%f percent" % (nad * 100))
    print("%f percent" % (djok * 100))
    print("%f percent" % (murr * 100))


main()
