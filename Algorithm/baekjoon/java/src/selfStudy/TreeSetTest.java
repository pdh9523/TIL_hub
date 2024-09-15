package selfStudy;

import java.util.HashMap;
import java.util.TreeSet;

public class TreeSetTest {

    public static void main(String[] args) {
        HashMap<Integer, TreeSet<Integer>> table = new HashMap<>();
        // 정렬을 위한 세트
        TreeSet<Integer> test = new TreeSet<>();
        test.add(5);
        test.add(2);
        table.put(1, test);
        test.add(3);
        table.put(2, test);
        System.out.println(table);
    }
}
