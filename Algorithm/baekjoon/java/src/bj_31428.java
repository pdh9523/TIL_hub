import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_31428 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st ;

        // N
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        // arr
        String[] arr = new String[N];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            arr[i] = st.nextToken();
        }

        // S
        st = new StringTokenizer(br.readLine());
        String S = st.nextToken();
        // cnt
        int cnt = 0;
        for(String s : arr) {
            if (S.equals(s)) {
                cnt ++;
            }
        }
        System.out.println(cnt);
    }
}
