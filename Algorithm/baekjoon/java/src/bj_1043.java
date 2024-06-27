import java.io.*;
import java.util.*;

public class bj_1043 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        // N,M
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // T, truth
        Set<Integer> truth = new HashSet<>();
        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for (int i=0; i<T; i++) {
            truth.add(Integer.parseInt(st.nextToken()));
        }

        // member, members
        Set<Integer>[] members = new Set[M];
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int mem = Integer.parseInt(st.nextToken());
            Set<Integer> member = new HashSet<>();
            for (int j=0; j<mem; j++) {
                member.add(Integer.parseInt(st.nextToken()));
            }
            members[i] = member;
        }
        // 합친 세트 만들기
        for (int i=0; i<M; i++) {
            for (Set<Integer> member : members) {
                Set<Integer> tmp = new HashSet<>(member);
                tmp.retainAll(truth);
                if (!tmp.isEmpty()) {
                    truth.addAll(member);
                }
            }
        }
        int cnt = 0;
        for (Set<Integer> member : members) {
            member.retainAll(truth);
            if (member.isEmpty()) cnt++;
        }
        System.out.println(cnt);
    }
}