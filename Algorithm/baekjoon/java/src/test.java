class Container<T> {
    T value;

    public Container(T t) {
        this.value = t;
    }

    public void print() {
        new Printer().print(this.value);
    }

    static class Printer {
        public void print(Integer a) {
            System.out.println("A" + a);
        }
        public void print(Object a) {
            System.out.println("B" + a);
        }
        public void print(Number a) {
            System.out.println("C" + a);
        }
    }
}
public class test {
    public static void main(String[] args) {
        new Container<>(0).print();
    }
}
