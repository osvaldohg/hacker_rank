// https://www.hackerrank.com/challenges/java-loops/problem
// by oz

import java.util.*;
import java.io.*;
import java.lang.Math;
class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            
            int res=a;
            
            for(int j=0; j<n;j++)
            {
                int temp=(int)Math.pow(2,j);
                res+=temp*b;
                System.out.print(""+res+" ");
            }
            System.out.println();
        }
        in.close();
        
        
    }
}