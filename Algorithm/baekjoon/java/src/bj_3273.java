import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj_3273 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        // 정렬
        Arrays.sort(arr);

        int left = 0;
        int right = N-1;
        int cnt = 0;

        st = new StringTokenizer(br.readLine());
        int target = Integer.parseInt(st.nextToken());

        while(left<right) {
            if (arr[left]+arr[right] == target) {
                cnt ++;
                left ++;
            }
            else if (arr[left] + arr[right] > target) {
                right --;
            }
            else if (arr[left] + arr[right] < target) {
                left ++;
            }
        }
        System.out.println(cnt);


    }
}
