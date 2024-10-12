import java.io.*;
import java.util.*;

public class bj_19563 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int L = Math.abs(N) + Math.abs(M);

        if (L <= K && (L-K)%2 == 0) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
