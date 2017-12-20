import java.util.*;

public class Solution {

    private static boolean isSolvable(int m, int[] arr, int i) {
        if (i < 0 || arr[i] == 1) return false;
        if ((i == arr.length - 1) || i + m > arr.length - 1) return true;

        arr[i] = 1;
        return isSolvable(m, arr, i + 1) || isSolvable(m, arr, i - 1) || isSolvable(m, arr, i + m);
    }

    public static boolean canWin(int leap, int[] game) {
        // Return true if you can win the game; otherwise, return false.
        int pos = 0;
        int n = game.length;
        while (pos < n) {
            // be greedy
            // don't want to go back to something already visited
            // This solution doesn't work for one reason:
            // YOU ARE ONLY CHECKING ONE ROUTE
            // Say you leap forward by leap spaces, then you cannot go any farther in the array
            // you are done, but there may have been a solution if you first leap by 1 and then leaped by leap
            // very inflexible
            game[pos] = 1;
            if (pos == n - 1 || (pos + 1) >= n || (pos + leap) >= n) {
                return true;
            } else if (game[pos + leap] != 1) {
                pos = pos + leap;
            } else if (game[pos + 1] != 1) {
                pos = pos + 1;
            } else if ((pos - 1) >= 0 && game[pos - 1] != 1) {
                pos = pos - 1;
            } else {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();

            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println( (isSolvable(leap, game, 0)) ? "YES" : "NO" );
        }
        scan.close();
    }
}
