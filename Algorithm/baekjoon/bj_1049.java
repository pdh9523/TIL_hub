package bj_1049;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        int pack = Integer.MAX_VALUE;
        int one = Integer.MAX_VALUE;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        for (int i=0 ; i < m ; i++) {
            st = new StringTokenizer(br.readLine());

            int tmpPack = Integer.parseInt(st.nextToken());
            int tmpOne = Integer.parseInt(st.nextToken());

            pack = Math.min(pack,tmpPack);
            one = Math.min(one,tmpOne);


        }
        if (pack > one*6) {
            System.out.println(one*n);
        } else {
            int a = n/6*pack + n%6*one;
            int b = n/6*pack + (n%6!=0?pack:0);
            System.out.println(Math.min(a,b));
        }
    }
}
