import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class bj_16398 {

    static class Node implements Comparable<Node> {
        int x;
        int weight;

        public Node(int x, int weight) {
            this.x = x;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o) {
            return this.weight - o.weight;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        ArrayList<ArrayList<Node>> graph = new ArrayList<>();
        for (int i=0; i<N; i++) {
            graph.add(new ArrayList<>());
        }


        int[][] arr = new int[N][N];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i=0; i<N-1; i++) {
            for (int j=i+1; j<N; j++) {
                graph.get(i).add(new Node(j, arr[i][j]));
                graph.get(j).add(new Node(i, arr[i][j]));
            }
        }

        boolean[] visit = new boolean[N];

        PriorityQueue<Node> pq = new PriorityQueue<>();
        // 0부터 시작
        pq.add(new Node(0 ,0));
        long ans = 0;
        while (!pq.isEmpty()) {
            Node node = pq.poll();

            int now = node.x;
            int nowDist = node.weight;

            if (!visit[now]) {
                visit[now] = true;
                ans += nowDist;
                ArrayList<Node> nextNodes = graph.get(now);
                for (int i=0; i<nextNodes.size(); i++) {
                    pq.add(nextNodes.get(i));
                }
            }
        }
        System.out.println(ans);
    }
}
