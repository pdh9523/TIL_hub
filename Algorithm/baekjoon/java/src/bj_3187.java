import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class bj_3187 {
    static class Node {
        int x;
        int y;
        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int k;       // 양
    static int v;       // 늑대
    static int N;
    static int M;
    static String[][] arr;
    static boolean[][] visit;
    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // 배열 입력
        arr = new String[N][M];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            String tmp = st.nextToken();
            for (int j=0; j<M; j++) {
                arr[i][j] = tmp.charAt(j)+"";
            }
        }
        // 방문 배열 초기화
        visit = new boolean[N][M];

        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (!visit[i][j]) {
                    bfs(i,j);
                }
            }
        }
        System.out.println(k + " " + v);
    }

    private static void bfs(int i, int j) {
        Queue<Node> q = new LinkedList<>();
        visit[i][j] = true;
        q.add(new Node(i,j));
        int sheep = 0;
        int wolves = 0;
        while (!q.isEmpty()) {
            Node node = q.poll();

            for (int k=0; k<4; k++) {
                int x = node.x + dx[k];
                int y = node.y + dy[k];
                if (0<= x && x < N && 0<= y && y < M) {
                    if (!visit[x][y] && !arr[x][y].equals("#")) {
                        visit[x][y] = true;
                        if (arr[x][y].equals("v")) {
                            wolves ++;
                        }
                        if (arr[x][y].equals("k")) {
                            sheep ++;
                        }
                        q.add(new Node(x,y));
                    }
                }
            }
        }
        if (sheep > wolves) {
            k += sheep;
        } else {
            v += wolves;
        }
    }
}
