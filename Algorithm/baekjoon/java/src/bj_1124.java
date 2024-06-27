import java.io.*;
import java.util.*;


public class bj_1124 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N,M
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // isPrime
        boolean[] isPrime = new boolean[M+1];
        for (int i=0; i<M+1; i++) {
            isPrime[i] = true;
        }
        isPrime[0]=isPrime[1]=false;

        // primes
        ArrayList<Integer> primes = new ArrayList<>();
        for (int i=2; i<M+1; i++) {
            if (isPrime[i]) {
                primes.add(i);
                for (int j=i*2; j<M+1; j+=i) {
                    isPrime[j] = false;
                }
            }
        }
        // primeCnt
        int[] primeCnt = new int[M+1];

        for (int prime : primes) {
            for (int i=prime; i<M+1; i+=prime) {
                int tmp = i ;
                while (tmp%prime==0) {
                    primeCnt[i] ++ ;
                    tmp /= prime ;
                }
            }
        }
        int ans = 0 ;
        for (int i=N; i<M+1; i++) {
            if (isPrime[primeCnt[i]]) ans ++;
        }

        System.out.println(ans);
    }
}
