def Code_Printer(N):
    for i in range(1, N):
        if(i == 1):
            print(
                "BUFA_TEST bufftest1prev[48:0] (.A(Psri_p[48:0]),.Y(Psri_pb1[48:0]));")
            print(
                "BUFA_TEST bufftest1[48:0] (.A(Psri[48:0]),.Y(Psri_b1[48:0]));")
            print(
                "BUFA_TEST bufftest1next[48:0] (.A(Psri_n[48:0]),.Y(Psri_nb1[48:0]));")
            print("")
        else:
            print(
                "BUFA_TEST bufftest%dprev[48:0] (.A(Psri_pb%d[48:0]),.Y(Psri_pb%d[48:0]));" % (i, i - 1, i))
            print(
                "BUFA_TEST bufftest%d[48:0] (.A(Psri_b%d[48:0]),.Y(Psri_b%d[48:0]));" % (i, i - 1, i))
            print(
                "BUFA_TEST bufftest%dnext[48:0] (.A(Psri_nb%d[48:0]),.Y(Psri_nb%d[48:0]));" % (i, i - 1, i))
            print("")


if __name__ == '__main__':
    print("wire [48:0] " + ",".join(["Psri_pb%d, Psri_b%d, Psri_nb%d" %
                                     (i, i, i) for i in range(1, 12)]) + ";")
    print("")
    Code_Printer(12)
