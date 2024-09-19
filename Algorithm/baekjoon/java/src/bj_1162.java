import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class bj_1162 {

    static class Node implements Comparable<Node> {
        int x;
        int cnt;
        long weight;

        public Node(int x, int cnt, long weight) {
            this.x = x;
            this.cnt = cnt;
            this.weight = weight;
        }

        public Node(int x, long weight) {
            this.x = x;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o) {
            return Long.compare(this.weight, o.weight);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        ArrayList<ArrayList<Node>> graph = new ArrayList<>();
        for (int i=0; i<=N; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            graph.get(a).add(new Node(b,d));
            graph.get(b).add(new Node(a,d));
        }

        long[][] distance = new long[N+1][K+1];
        for (int i=0; i<=N; i++) {
            Arrays.fill(distance[i], Long.MAX_VALUE);
        }

        distance[1][0] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(1,0,0));

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            long distNow = node.weight;
            int cnt = node.cnt;
            int now = node.x;

            if (distNow > distance[now][cnt]) continue;

            ArrayList<Node> nextNodes = graph.get(now);

            for (Node nextNode : nextNodes) {
                long distNext = distNow + nextNode.weight;
                if (distance[nextNode.x][cnt] > distNext) {
                    distance[nextNode.x][cnt] = distNext;
                    pq.add(new Node(nextNode.x,cnt,distNext));
                }

                if (cnt < K && distance[nextNode.x][cnt+1] > distNow) {
                    distance[nextNode.x][cnt+1] = distNow;
                    pq.add(new Node(nextNode.x,cnt+1, distNow));
                }
            }
        }

        long ans = Long.MAX_VALUE;

        for (long x: distance[N]) {
            if (ans > x) {
                ans = x;
            }
        }
        System.out.println(ans);
    }
}
