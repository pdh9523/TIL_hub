import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class bj_15650 {

    private static int N,M;
    private static StringBuffer sb = new StringBuffer();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        backtrack(new ArrayList<Integer>());
        System.out.println(sb);
    }
    private static void backtrack(ArrayList<Integer> visit) {
        if (visit.size() == M) {
            for (int i=0; i<M; i++) {
                sb.append(visit.get(i)).append(" ");
            }
            sb.append("\n");
            return;
        }

        for(int i=1; i<=N; i++) {
            if (!visit.contains(i)) {
                if (visit.isEmpty() || visit.getLast() < i) {
                    visit.add(i);
                    backtrack(visit);
                    visit.removeLast();
                }
            }
        }
    }
}
