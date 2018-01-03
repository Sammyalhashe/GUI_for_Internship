/*input
5
1 2 3 4 5
7
5 9 1 3 6 1 9
9
34 2 6 1 3 4 5 6 3
1
5
*/
import java.util.*;
import java.io.*;
/////////////////
// DP Solution //
/////////////////

class LongestQuasi {

    public static int getAmp(int[] array) {
        if (array.length == 0) {
            return 0;
        } else {
            return (array[array.length - 1] - array[0]);
        }
    }
    public static boolean isQuasi(int[] array) {
        if (getAmp(array) < 2) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        /**
         * Used to take in STDIN
         * @param  System.in Standard input
         * @return           new Scanner() object
         */
        Scanner sc = new Scanner(System.in);

        /**
         * Run for all inputs in STDIN
         */
        while (sc.hasNextLine()) {



            int n = sc.nextInt();
            int [] testArray = new int[n];
            for (int i = 0; i < n; i++) {
                testArray[i] = sc.nextInt();
            }

            System.out.println(Arrays.toString(testArray));

            Arrays.sort(testArray);

            /**
             * Really unnecessary but done anyways
             */
            int[][] A = new int[n][n];

            ////////////////
            // Base Cases //
            ////////////////

            /**
             * Subarrays of length 1 have longest quasi length of 1
             */

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (i == j) {
                        A[i][j] = 1;
                    }
                }
            }

            /////////////////////
            // DP Step Through //
            /////////////////////

            int i = 0;
            int j = 1;
            int maximum = 1;
            while (j < n && i <= j) {
                if (isQuasi(Arrays.copyOfRange(testArray, i, j))) {
                    A[i][j] = Arrays.copyOfRange(testArray, i, j).length;
                    if (maximum < A[i][j]) {
                        maximum = A[i][j];
                    }
                    j++;
                } else {
                    A[i][j] = A[i][j - 1];
                    i++;
                }
            }

            System.out.println(maximum);
        }
        ///////////////////////
        // Close the Scanner //
        ///////////////////////
        sc.close();
    }
}
