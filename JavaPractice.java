// use of static initialization blocks for more complex initialization
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class StaticInit {


    static Scanner sc = new Scanner(System.in);
    static int B = sc.nextInt();
    static int H = sc.nextInt();
    static boolean flag = true;
    static { // initializer block
        if (B <= 0 || H <= 0) {
            System.out.println("java.lang.Exception: Breadth and height must be positive");
            flag = false;
        }

    }
    public static void main(String[] args) {
        if (flag) {
            int area = B * H;
            System.out.print(area);
        }

    }//end of main

}//end of class


/*-------------------------------------------------------------------------------------*/
int n = 12;
String s = Integer.toString(n); // casts to string as name suggests

/*-------------------------------------------------------------------------------------*/

public class DynamicArrays {

    public static void main(String[] args) throws IOException {
        /* pretty much creating an adjacency list*/
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int n0;

        ArrayList<ArrayList<Integer>> adj = new ArrayList<ArrayList<Integer>>(n);

        for (int i = 0; i < n; i++) {
            n0 = sc.nextInt();
            ArrayList<Integer> sub = new ArrayList<Integer>(n0);
            for (int j = 0; j < n0; j++) {
                sub.add(sc.nextInt());
            }
            adj.add(sub);
        }
        //Debug:
        //System.out.println(adj);

        int q = sc.nextInt(); // # of querries
        int y, x;
        for (int i = 0; i < q; i++) {
            y = sc.nextInt();
            x = sc.nextInt();
            try {
                System.out.println(adj.get(y - 1).get(x - 1));
            } catch (IndexOutOfBoundsException e) {
                System.out.println("ERROR!");
            }
        }
    }
}