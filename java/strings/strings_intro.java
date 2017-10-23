// https://www.hackerrank.com/challenges/java-strings-introduction/problem
// by oz
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        int total=0;
        total=A.length()+B.length();
        System.out.println(""+total);
        if (A.compareTo(B) >0)
        {
            System.out.println("Yes");
        }
        else
        {
            System.out.println("No");
        }
        
        String output = A.substring(0, 1).toUpperCase() + A.substring(1);
        String output2 = B.substring(0, 1).toUpperCase() + B.substring(1);
        System.out.println(output+" "+output2);
        
        
    }
}
