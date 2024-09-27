import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class bj_23793 {

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

    private static ArrayList<ArrayList<Node>> graph;
    private static int[] distance;
    private static int N;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        graph = new ArrayList<>();
        for (int i=0; i<=N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            graph.get(a).add(new Node(b,weight));
        }
        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int mid = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        int res1 = dijkstra(start,mid, 0);
        int res2 = dijkstra(mid,end,0);
        int res3 = dijkstra(start,end,mid);
        int res = 0;
        if (res1 == -1 || res2 == -1 ) {
            res = -1;
        } else {
            res = res1+res2;
        }

        System.out.println(res+" "+res3);

    }

    private static int dijkstra(int s, int e, int exception) {
        distance = new int[N+1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[s] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(s,0));
        while (!pq.isEmpty()) {
            Node node = pq.poll();

            if (node.x == exception) continue;

            if (node.weight > distance[node.x]) continue;

            ArrayList<Node> nextNodes = graph.get(node.x);
            for (Node next: nextNodes) {
                int cost = next.weight + node.weight;
                if (distance[next.x] > cost) {
                    distance[next.x] = cost;
                    pq.add(new Node(next.x, cost));
                }
            }
        }

        return distance[e] == Integer.MAX_VALUE ? -1 : distance[e];
    }
}
