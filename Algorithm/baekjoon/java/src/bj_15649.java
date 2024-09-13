import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class bj_15649 {
    private static int N,K;

    private static final StringBuffer sb = new StringBuffer();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        backtrack(0, new int[K], new boolean[N+1]);
        System.out.println(sb);
    }

    static void backtrack(int idx, int[] arr, boolean[] visit) {
        if (idx==K) {
            for (int i=0; i<K; i++) {
                sb.append(arr[i]).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i=1; i<=N; i++) {
            if (!visit[i]) {
                arr[idx] = i;
                visit[i] = true;
                backtrack(idx+1, arr, visit);
                visit[i] = false;
                arr[idx] = 0;
            }
        }
    }
}
