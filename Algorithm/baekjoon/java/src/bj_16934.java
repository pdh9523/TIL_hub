import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class bj_16934 {

    private static class Trie {
        TrieNode root;

        public Trie() {
            root = new TrieNode();
        }

        public void insert(String word) {
            TrieNode now = root;

            for (char c: word.toCharArray()) {
                now.children.putIfAbsent(c, new TrieNode());
                now = now.children.get(c);
            }
            now.count ++ ;
        }

        public String search(String word) {
            TrieNode now = root;
            StringBuilder ans = new StringBuilder();
            for (char c: word.toCharArray()) {
                ans.append(c);
                if (!now.children.containsKey(c)) return ans.toString();
                now = now.children.get(c);
            }
            if (now.count > 0) {
                ans.append(now.count + 1);
            }
            return ans.toString();
        }
    }

    private static class TrieNode {
        
        HashMap<Character, TrieNode> children;
        int count;

        private TrieNode() {
            children = new HashMap<>();
            count = 0;
        }
    }


    static Trie trie = new Trie();
    static StringBuffer sb = new StringBuffer();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            String word = st.nextToken();
            sb.append(trie.search(word)).append("\n");
            trie.insert(word);
        }
        System.out.println(sb);
    }
}
