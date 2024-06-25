package bj_30802;

import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // N : 전체 인원 수
        int N = Integer.parseInt(st.nextToken());

        // arr : 티셔츠 배열
        st = new StringTokenizer(br.readLine());
        int[] arr = new int[6];
        for (int i=0; i<6; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // T : 티셔츠 묶음 수
        // P : 펜 묶음 수
        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        int ans = 0 ;
        for (int i=0; i<6; i++) {
            ans += (arr[i]+T-1)/T;
        }

        System.out.println(ans);
        System.out.printf("%s %s", N/P, N%P);

    }
}
