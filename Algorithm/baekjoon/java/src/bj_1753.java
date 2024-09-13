import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class bj_1753 {

    static class Node implements Comparable<Node> {
        int x;
        int weight;
        public Node(int x, int weight) {
            this.x = x;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o) {
            return this.weight-o.weight;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());

        // start
        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());

        // 그래프 만들기
        ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();
        for (int i=0; i<=V; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i=0; i<E; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            graph.get(x).add(new Node(y, weight));
        }
        int[] distance = new int[V+1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[start] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start,0));

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int now = node.x;
            int distNow = node.weight;

            if (distance[now] < distNow) {
                continue;
            }

            ArrayList<Node> graphNow = graph.get(now);

            for (int i=0; i<graphNow.size(); i++) {
                int cost = graphNow.get(i).weight;
                int next = graphNow.get(i).x;

                if (distance[next] > distNow+cost) {
                    distance[next] = distNow+cost;
                    pq.add(new Node(next,distNow+cost));
                }
            }
        }

        for (int i=1; i<=V; i++) {
            System.out.println(distance[i]==Integer.MAX_VALUE?"INF":distance[i]);
        }
    }
}
