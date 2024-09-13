import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class bj_22865 {

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

    static int N;
    static ArrayList<ArrayList<Node>> graph;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        st = new StringTokenizer(br.readLine());
        int[] friends = new int[3];
        for (int i = 0; i < 3; i++) {
            friends[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            graph.get(x).add(new Node(y, weight));
            graph.get(y).add(new Node(x, weight));
        }

        int[][] distance = new int[3][N + 1];
        for (int i = 0; i < 3; i++) {
            Arrays.fill(distance[i], Integer.MAX_VALUE);
            dijkstra(friends[i], distance[i]);
        }

        int maxMinDistance = Integer.MIN_VALUE;
        int answerNode = 0;

        for (int i = 1; i <= N; i++) {
            int minDistanceToFriends = Math.min(distance[0][i], Math.min(distance[1][i], distance[2][i]));
            if (minDistanceToFriends > maxMinDistance) {
                maxMinDistance = minDistanceToFriends;
                answerNode = i;
            }
        }

        System.out.println(answerNode);
    }

    static void dijkstra(int start, int[] distance) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        distance[start] = 0;
        pq.offer(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int now = node.x;
            int dist = node.weight;

            if (distance[now] < dist) continue;

            for (Node nextNode : graph.get(now)) {
                int next = nextNode.x;
                int cost = dist + nextNode.weight;

                if (cost < distance[next]) {
                    distance[next] = cost;
                    pq.offer(new Node(next, cost));
                }
            }
        }
    }
}
