package swea_1231;

import java.io.*;
import java.util.*;

public class Main {
    public static void inOrder(int[][] tree, String[] arr, int node) {
        if (tree[node][0]!=0) {
            inOrder(tree,arr,tree[node][0]);
        }
        System.out.println(arr[node]);
        if (tree[node][1]!=0) {
            inOrder(tree,arr,tree[node][1]);
        }
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st ;
        // tc
        st = new StringTokenizer(br.readLine());
        int tc = Integer.parseInt(st.nextToken());

        for (int i=1; i < tc+1; i++ ) {
            // N
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());

            String[] arr = new String[N+1];
            int[][] tree = new int[N+1][2];

            for (int j=0; j<N; j++ ) {
                st = new StringTokenizer(br.readLine());
                int M = Integer.parseInt(st.nextToken());
                String T = st.nextToken();
                arr[j+1] = T;
                for (int k = 0; k < 2; k++) {
                    try {
                        tree[M][k] = Integer.parseInt(st.nextToken());
                    } catch (NoSuchElementException e) {
                        continue;
                    }
                }
            }
            inOrder(tree,
                    arr,
                    1);
        }
    }
}
