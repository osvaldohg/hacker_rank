// https://www.hackerrank.com/challenges/java-end-of-file/problem
// by oz
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        int count=1;
        Scanner scan= new Scanner(System.in);
        while (scan.hasNext())
        
        {
            System.out.println(count+" "+scan.nextLine());
            count++;
        }
        
            
    }
}