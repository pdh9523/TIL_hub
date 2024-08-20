import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_14267 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // arr
        st = new StringTokenizer(br.readLine());
        int[] arr = new int[N+1];
        for (int i=1 ; i<=N ; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // DP
        int[] DP = new int[N+1];

        // 계산
        for (int j=0; j<M; j++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            DP[i] += w;
        }

        //
        for (int i=2; i<=N; i++) {
            DP[i] += DP[arr[i]];
        }

        for (int i=1; i<DP.length; i++) {
            System.out.print(DP[i] + " ");
        }
    }
}
