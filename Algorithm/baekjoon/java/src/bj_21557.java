import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class bj_21557 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st ;

        // N
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr;
        arr = new int[N];
        // arr
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int left = arr[0];
        int right = arr[N-1];

        for (int i=0; i<N-3; i++) {
            if (left>right) {
                left -= 1;
            } else {
                right -= 1;
            }
        }
        int ans = Math.max(left,right) -1;
        System.out.println(ans);
    }
}
