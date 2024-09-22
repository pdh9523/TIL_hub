import java.util.HashMap;
import java.util.TreeSet;

public class b0921 {

    private static class RESULT {
        int success;
        String word;
    }

    HashMap<Integer, TreeSet<String>> dict;
    HashMap<Integer, Integer> dictIndex;

    public char getKey(String word) {
        return word.charAt(0);
    }

    public int hashing(char i) {
        return i-'a';
    }

    public void init(int N, String[] mWords) {
        dict = new HashMap<>();
        dictIndex = new HashMap<>();

        for (int i=0; i<26; i++) {
            dict.put(i, new TreeSet<>());
            dictIndex.put(i, 0);
        }

        for (int i=0; i<N; i++) {
            String word = mWords[i];
            int key = hashing(getKey(word));
            dict.get(key).add(word);
            dictIndex.put(key, dictIndex.get(key)+1);
        }
    }

    public int add(String word) {
        int key = hashing(getKey(word));
        TreeSet<String> wordTree = dict.get(key);
        if (wordTree.contains(word)) {
            return 0;
        }
        wordTree.add(word);
        dictIndex.put(key, dictIndex.get(key)+1);
        return 1;
    }

    public int remove(String word) {
        int key = hashing(getKey(word));
        TreeSet<String> wordTree = dict.get(key);

        if (!wordTree.contains(word)) {
            return 0;
        }
        wordTree.remove(word);
        dictIndex.put(key, dictIndex.get(key)-1);
        return 1;
    }
    // 여기가 좀 걸리긴함.
    public RESULT query(char mInitial, int mIndex) {
        RESULT res = new RESULT();
        int key = hashing(mInitial);
        if (dictIndex.get(key) < mIndex) {
            res.success = 0;
        } else {
            TreeSet<String> wordTree = dict.get(key);
            int i=1;
            for (String word: wordTree) {
                if (i==mIndex) {
                    res.success = 1;
                    res.word = word;
                    break;
                }
            }
        }
        return res;
    }

    public int getIndex(String word) {
        int key = hashing(getKey(word));
        int ans = 0;

        for (int i=0; i<key; i++) {
            ans += dictIndex.get(i);
        }
        TreeSet<String> wordTree = dict.get(key);
        ans += wordTree.headSet(word, true).size();

        return ans;
    }
}