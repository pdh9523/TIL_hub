import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class bj_17142 {

    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0 ,-1 ,0};

    static int N,M;
    static int ans;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int[][] arr = new int[N][N];

        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        backtrack(0,-1,0, arr);

        System.out.println(ans);
    }

    private static void backtrack(int x, int y, int idx, int[][] arr) {
        if (idx == M) {
            ans = Math.max(ans,dfs(arr));
            return;
        }
        y ++;
        if (y==N) {
            x ++;
            y=0;
            if (x==N) {
                return;
            }
        }
        backtrack(x,y,idx+1,arr);
        if (arr[x][y] == 0) {
            arr[x][y] = 3;
            backtrack(x, y, idx + 1, arr);
            arr[x][y] = 0;
        }
    }

    private static int dfs(int[][] arr) {
        int cnt = 0;
        Queue<int[]> q = new LinkedList<>();
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (arr[i][j] == 3) {
                    q.add(new int[]{i,j,0});
                }
            }
        }

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            cnt = cur[2];
            for (int i=0; i<4; i++) {
                int x = cur[0] + dx[i];
                int y = cur[1] + dy[i];
                if (0<= x && x<N && 0<= y && y<N) {
                    if (arr[x][y] == 0) {
                        arr[x][y] = 3;
                        q.add(new int[]{x,y,cur[2]+1});
                    }
                }
            }
        }
        return cnt;
    }
}
