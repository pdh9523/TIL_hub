import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class bj_1270 {

    static HashMap<Long, Integer> data;
    static StringBuffer sb = new StringBuffer();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        for (int k=0; k<N; k++) {

            st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(st.nextToken());

            data = new HashMap<>();

            int ans = 0;
            long res = 0;
            for (int j=0; j<M; j++) {
                long tmp = Long.parseLong(st.nextToken());
                int count = data.getOrDefault(tmp,0)+1;

                data.put(tmp, count);

                if (ans < count) {
                    ans = count;
                    res = tmp;
                }
            }

            if (data.get(res) > M/2) {
                sb.append(res).append("\n");
            } else {
                sb.append("SYJKGW").append("\n");
            }
        }
        System.out.println(sb);
    }
}
