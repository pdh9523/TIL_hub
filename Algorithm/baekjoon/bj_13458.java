package bj_13458;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // A : 시험장의 개수
        int A = Integer.parseInt(st.nextToken());
        // 시험장의 개수만큼 배열을 생성
        int[] arr;
        arr = new int[A];

        st = new StringTokenizer(br.readLine());
        for (int i=0 ; i < A ; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        long ans = 0;
        for (int num : arr) {
            ans += 1;
            num -= B;
            if (num>0) {
                ans += (num+C-1)/C;
            }

        }
    System.out.println(ans);
    }
}
