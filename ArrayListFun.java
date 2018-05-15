/*input
10
48908 99556 51237 37007 96350 9826 11431 62869 50411 83719
10
Delete
2
Insert
4 36173
Insert
6 79735
Delete
3
Delete
0
Insert
4 98904
Delete
9
Insert
2 2073
Delete
0
Delete
5
*/
import java.io.*;
import java.util.*;

public class ArrayListFun {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in).useDelimiter("\\s");
        int N = sc.nextInt();
        ArrayList < Integer > a = new ArrayList < Integer > (N);
        int next;
        String query;
        int x, y;
        for (int i = 0; i < N; i++) {
            next = sc.nextInt();
            a.add(i,next);
        }
        int Q = sc.nextInt();
        System.out.println(Q);
        for (int i = 0; i < Q; i++) {
                query = sc.next();
                x = sc.nextInt();
                if (query.equals("Insert")) {
                    y = sc.nextInt();
                    if (x >= a.size()) {
                        a.add(y);
                    } else {
                        a.add(x, y);
                    }

                } else {

                    a.remove(x);
                }
        }
        for(int el: a) {
            System.out.print(el + " ");
        }
    }
}