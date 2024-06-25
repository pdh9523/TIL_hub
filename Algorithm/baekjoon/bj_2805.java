package bj_2805;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st ;

        // N,M : 나무 개수, 나무 길이
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // trees : 나무들의 길이
        // start : 시작 값
        // end : 나무 중 가장 긴 나무
        int start = 1;
        int end = 0;
        st = new StringTokenizer(br.readLine());
        int[] trees = new int[N];
        int data ;
        for (int i=0; i<N; i++) {
            data = Integer.parseInt(st.nextToken());
            end = Math.max(end,data);
            trees[i] = data;
        }
        // mid : 이분탐색에서의 중간값
        int mid;
        //
        long res;
        while (start <= end) {
            mid = (start+end)/2;

            res = 0;
            for (int tree : trees) {
                if (tree>=mid) {
                    res += tree-mid;
                }
            }
            if (res>=M) {
                start = mid+1;
            } else {
                end = mid-1;
            }
        }
        System.out.println(end);
    }
}
