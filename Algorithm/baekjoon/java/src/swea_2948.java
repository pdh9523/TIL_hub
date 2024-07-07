import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class swea_2948 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // tc
        StringTokenizer st = new StringTokenizer(br.readLine());
        int tc = Integer.parseInt(st.nextToken());

        for (int t = 0; t < tc; t++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            String[] arr = new String[N];
            st = new StringTokenizer(br.readLine());
            for (int i=0; i<N; i++) {
                arr[i] = st.nextToken();
            }
            HashMap<String, Boolean> brr = new HashMap<>();
            st = new StringTokenizer(br.readLine());
            for (int i=0; i<M; i++) {
                brr.put(st.nextToken(), true);
            }
            int cnt = 0;
            for (int i=0; i<N; i++) {
                if (brr.containsKey(arr[i])) {
                    cnt ++;
                }
            }
            System.out.println("#"+(t+1)+" "+cnt);
        }
    }
}