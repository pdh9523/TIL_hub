import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class bj_17142 {

    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0 ,-1 ,0};

    static int N,M;
    static int ans = Integer.MAX_VALUE;
    static int emptySpace ;

    static class Virus {
        int x;
        int y;
        int time;
        Virus(int x, int y, int time) {
            this.x = x;
            this.y = y;
            this.time = time;
        }
    }

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
                if (arr[i][j] == 0) {
                    emptySpace++;
                }
            }
        }
        backtrack(0,-1,0, arr);

        System.out.println(ans==Integer.MAX_VALUE?-1:ans);
    }

    private static void backtrack(int x, int y, int idx, int[][] arr) {
        if (idx == M) {
            int[][] copyArr = new int[N][N];
            for (int i=0; i<N; i++) {
                copyArr[i] = arr[i].clone();
            }
            ans = Math.min(ans, bfs(copyArr));

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
        if (arr[x][y] == 2) {
            arr[x][y] = 3;
            backtrack(x, y, idx + 1, arr);
            arr[x][y] = 2;
        }
        backtrack(x,y,idx,arr);
    }

    private static int bfs(int[][] arr) {
        Queue<Virus> q = new LinkedList<>();
        int time = 0;
        int filledSpace = 0;
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (arr[i][j] == 3) {
                    q.add(new Virus(i,j,0));
                }
            }
        }
        while (!q.isEmpty()) {
            Virus cur = q.poll();

            if (filledSpace==emptySpace) break;

            for (int i=0; i<4; i++) {
                int x = cur.x + dx[i];
                int y = cur.y + dy[i];
                if (0<= x && x<N && 0<= y && y<N) {
                    if (arr[x][y] == 0) {
                        arr[x][y] = 3;
                        q.add(new Virus(x,y,cur.time + 1));
                        time = cur.time+1;
                        filledSpace++;
                    } else if (arr[x][y] == 2) {
                        arr[x][y] = 3;
                        q.add(new Virus(x,y,cur.time + 1));
                    }
                }
            }
        }
        return filledSpace==emptySpace? time: Integer.MAX_VALUE;
    }
}
