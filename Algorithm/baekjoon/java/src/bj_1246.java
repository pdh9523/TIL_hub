import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class bj_1246 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // N: 달걀 개수
        // M: 잠재 고객 수
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Integer[] arr = new Integer[M];
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int maxV = Integer.MIN_VALUE;
        int ans = 0;
        Arrays.sort(arr, Collections.reverseOrder());

        for (int i=0; i<M; i++) {
            if (i+1 > N) break;

            if (arr[i] * (i+1) > maxV) {
                ans = arr[i];
                maxV = arr[i] * (i+1);
            }
        }
        System.out.println(ans+" "+maxV);
    }
}
