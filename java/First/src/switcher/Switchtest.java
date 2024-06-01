package switcher;

import java.util.Scanner;

public class Switchtest {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int a ;
		a = sc.nextInt();
		switch (a) { 
		case 1:
			System.out.println("!입력시");
		case 2:
			System.out.println("2입력시");
		case 3:
			System.out.println("3입력시");
		default :
			System.out.println("기본");	
		}
	}
}
