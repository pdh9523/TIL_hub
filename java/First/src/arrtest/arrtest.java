package arrtest;

import java.util.Arrays;

public class arrtest {
	public static void main(String args[]) {
		int intArray [] = {1,3,5,7,9} ;
		// 순회 1
		for (int i=0 ; i < intArray.length ; i++) {
			System.out.println(intArray[i]);
		}
		// 순회 2 
		for ( int x : intArray ) {
			System.out.println(x);
		}
		// 리스트 출력
		System.out.println(Arrays.toString(intArray));
		
		// 최대값 최소값 (1)
		int min = 1000;
		int max = 0 ;
		
		for (int num: intArray) {
			if (num > max) {
				max = num ;
			}
			if (num < min) {
				min = num ;
			}
		}
		System.out.printf("min : %d, max : %d %n", min, max);
		
		// 최대값 최소값 (2)
		
		int min_2 = Integer.MAX_VALUE;
		int max_2 = Integer.MIN_VALUE;
		
		for (int num : intArray) { 
			min_2 = Math.min(min_2,num);
			max_2 = Math.max(max_2,num);
			
		}
		System.out.printf("min : %d, max : %d %n", min, max);
		
		// count 구하기
		
		int[] newArray = {1,1,1,2,3,4,5,6,6,6,7,8,8,8,8,8};
		int[] used = new int[10];
		
		for(int num: newArray) {
			used[num]++;
		}
		System.out.println(Arrays.toString(used));
	}
}
