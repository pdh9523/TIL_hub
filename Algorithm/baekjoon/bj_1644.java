package bj_1644;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        boolean[] isPrime = new boolean[N+1];

        int[] sosu = new int[N/2+1];
        int idx=0;
        int tmp;
        // 에라토스테네스의 체
        for (int i=2; i<N+1; i++) {
            if (!isPrime[i]) {
                sosu[idx]=i;
                idx ++;
                tmp = 2*i;
                while (tmp<=N) {
                    isPrime[tmp]=true;
                    tmp += i;
                }
            }
        }
        int start=0,end=0,res=0,cnt=0;
        if (Arrays.stream(sosu).anyMatch(value -> value == N)) {
            cnt ++;
        }

        while (end<idx) {
            if (res==N) cnt++;
            if (res<N) {
                res+=sosu[end];
                end ++;
            } else {
                res-=sosu[start];
                start ++;
            }
        }
        System.out.println(cnt);
    }
}
