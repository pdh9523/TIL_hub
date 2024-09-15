package selfStudy;

public class StringTest {

    static StringBuffer sb = new StringBuffer();

    public static void main(String[] args) throws Exception {
        String test = "리빙포인트:치킨이먹고싶을떈치킨을시키면된다.";
        char ch = test.charAt(6);
        System.out.println(ch);
        String sliced = test.substring(1);
        System.out.println(sliced);
        String sliced2 = sliced.substring(1,5);
        System.out.println(sliced2);
        for (int i=0; i<test.length()-1; i++) {
            System.out.println(test.charAt(i));
        }
        for (int i=test.length()-1; i>=0; i--) {
            sb.append(test.charAt(i));
        }

        System.out.println(sb);
    }
}
