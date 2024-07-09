import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class bj_14467 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        HashMap<Integer, Integer> data = new HashMap<>();
        int cnt = 0;
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if (data.containsKey(a)) {
                if (data.get(a) != b) {
                    cnt ++ ;
                }
            }
            data.put(a,b);
        }
        System.out.println(cnt);
    }
}
