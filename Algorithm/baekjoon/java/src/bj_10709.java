import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj_10709 {

    static StringBuffer sb = new StringBuffer();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        char[][] arr = new char[N][M];
        int[][] ans = new int[N][M];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            String tmp = st.nextToken();
            Arrays.fill(ans[i], -1);
            for (int j=0; j<M; j++) {
                arr[i][j] = tmp.charAt(j);
            }
        }

        for (int i=0; i<N; i++) {
            boolean check = false;
            int cnt = 0;
            for (int j=0; j<M; j++) {
                if (arr[i][j] == 'c') {
                    cnt = 0;
                    ans[i][j] = 0;
                    check = true;
                } else if (check) {
                    cnt ++;
                    ans[i][j] = cnt;
                }
            }
        }

        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                sb.append(ans[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
