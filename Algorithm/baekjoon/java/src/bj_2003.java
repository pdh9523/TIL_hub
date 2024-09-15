import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_2003 {

    public static void main (String [] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 배열 입력
        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0;
        int right = 0;
        int now = arr[0];
        int cnt = 0;
        while (true) {
            if (now == M) {
                cnt ++;
                right ++;
                if (right >= N) break;
                now += arr[right];
            }
            else if (now < M) {
                right ++;
                if (right >= N) break;
                now += arr[right];
            }
            else if (now > M) {
                now -= arr[left];
                left ++;
            }
        }
        System.out.println(cnt);

    }
}
