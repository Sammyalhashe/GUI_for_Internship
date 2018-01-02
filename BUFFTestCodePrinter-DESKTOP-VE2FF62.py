<<<<<<< HEAD
def Code_Printer(N, buff):
    for i in range(1, N):
        if(i == 1):
            print(
                "BUF%s_TEST bufftest1prev[48:0] (.A(Psri_p[48:0]),.Y(Psri_pb1[48:0]));" % (buff))
            print(
                "BUF%s_TEST bufftest1[48:0] (.A(Psri[48:0]),.Y(Psri_b1[48:0]));" % (buff))
            print(
                "BUF%s_TEST bufftest1next[48:0] (.A(Psri_n[48:0]),.Y(Psri_nb1[48:0]));" % (buff))
            print("")
        else:
            print(
                "BUF%s_TEST bufftest%dprev[48:0] (.A(Psri_pb%d[48:0]),.Y(Psri_pb%d[48:0]));" % (buff, i, i - 1, i))
            print(
                "BUF%s_TEST bufftest%d[48:0] (.A(Psri_b%d[48:0]),.Y(Psri_b%d[48:0]));" % (buff, i, i - 1, i))
            print(
                "BUF%s_TEST bufftest%dnext[48:0] (.A(Psri_nb%d[48:0]),.Y(Psri_nb%d[48:0]));" % (buff, i, i - 1, i))
            print("")


if __name__ == '__main__':
    N = 2
    buff = "A"
    print("wire [48:0] " + ", ".join(["Psri_pb%d, Psri_b%d, Psri_nb%d" %
                                      (i, i, i) for i in range(1, N)]) + ";")
    print("")
    Code_Printer(N, buff)
=======
def Code_Printer(N, buff):
    for i in range(1, N):
        if(i == 1):
            print(
                "BUF%s_TEST bufftest1prev[48:0] (.A(Psri_p[48:0]),.Y(Psri_pb1[48:0]));" % (buff))
            print(
                "BUF%s_TEST bufftest1[48:0] (.A(Psri[48:0]),.Y(Psri_b1[48:0]));" % (buff))
            print(
                "BUF%s_TEST bufftest1next[48:0] (.A(Psri_n[48:0]),.Y(Psri_nb1[48:0]));" % (buff))
            print("")
        else:
            print(
                "BUF%s_TEST bufftest%dprev[48:0] (.A(Psri_pb%d[48:0]),.Y(Psri_pb%d[48:0]));" % (buff, i, i - 1, i))
            print(
                "BUF%s_TEST bufftest%d[48:0] (.A(Psri_b%d[48:0]),.Y(Psri_b%d[48:0]));" % (buff, i, i - 1, i))
            print(
                "BUF%s_TEST bufftest%dnext[48:0] (.A(Psri_nb%d[48:0]),.Y(Psri_nb%d[48:0]));" % (buff, i, i - 1, i))
            print("")


if __name__ == '__main__':
    N = 12
    buff = "A"
    print("wire [48:0] " + ", ".join(["Psri_pb%d, Psri_b%d, Psri_nb%d" %
                                      (i, i, i) for i in range(1, N)]) + ";")
    print("")
    Code_Printer(N, buff)
>>>>>>> 3baf57ceecff4eee51d0142a2791cab22e0a7317
