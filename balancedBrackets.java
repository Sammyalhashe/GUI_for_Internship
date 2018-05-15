/*input
{[()]}
{[(])}
{{[[(())]]}}
*/
import java.util.*;
import java.io.*;

public class balancedBrackets {

    public static boolean check(String input) throws IOException{
        HashMap<String, String> Brackets = new HashMap<>(3);
        Brackets.put("{", "}");
        Brackets.put("(", ")");
        Brackets.put("[", "]");
        String popped;
        String brack;
        ArrayList<String> stack = new ArrayList<>();
        for (int i = 0; i < input.length(); i++) {
            brack = Character.toString(input.charAt(i));
            if (Brackets.containsKey(brack)) {
                stack.add(Brackets.get(brack));
            } else {
                if (stack.size() == 0 || !(brack.trim().equals(stack.remove(stack.size() - 1).trim()))) {
                    return false;
                }
            }
        }
        return (stack.size() == 0);
    }


    public static void main(String []argh) throws IOException{
        Scanner sc = new Scanner(System.in);

        boolean ret;

        while (sc.hasNext()) {
            String input = sc.next();
            ret = check(input);
            System.out.println(ret ? "YES" : "NO");
        }

    }

}