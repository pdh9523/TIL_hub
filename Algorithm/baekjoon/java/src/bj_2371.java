import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class bj_2371 {

    static List<List<Integer>> lists = new ArrayList<>();
    static Set<Integer> set = new HashSet<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        for (int i=0; i<N; i++) {
            List<Integer> list = new ArrayList<>();
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            while (k != -1) {
                list.add(k);
                k = Integer.parseInt(st.nextToken());
            }
            lists.add(list);
        }

        int ans = 0;
        while (!isDist(ans++)) set.clear();

        System.out.println(ans);
    }

    private static boolean isDist(int n) {
        for (List<Integer> list : lists) {
            if (n <list.size()) {
                if (set.contains(list.get(n))) return false;
                set.add(list.get(n));
            }
        }

        return true;
    }
}
