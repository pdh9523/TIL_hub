import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;
import java.io.BufferedReader;

public class bj_23057 {

    static int N;
    static HashSet<Integer> data = new HashSet<>();
    static int[] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int M = 0;

        arr = new int[N];
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            M += arr[i];
        }

        backtrack(0,0);

        System.out.println((M+1-data.size()));
    }

    private static void backtrack(int idx, int res) {

        data.add(res);

        if (idx==N) return;

        backtrack(idx+1, res+arr[idx]);
        backtrack(idx+1, res);
    }
}
