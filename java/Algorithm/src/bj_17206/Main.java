package bj_17206;

import java.util.*;
import java.io.*;

public class Main {
	public static void main(String args[]) throws IOException {
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int[] ans = new int[80001];
		ans[10] = 25;
		for (int i=11; i <=80000; i++) {
			if (i%3==0 || i%7==0) {
				ans[i] += ans[i-1]+i;
			}
			else {
				ans[i] = ans[i-1];
			}
		}
		
		StringBuilder sb = new StringBuilder();
		
		for (int i=0; i<t; i++) {
			int n = Integer.parseInt(st.nextToken());
			sb.append(ans[n] + "\n");
		}
		System.out.println(sb);
	}
}