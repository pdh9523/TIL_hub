import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class bj_14716 {

    static int N;
    static int M;
    static int[][] arr;
    static int[] dx = {1, 0, -1, 0, -1, 1, -1, 1};
    static int[] dy = {0, 1, 0 ,-1, 1, -1, -1, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N][M];
        int cnt = 0;
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (arr[i][j] != 0) {
                    cnt += bfs(i,j);
                }
            }
        }

        System.out.println(cnt);
    }

    private static int bfs(int x, int y) {
        arr[x][y] = 0;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x,y});

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int ci = cur[0];
            int cj = cur[1];
            for (int i=0; i<8; i++) {
                int ni = ci + dx[i];
                int nj = cj + dy[i];
                if (0<= ni && ni < N && 0<= nj && nj < M && arr[ni][nj] != 0) {
                    arr[ni][nj] = 0;
                    q.add(new int[]{ni,nj});
                }
            }
        }
        return 1;
    }
}
