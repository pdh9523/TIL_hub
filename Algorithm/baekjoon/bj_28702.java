package bj_28702;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st ;
        int ans = 0 ;
        for (int i=0; i<3; i++) {
            st = new StringTokenizer(br.readLine());
        try {
            ans = Integer.parseInt(st.nextToken());
        } catch (NumberFormatException e) {
            ans ++;
        }
        }
        ans ++ ;
        if (ans%15==0) {
            System.out.println("FizzBuzz");
        } else if (ans%5==0) {
            System.out.println("Buzz");
        } else if (ans%3==0) {
            System.out.println("Fizz");
        } else {
            System.out.println(ans);
        }
    }
}
