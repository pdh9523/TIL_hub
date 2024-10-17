import java.util.Arrays;

public class test {

//    static class Test {
//        int x;
//
//        public Test(int x) {
//            this.x = x;
//        }
//
//        @Override
//        public String toString() {
//            return "x:"+ x;
//        }
//    }
//    public static void main(String[] args) throws Exception {
//        Test a = new Test(2);
//        System.out.println("in out: "+a);
//        foo(a);
//        System.out.println("in out: "+a);
//    }
//
//    private static void foo(Test b) {
//        System.out.println("in function: "+b);
//        b = new Test(1);
//        System.out.println("in function: "+b);
//    }

    private static void func(int i, int[] j) {
        i = 20;
        j[3] = 400;
    }

    public static void main(String[] args) {
        int i = 10, j[] = {1, 2, 3, 4};

        func(i, j);
        System.out.println(i);
        System.out.println(Arrays.toString(j));
    }
}
