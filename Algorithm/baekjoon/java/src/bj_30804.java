import java.io.*;
import java.util.*;

public class bj_30804 {
    public static void main(String[] args) throws Exception {
        // 입력 초기 처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st ;

        // N : 총 개수
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        // arr : 탕후루 배열
        st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        // ans, left, right : ans는 답, left,right는 투 포인터
        int ans = 0;
        int left = 0;
        int right = 0;
        // cnt : 각 인덱스의 숫자 개수를 세어줄 배열
        int[] cnt = new int[10];

        while (right<N) {
            cnt[arr[right]]++;
            right ++;
            while (true) {
                int tmp = 0;
                for (int j=0; j<10; j++) {
                    if (cnt[j]>0) {
                        tmp ++;
                    }
                }
                if (tmp<=2) break;

                cnt[arr[left]] -= 1;
                left += 1;
            }
            ans = Math.max(ans, right-left);
        }
        System.out.println(ans);
    }
}
