import java.util.*;

public class Solution {

    private static boolean isSolvable(int m, int[] arr, int i) {
    if (i < 0 || arr[i] == 1) return false;
    if ((i == arr.length - 1) || i + m > arr.length - 1) return true;

    arr[i] = 1;
    return isSolvable(m, arr, i + 1) || isSolvable(m, arr, i - 1) || isSolvable(m, arr, i + m);
}
    public static boolean check(int[] game, int leap, int i, int j, int n,boolean wentBack) {
        if(j >= n-1 || i+1 > n-1 || i+leap > n-1){
            return true;
        }
        if(game[i+leap] != 1){
            return check(game,leap,i+leap,j+leap,n, false);
        }
        else if(game[i+1] != 1) {
            return check(game,leap,i+1,j+1,n,true);
        }
        else if((i-1) >= 0 && game[i-1] != 1 && wentBack == false) {
            return check(game,leap,i-1,j-1,n,true);
        } else {
            return false;
        }
    }

    public static boolean canWin(int leap, int[] game) {
        // Return true if you can win the game; otherwise, return false.
        int pos = 0;
        int n = game.length;
        while(pos<n) {
            // be greedy
            // don't want to go back to something already visited
            game[pos] = 1;
            if(pos == n-1 || (pos+1) >= n || (pos+leap) >= n) {
                return true;
            }
            else if(game[pos+leap] != 1) {
                pos = pos+leap;
            }
            else if(game[pos+1]!=1) {
                pos = pos + 1;
            }
            else if ((pos-1)>=0 && game[pos-1]!=1){
                pos = pos-1;
            } else {
                return false;
            }
        }
        return true;
        //return check(game,leap,0,leap,n, false);
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

            System.out.println( (isSolvable(leap, game,0)) ? "YES" : "NO" );
        }
        scan.close();
    }
}