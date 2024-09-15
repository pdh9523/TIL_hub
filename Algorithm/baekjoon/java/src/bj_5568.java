import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;

public class bj_5568 {

    static HashSet<Integer> set = new HashSet<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());

        int[] arr = new int[N];
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        backtrack(0, K, arr, new boolean[N], new ArrayList<>());
        System.out.println(set.size());
    }

    private static void backtrack(int idx, int k, int[] arr, boolean[] visit, ArrayList<Integer> res) {
        if (idx==k) {
            StringBuffer sb = new StringBuffer();
            for (int i=0; i<res.size(); i++) {
                sb.append(res.get(i));
            }
            set.add(Integer.parseInt(sb.toString()));
        }

        for (int i=0; i<arr.length; i++) {
            if (!visit[i]) {
                visit[i] = true;
                res.add(arr[i]);
                backtrack(idx+1, k, arr, visit, res);
                visit[i] = false;
                res.removeLast();
            }
        }
    }
}