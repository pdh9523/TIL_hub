import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_2243 {
    static int maxSize = (int)Math.pow(10, 6);
    static StringBuffer sb = new StringBuffer();
    static int[] tree = new int[4*maxSize];
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            if (cmd.equals("1")) {
                int a = Integer.parseInt(st.nextToken());
                findCandy(1, maxSize, 1, a);
            } else {
              int a = Integer.parseInt(st.nextToken());
              int b = Integer.parseInt(st.nextToken());
              putCandy(1, maxSize, 1, a, b);
            }
        }
        System.out.println(sb);
    }

    private static void putCandy(int left, int right, int node, int a, int b) {
        tree[node] += b;

        if (left == right) return;
        int mid = (left + right) / 2;

        if (a <= mid) {
            putCandy(left, mid, node*2, a, b);
        } else {
            putCandy(mid+1, right, node*2+1, a, b);
        }
    }

    private static void findCandy(int left, int right, int node, int a) {
        tree[node] -= 1;

        if (left == right) {
            sb.append(left).append("\n");
            return;
        }
        int mid = (left+right) / 2;

        if (tree[node*2] >= a) {
            findCandy(left, mid, node*2, a);
        } else {
            findCandy(mid+1, right, node*2+1, a-tree[node*2]);
        }
    }
}
