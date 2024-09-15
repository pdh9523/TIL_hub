import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class bj_22116 {

    static class Node implements Comparable<Node> {
        int x;
        int y;
        int weight;

        public Node(int x, int y, int weight) {
            this.x = x;
            this.y = y;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o) {
            return this.weight - o.weight;
        }
    }
    static int[] dx = {1,0,-1,0};
    static int[] dy = {0,1,0,-1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        // 초기 배열 입력
        int[][] arr = new int[N][N];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 다익스트라 거리 배열 초기화
        int[][] distance = new int[N][N];
        for (int i=0; i<N; i++) {
            Arrays.fill(distance[i], Integer.MAX_VALUE);
        }
        // 초기값 설정
        distance[0][0] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        pq.add(new Node(0,0,0));

        while (!pq.isEmpty()) {
            Node node = pq.poll();

            if (node.weight > distance[node.x][node.y]) continue;

            for (int i=0; i<4; i++) {
                int x = node.x + dx[i];
                int y = node.y + dy[i];
                if (0 <= x && x < N && 0 <= y && y < N) {
                    int cost = Math.max(node.weight, Math.abs(arr[x][y]-arr[node.x][node.y]));
                    if (distance[x][y] > cost) {
                        distance[x][y] = cost;
                        pq.add(new Node(x,y,cost));
                    }
                }
            }
        }
        System.out.println(distance[N-1][N-1]);
    }
}
