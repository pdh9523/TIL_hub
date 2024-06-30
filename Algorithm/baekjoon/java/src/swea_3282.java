import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea_3282 {
    public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st ;

    st = new StringTokenizer(br.readLine());
    int t = Integer.parseInt(st.nextToken());

    for (int tc=1; tc<=t; tc++) {
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[][] DP = new int[N+1][K+1];
        int[][] things = new int[N+1][2] ;

        for (int thing=1; thing < N; thing++) {
            st = new StringTokenizer(br.readLine());
            things[thing][0] = Integer.parseInt(st.nextToken());
            things[thing][1] = Integer.parseInt(st.nextToken());
        }

        for (int i=1; i<N+1; i++) {
            for (int j=1; j<K+1; j++) {

                if (j < things[i][0]) {
                    DP[i][j] = DP[i-1][j] ;
                } else {
                    DP[i][j] = Math.max(DP[i-1][j-things[i][0]]+things[i][1], DP[i-1][j] );
                }
            }
        }
        System.out.println("#" + tc + " " + DP[N][K]);
    }



    }
}
