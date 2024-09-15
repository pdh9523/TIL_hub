package selfStudy;

import java.util.HashMap;
import java.util.Objects;

public class HashMapTest {

    static class Tuple {
        int x;
        int y;
        int z;

        Tuple(int x, int y, int z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }

        // 게터는 오버라이드 할 필요 없음.
        // 오버라이드 해야 하는 것: equals, hashCode, toString
        // 덤: compareTo

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;

            if (o == null || getClass() != o.getClass()) return false;

            Tuple tuple = (Tuple) o;
            return y == tuple.y &&
                    Objects.equals(x, tuple.x) &&
                    Objects.equals(z, tuple.z);
        }

        @Override
        public int hashCode() {
            return Objects.hash(x,y,z);
        }

        @Override
        public String toString() {
            return "(" + x + "," + y + "," + z + ")";
        }
    }

    public static void main(String[] args) throws Exception {
        HashMap<String, Integer> data = new HashMap<>();
        data.put("test", 1);
        System.out.println(data);
        data.put("test", 2);
        System.out.println(data);
        data.put("test", data.get("test")+1);
        data.put("another", data.getOrDefault("another", 0)+1);
        System.out.println(data);

        // 튜플을 키값으로 넣는 경우
        HashMap<Tuple, String> map = new HashMap<>();
        Tuple tuple = new Tuple(1,2,3);
        map.put(tuple, "test");
        //
        System.out.println(map);
        //
        map.put(tuple, "test2");
        System.out.println(map);
    }
}
