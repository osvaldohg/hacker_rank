// https://www.hackerrank.com/challenges/java-date-and-time/problem
// by oz

import java.util.Scanner;
import java.time.LocalDate;
import java.time.DayOfWeek;
public class Solution {
    public static String getDay(String day, String month, String year) {
        /*
        * Write your code here.
        */
        int n_day = Integer.parseInt(day);
        int n_month = Integer.parseInt(month);
        int n_year = Integer.parseInt(year);
        LocalDate local=LocalDate.of(n_year,n_month,n_day);
        DayOfWeek daynum=local.getDayOfWeek();
        return daynum.toString();
        
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String month = in.next();
        String day = in.next();
        String year = in.next();
        
        System.out.println(getDay(day, month, year));
    }
}