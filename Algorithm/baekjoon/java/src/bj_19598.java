import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class bj_19598 {

    static class Node implements Comparable<Node> {
        int x;
        int y;
        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Node o) {
            if (this.x == o.x) {
                return this.y - o.y;
            }
            return this.x - o.x;
        }

        @Override
        public String toString() {
            return "(" + x + " " + y + ")";
        }
    }

    static ArrayList<Node> arr = new ArrayList<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            arr.add(new Node(start, 1));
            arr.add(new Node(end, -1));
        }
        arr.sort(Node::compareTo);

        int ans = 0;
        int cur = 0;

        for (Node now: arr) {
            cur += now.y;
            ans = Math.max(ans, cur);
        }
        System.out.println(ans);
    }
}
