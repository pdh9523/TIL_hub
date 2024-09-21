import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class bj_1351 {

    static HashMap<Long, Long> data = new HashMap<>();
    static long N,P,Q;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Long.parseLong(st.nextToken());
        P = Long.parseLong(st.nextToken());
        Q = Long.parseLong(st.nextToken());
        data.put(0L, 1L);
        System.out.println(seq(N));
    }

    private static long seq(long n) {
        if (data.containsKey(n)) return data.get(n);
        data.put(n, seq(n/P)+seq(n/Q));
        return data.get(n);
    }
}
