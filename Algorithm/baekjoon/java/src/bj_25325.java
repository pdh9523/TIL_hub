import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class bj_25325 {

    private static class Node implements Comparable<Node> {
        String key;
        int value;

        public Node(String key, int value) {
            this.key = key;
            this.value = value;
        }

        @Override
        public int compareTo(Node o) {
            if (this.value == o.value) {
                return this.key.compareTo(o.key);
            }
            return o.value - this.value;
        }
    }

    static StringBuffer sb = new StringBuffer();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        HashMap<String, Integer> data = new HashMap<>();
        for (int i=0; i<=N; i++) {
            st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                String person = st.nextToken();
                data.put(person, data.getOrDefault(person, -1)+1);
            }
        }

        List<Node> lists = new ArrayList<>();
        for (String key : data.keySet()) {
            lists.add(new Node(key, data.get(key)));
        }

        Collections.sort(lists);

        for (Node node: lists) {
            sb.append(node.key).append(" ").append(node.value).append("\n");
        }
        System.out.println(sb);
    }
}