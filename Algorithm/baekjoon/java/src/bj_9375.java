import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st ;
        // tc : 테케 개수
        st = new StringTokenizer(br.readLine());
        int tc = Integer.parseInt(st.nextToken());

        for (int i=0; i<tc; i++) {
            // n : 옷 개수
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            // clothings : 옷 해시맵
            HashMap<String, Integer> clothings = new HashMap<>();
            for (int j=0; j<n; j++) {
                st = new StringTokenizer(br.readLine());
                String cloth = st.nextToken();
                String category = st.nextToken();
                clothings.put(category, clothings.getOrDefault(category, 0)+1);
            }
            int ans = 1;
            for (int res : clothings.values()) {
                ans *= (res+1);
            }
            System.out.println(ans-1);
        }

    }
}
