import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st ;
        // piece
        HashMap<String, List<String>> piece = new HashMap<>();

        piece.put("1", Arrays.asList("4","5"));
        piece.put("3", Arrays.asList("4","5"));
        piece.put("4", Arrays.asList("2","3"));
        piece.put("5", Arrays.asList("8"));
        piece.put("6", Arrays.asList("2","3"));
        piece.put("7", Arrays.asList("8"));
        piece.put("8", Arrays.asList("6","7"));

//        System.out.println(piece);

        int cnt = 0;
        while (true) {
            cnt ++;
            // num
            st = new StringTokenizer(br.readLine());
            String num = st.nextToken();
            int numLength = num.length();

            // 입력이 0 인 경우
            if (num.equals("0")) break;
            // 시작이 1, 끝이 2가 아닌 경우
            if ( num.charAt(0) != '1' || num.charAt(numLength-1) != '2' ) {
                System.out.printf("%s. NOT%n", cnt);
                continue;
            }
            // 일반적인 경우
            boolean check = true;
            for (int i=0; i<numLength-1; i++) {
                String n = String.valueOf(num.charAt(i));
                String nextN = String.valueOf(num.charAt(i+1));
                if (!piece.containsKey(n) || !piece.get(n).contains(nextN) ) {
                    System.out.printf("%s. NOT%n", cnt);
                    check = false;
                    break;
                }
            }
            if (check) {
                System.out.printf("%s. VALID%n",cnt);
            }
        }
    }
}
