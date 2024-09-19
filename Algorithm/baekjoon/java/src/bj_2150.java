import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class bj_2150 {

    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    static ArrayList<ArrayList<Integer>> reversedGraph = new ArrayList<>();
    static ArrayList<Integer> stack = new ArrayList<>();
    static boolean[] visit;
    static ArrayList<Integer> scc;

    static StringBuffer sb = new StringBuffer();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        for (int i=0; i<=N; i++) {
            graph.add(new ArrayList<>());
            reversedGraph.add(new ArrayList<>());
        }

        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            reversedGraph.get(b).add(a);
        }

        visit = new boolean[N+1];
        for (int i=1; i<=N; i++) {
            if (!visit[i]) {
                dfs(i);
            }
        }

        visit = new boolean[N+1];
        ArrayList<ArrayList<Integer>> ans = new ArrayList<>();
        while (!stack.isEmpty()) {
            scc = new ArrayList<>();

            int now = stack.remove(stack.size()-1);
            if (!visit[now]) {
                sfd(now);
                Collections.sort(scc);
                ans.add(scc);
            }
        }

//      ans.sort(Comparator.comparing(o -> o.get(0)));

        System.out.println(ans.size());

        Comparator<List<Integer>> comparator = Comparator.comparing(o -> o.get(0));

        // 제일 짧은 값을 기준으로 하기
        for (int i=1; i<=N; i++) {
            final int index = i;
            comparator = comparator.thenComparing(o -> o.get(index));
        }

        ans.sort(comparator);

        for (ArrayList<Integer> tmp : ans) {
            for (Integer integer : tmp) {
                sb.append(integer).append(" ");
            }
            sb.append("-1");
            sb.append("\n");
        }
        System.out.println(sb);
    }

    private static void dfs(int now) {
        visit[now] = true;
        ArrayList<Integer> nextNodes = graph.get(now);
        for (int i=0; i<nextNodes.size(); i++) {
            if (!visit[nextNodes.get(i)]) {
                dfs(nextNodes.get(i));
            }
        }
        stack.add(now);
    }

    private static void sfd(int now) {
        visit[now] = true;
        scc.add(now);
        ArrayList<Integer> nextNodes = reversedGraph.get(now);
        for (int i=0; i<nextNodes.size(); i++) {
            if (!visit[nextNodes.get(i)]) {
                sfd(nextNodes.get(i));
            }
        }
    }
}
