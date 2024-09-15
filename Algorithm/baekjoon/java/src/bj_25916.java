import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_25916 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        long ans = 0;
        int left = 0;
        int right = 0;
        long now = arr[0];
        while (true) {
            if (M == now) {
                ans = M;
                break;
            }

            if (M > now) {
                ans = Math.max(ans, now);
                right ++;
                if (right>=N) break;
                now += arr[right];
            } else {
                now -= arr[left];
                left ++;
            }
        }
        System.out.println(ans);
    }
}
