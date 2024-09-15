import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class bj_27160 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        HashMap<String, Integer> data = new HashMap<>();

        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            String word = st.nextToken();
            int count = Integer.parseInt(st.nextToken());

            if (!data.containsKey(word)) {
                data.put(word, count);
            } else {
                data.put(word, data.get(word) + count);
            }
        }

        String ans = "NO";
        for (String word : data.keySet()) {
            if (data.get(word) == 5) {
                ans = "YES";
                break;
            }
        }
        System.out.println(ans);
    }
}
