import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class bj_17450 {

    static class Node implements Comparable<Node> {
        double cost;
        String name;

        public Node(double cost, String name) {
            this.cost = cost;
            this.name = name;
        }

        @Override
        public int compareTo(Node o) {
            return Double.compare(o.cost, this.cost);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        Node[] arr = new Node[3];
        for (int i=0; i<3; i++) {
            st = new StringTokenizer(br.readLine());

            double price = Double.parseDouble(st.nextToken());
            double weight = Double.parseDouble(st.nextToken());
            price *= 10;
            weight *= 10;

            if (price >= 5000) {
                price -= 500;
            }

            double eff = weight / price;
            String name = "";
            switch (i) {
                case 0:
                    name = "S";
                    break;
                case 1:
                    name = "N";
                    break;
                case 2:
                    name = "U";
                    break;
            }

            arr[i] = new Node(eff, name);
        }

        Arrays.sort(arr);
        System.out.println(arr[0].name);
    }
}