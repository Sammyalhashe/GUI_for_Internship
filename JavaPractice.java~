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

/*-------------------------------------------------------------------------------------*/

// Comparator usage:

class Checker implements Comparator<Player> {

    /**
     * [Implments the comparator interface -> its compare method used]
     * @param  a [player a]
     * @param  b [player b]
     * @return   [If player a's score is greater than player b's -> return a negative number to sort in ascedning order. Else, compare the names]
     */
    @Override

    ////////////////////////////////////////////////////////////
    // @Override decorator to override the interface function //
    ////////////////////////////////////////////////////////////
    public int compare(Player a, Player b) {
        int scorediff = b.score - a.score;
        if (scorediff != 0) {
            return (scorediff);
        } else {
            return a.name.compareTo(b.name);
        }
    }
}

class Player {

    String name;
    int score;

    Player(String name, int score) {
        this.name = name;
        this.score = score;
    }
}

class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        Player[] player = new Player[n];

        Checker checker = new Checker();

        for (int i = 0; i < n; i++) {
            player[i] = new Player(scan.next(), scan.nextInt());
        }
        scan.close();

        Arrays.sort(player, checker);
        for (int i = 0; i < player.length; i++) {
            System.out.printf("%s %s\n", player[i].name, player[i].score);
        }
    }
}

/*-------------------------------------------------------------------------------------*/

// Priority Queue in Java
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.*;

class Student {

    ///////////////////
    // Private Vars  //
    ///////////////////
    private int __id;
    private String __name;
    private double __cgpa;

    /////////////////
    // Constructor //
    /////////////////

    /**
     * Contains id, name, and cgpa
     * @param  id   [# id of student]
     * @param  name [String name]
     * @param  cgpa [double cgpa]
     */
    public Student(int id, String name, double cgpa) {
        this.setID(id);
        this.setName(name);
        this.setCGPA(cgpa);
    }

    //////////////////////////
    // Getters and Setters  //
    //////////////////////////

    public int getID() {
        return (this.__id);
    }

    public void setID(int id) {
        this.__id = id;
    }

    public String getName() {
        return (this.__name);
    }

    public void setName(String name) {
        this.__name = name;
    }

    public double getCGPA() {
        return (this.__cgpa);
    }

    public void setCGPA(double cgpa) {
        this.__cgpa = cgpa;
    }
}


class myComp implements Comparator<Student> {
    @Override
    public int compare(Student a, Student b) {
        if (a.getCGPA() > b.getCGPA()) {
            return 1;
        } else if (a.getCGPA() == b.getCGPA()) {
            if (a.getName().compareTo(b.getName()) > 0) {
                return -1;
            } else if (a.getName().compareTo(b.getName()) == 0) {
                if (a.getID() > b.getID()) {
                    return -1;
                }
            }
        }
        return 0;
    }
}


class Priorities {

    //////////////////
    // Private Vars //
    //////////////////

    private List<Student> __heap;
    private int size;

    /////////////////
    // Constructor //
    /////////////////

    public Priorities() {
        this.setHeap();
    }

    ////////////////////////////////
    // Getter and Setter for Heap //
    ////////////////////////////////
    public List<Student> getHeap() {
        return (this.__heap);
    }

    public void setHeap() {
        Student init = new Student(0, "0", 0.0); // dummy student
        this.__heap = new ArrayList<Student>();
        this.__heap.add(0, init);
        this.size = 0;

    }

    ///////////
    // Swap  //
    ///////////

    /**
     * Swaps heap elements at indices i1 and i2
     * @param i1 first index
     * @param i2 second index
     */
    private void swap(int i1, int i2) {
        Student temp = this.__heap.get(i1);
        this.__heap.set(i1, this.__heap.get(i2));
        this.__heap.set(i2, temp);
    }

    ///////////////////////
    // Get largest child //
    ///////////////////////

    /**
     * Gets the largest child of index
     * @param  index index to get the largest child from, if it's not already larger
     * @return       Out of index, and its two children, which is "larger"
     */
    private int largestChild(int index) {
        int largest;
        if (2 * index + 1 > this.size) {
            return (2 * index);
        } else {
            largest = 2 * index;
            if (this.__heap.get(largest).getCGPA() < this.__heap.get(2 * index + 1).getCGPA()) {
                largest = 2 * index + 1;
            } else if (this.__heap.get(largest).getCGPA() == this.__heap.get(2 * index + 1).getCGPA()) {
                if (this.__heap.get(2 * index + 1).getName().compareTo(this.__heap.get(largest).getName()) < 0) {
                    largest = 2 * index + 1;
                } else if (this.__heap.get(largest).getName().compareTo(this.__heap.get(2 * index + 1).getName()) == 0) {
                    if (this.__heap.get(2 * index + 1).getID() < this.__heap.get(largest).getID()) {
                        largest = 2 * index + 1;
                    }
                }
            }
            return (largest);
        }
    }

    ////////////////////////////////////////////////////////////////
    /// Bubble down element until max heap property is satisified //
    ////////////////////////////////////////////////////////////////

    /**
     * Bubble down element by comparing its value with its largest child
     * @param index initial index of element
     */
    public void bubbleDown(int index) {
        int lc;
        while (2 * index <= this.size) {
            lc = this.largestChild(index);
            if (this.__heap.get(lc).getCGPA() > this.__heap.get(index).getCGPA()) {
                this.swap(index, lc);
                index = lc;
            } else if (this.__heap.get(lc).getCGPA() == this.__heap.get(index).getCGPA()) {
                if (this.__heap.get(index).getName().compareTo(this.__heap.get(lc).getName()) > 0) {
                    this.swap(index, lc);
                    index = lc;
                } else if (this.__heap.get(lc).getName().compareTo(this.__heap.get(index).getName()) == 0) {
                    if (this.__heap.get(index).getID() > this.__heap.get(lc).getID()) {
                        this.swap(index, lc);
                        index = lc;
                    }
                } else {
                    break;
                }
            } else {
                break;
            }
        }
    }

    ////////////////////////////////////
    // Function to process the events //
    ////////////////////////////////////

    /**
     * [getStudents description]
     * @param  events [description]
     * @return        [description]
     */
    public List<Student> getStudents(List<String> events) {
        List<Student> ret;
        String[] temp;
        String oper;
        String name;
        int lc;
        int id;
        double cgpa;
        myComp comp = new myComp();
        while (!(events.isEmpty())) {
            temp = events.remove(0).split(" ");
            //ystem.out.println(Arrays.toString(temp));
            oper = temp[0];
            if (oper.equals("ENTER")) {
                name = temp[1];
                cgpa = Double.parseDouble(temp[2]);
                id = Integer.parseInt(temp[3]);
                this.__heap.add(new Student(id, name, cgpa));
                this.size++;
                this.reheapify(this.size);
                //System.out.println(this.__heap.get(1).getCGPA());
            } else {
                // remove student with highest priority and reheapify
                //ret = this.__heap.get(1);
                lc = this.largestChild(1);
                //System.out.println(ret.name);
                this.swap(1, size);
                this.__heap.remove(this.size);
                this.size--;
                this.bubbleDown(1);
            }

            //this.__heap.add()
        }

        //this.makeBST();
        System.out.println(this.__heap.subList(1, this.size + 1));
        ret = (this.__heap.subList(1, this.size + 1));
        return (ret); // end index is exclusive for subList
    }

    ////////////////
    // Re-Heapify //
    ////////////////

    public void reheapify(int index) {
        while (index / 2 > 0) {
            if (this.__heap.get(index / 2).getCGPA() < this.__heap.get(index).getCGPA()) {
                this.swap(index, index / 2);
                index = index / 2;
            } else if (this.__heap.get(index / 2).getCGPA() == this.__heap.get(index).getCGPA()) {
                if (this.__heap.get(index / 2).getName().compareTo(this.__heap.get(index).getName()) > 0) {
                    this.swap(index, index / 2);
                    index = index / 2;
                } else if (this.__heap.get(index / 2).getName().compareTo(this.__heap.get(index).getName()) == 0) {
                    if (this.__heap.get(index / 2).getID() > this.__heap.get(index).getID()) {
                        this.swap(index, index / 2);
                        index = index / 2;
                    }
                } else {
                    //this.bubbleDown(index);
                    break;
                }
            } else {
                //this.bubbleDown(index);
                break;
            }
        }
    }

    //////////////////
    // Child Switch //
    //////////////////
    public void makeBST() {
        int index = 1;
        while (2 * index < this.size && 2 * index + 1 < this.size) {
            if (this.__heap.get(2 * index).getCGPA() < this.__heap.get(2 * index + 1).getCGPA()) {
                this.swap(2 * index, 2 * index + 1);
            } else if (this.__heap.get(2 * index).getCGPA() == this.__heap.get(2 * index + 1).getCGPA()) {
                if (this.__heap.get(2 * index).getName().compareTo(this.__heap.get(2 * index + 1).getName()) > 0) {
                    this.swap(2 * index, 2 * index + 1);
                } else if (this.__heap.get(2 * index).getName().compareTo(this.__heap.get(2 * index + 1).getName()) == 0) {
                    if (this.__heap.get(2 * index).getID() > this.__heap.get(2 * index + 1).getID()) {
                        this.swap(index, index - 1);
                    }
                }
            }


            index++;
        }
    }

}


public class Solution {
    private final static Scanner scan = new Scanner(System.in);
    private final static Priorities priorities = new Priorities();

    public static void main(String[] args) {
        int totalEvents = Integer.parseInt(scan.nextLine());
        List<String> events = new ArrayList<>();

        while (totalEvents-- != 0) {
            String event = scan.nextLine();
            events.add(event);
        }

        List<Student> students = priorities.getStudents(events);

        if (students.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            for (Student st : students) {
                System.out.println(st.getName());
            }
        }
    }
}

/*-------------------------------------------------------------------------------------*/
