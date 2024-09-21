import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_32200 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        int X = Integer.parseInt(st.nextToken());
        int Y = Integer.parseInt(st.nextToken());

        int ans = 0;
        int rest = 0;

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            int num = Integer.parseInt(st.nextToken());

            int cnt = num/X;
            int maxValue = num - Y*cnt;

            if (maxValue > 0) {
                rest += maxValue;
            }
            ans += cnt;
        }

        System.out.println(ans);
        System.out.println(rest);
    }
}
