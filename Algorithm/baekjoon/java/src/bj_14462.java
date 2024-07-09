import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_14462 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        // left
        int[] left = new int[N+1];
        for (int i=1; i<=N; i++) {
            st = new StringTokenizer(br.readLine());
            left[i] = Integer.parseInt(st.nextToken());
        }
        // right
        int[] right = new int[N+1];
        for (int i=1; i<=N; i++) {
            st = new StringTokenizer(br.readLine());
            right[i] = Integer.parseInt(st.nextToken());
        }
        // DP
        int[][] DP = new int[N+1][N+1];

        for (int i=1; i<=N; i++) {
            for (int j=1; j<=N; j++) {
                DP[i][j] = Math.max(DP[i-1][j], DP[i][j-1]);
                if (Math.abs(left[i]-right[j]) <=4 ) {
                    DP[i][j] = DP[i-1][j-1] + 1;
                }
            }
        }

        System.out.println(DP[N][N]);
    }
}
