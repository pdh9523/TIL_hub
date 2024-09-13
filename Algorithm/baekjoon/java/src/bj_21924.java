import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class bj_21924 {

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
        int M = Integer.parseInt(st.nextToken());

        ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();
        for (int i=0; i<=N; i++) {
            graph.add(new ArrayList<Node>());
        }
        // making graph
        long total = 0;
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            graph.get(x).add(new Node(y, weight));
            graph.get(y).add(new Node(x, weight));
            total += weight;
        }

        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        // 시작 지점을 1로 설정
        pq.add(new Node(1,0));
        boolean[] visit = new boolean[N+1];
        int cnt = 0;
        while (!pq.isEmpty()) {
            Node node = pq.poll();

            int next = node.x;
            int distance = node.weight;

            if (!visit[next]) {
                visit[next] = true;
                cnt ++;
                total -= distance;

                ArrayList<Node> nextNodes = graph.get(next);
                for (Node nextNode: nextNodes) {
                    if (!visit[nextNode.x]) {
                        pq.offer(nextNode);
                    }
                }
            }
        }

        System.out.println(cnt==N? total : -1);
    }
}
